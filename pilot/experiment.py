"""Bounded pilot; see PRESPEC.md. Levels and increments are not interchangeable."""
import numpy as np
from scipy.signal import welch, resample_poly
from scipy.ndimage import gaussian_filter1d
from scipy.stats import linregress


def estimate(levels, dt, lags_physical, segment_length, bounds):
    x = np.asarray(levels)
    lags = np.rint(np.asarray(lags_physical)/dt).astype(int)
    nper = int(round(segment_length/dt))
    if (len(x)<512 or not np.isfinite(x).all() or np.var(x)<=0
            or len(lags)<20 or lags.min()<1 or len(x)-lags.max()<100
            or not np.allclose(lags*dt,lags_physical,atol=1e-7)
            or len(x)-1 < nper+nper//2 or .5/dt <= 1/bounds[0]):
        raise ValueError('Invalid data, unequal scale grid, or insufficient physical support')
    gamma = np.array([.5*np.mean((x[k:]-x[:-k])**2) for k in lags])
    f,p = welch(np.diff(x),fs=1/dt,window='hann',nperseg=nper,
                noverlap=nper//2,detrend='constant',scaling='density')
    mask=(f>=1/bounds[1]) & (f<=1/bounds[0])
    f,p=f[mask],p[mask]
    if len(f)<20 or np.any(gamma<=0) or np.any(p<=0):
        raise ValueError('Insufficient positive fit data')
    v=linregress(np.log(lags_physical),np.log(gamma))
    s=linregress(np.log(f),np.log(p))
    return {'n':len(x),'dt':dt,'bounds':list(bounds),'nperseg':nper,
            'segments':1+(len(x)-1-nper)//(nper-nper//2),
            'variogram':{'H':v.slope/2,'slope':v.slope,'r2':v.rvalue**2,
                         'lags':list(map(float,lags_physical)),'gamma':gamma.tolist(),
                         'minimum_pairs':int(len(x)-lags.max())},
            'spectral':{'H':(1-s.slope)/2,'slope':s.slope,'r2':s.rvalue**2,
                        'frequencies':f.tolist(),'psd_increments':p.tolist(),
                        'input':'first differences of levels; low-frequency fGn relation'}}



def blocks(depth, gr, dt):
    valid=np.isfinite(depth)&np.isfinite(gr)
    result=[]
    start=None
    for i in range(len(gr)):
        connected=(i>0 and valid[i-1] and depth[i]>depth[i-1]
                   and abs(depth[i]-depth[i-1]-dt)<=.0005)
        if start is not None and (not valid[i] or not connected):
            result.append((start,i)); start=None
        if valid[i] and start is None:
            start=i
    if start is not None:
        result.append((start,len(gr)))
    return result


def variants(depth, gr, dt):
    result={'baseline':(depth[40:-40],gr[40:-40],dt),
            'smooth':(depth[40:-40],gaussian_filter1d(gr,.304/dt,mode='reflect')[40:-40],dt)}
    for q in [2,4]:
        y=resample_poly(gr,1,q,window=('kaiser',5.),padtype='line')
        trim=40//q
        result[f'down{q}']=(depth[::q][trim:-trim],y[trim:-trim],dt*q)
    return result


def generate(h, n, seed):
    if not 0 < h < 1 or n < 2:
        raise ValueError('Need 0<H<1 and n>=2')
    k = np.arange(n+1, dtype=float)
    r = .5*((k+1)**(2*h)-2*k**(2*h)+abs(k-1)**(2*h))
    row = np.r_[r, r[-2:0:-1]]
    eigen = np.fft.fft(row).real
    if eigen.min() < -1e-10:
        raise ValueError('Circulant embedding not PSD; no approximate fallback')
    eigen = np.maximum(eigen, 0)
    white = np.random.default_rng(seed).normal(size=2*n)
    increments = np.fft.ifft(np.sqrt(eigen)*np.fft.fft(white)).real[:n]
    return increments, np.r_[0., np.cumsum(increments)], eigen


def run(out_dir):
    import json, hashlib, platform
    from pathlib import Path
    import lasio
    from plot import make_plots
    root=Path(__file__).resolve().parent
    out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    def dump(name, obj):
        def json_default(value):
            if isinstance(value, np.generic):
                return value.item()
            raise TypeError(f'Object of type {type(value).__name__} is not JSON serializable')
        (out/name).write_text(json.dumps(obj, indent=2, allow_nan=False,
                                         default=json_default) + '\n')
    result={'synthetic':[],'real':[],'synthetic_summary':[],
            'prespec_sha256':hashlib.sha256((root/'PRESPEC.md').read_bytes()).hexdigest(),
            'python':platform.python_version(),
            'interpretation':'GR H values are apparent scaling summaries, not validated geological H.'}
    print('Known-answer validation: fGn increments -> cumulative fBm levels; no tuning.')
    arrays={}
    for h in [.2,.5,.8]:
        for seed in [11,22,33,44]:
            increments,levels,eigen=generate(h,8192,seed)
            fit=estimate(levels,1.,np.arange(20,161,4),2048.,(20.,160.))
            result['synthetic'].append({'H_true':h,'seed':seed,'eigen_min':float(eigen.min()),'fit':fit})
            arrays[f'H{h}_seed{seed}_levels']=levels
        for method in ['variogram','spectral']:
            errors=np.array([s['fit'][method]['H']-h for s in result['synthetic'] if s['H_true']==h])
            bias=float(errors.mean()); rmse=float(np.sqrt(np.mean(errors**2)))
            row={'H_true':h,'method':method,'bias':bias,'rmse':rmse,'pass':abs(bias)<=.12 and rmse<=.18}
            result['synthetic_summary'].append(row); print(row)
    np.savez_compressed(out/'synthetic_levels.npz',**arrays)
    result['synthetic_gate']=all(s['pass'] for s in result['synthetic_summary'])
    print('FORCE: deterministic contiguous finite GR selection; fixed physical scales, no geology ground truth.')
    source=root.parent/'data/force2020/extracted'
    paths=sorted(source.rglob('*.las'),key=lambda p:p.relative_to(source).as_posix())
    manifest={'source_root':str(source),'candidates_total':len(paths),'selected':[],'rejected':[]}
    for path in paths:
        rel=path.relative_to(source).as_posix()
        las=lasio.read(path)
        if 'GR' not in las.curves.keys() or las.curves[0].unit.lower() not in ['m','metre','meter']:
            manifest['rejected'].append({'path':rel,'reason':'GR absent or depth not metres'}); continue
        depth=np.asarray(las.index); gr=np.asarray(las['GR']).copy()
        gr[gr==float(las.well['NULL'].value)]=np.nan
        dt=float(las.well['STEP'].value)
        if dt<=0:
            manifest['rejected'].append({'path':rel,'reason':'nonpositive STEP'}); continue
        candidates=blocks(depth,gr,dt)
        candidates.sort(key=lambda b: (-(b[1]-b[0]),b[0]))
        if not candidates or candidates[0][1]-candidates[0][0]<4097:
            manifest['rejected'].append({'path':rel,'reason':'no >=4097 contiguous finite uniform GR points'}); continue
        start,stop=candidates[0]; end=start+4097
        d,x=depth[start:end],gr[start:end]
        lags=np.arange(4, int(np.floor(24.32/dt))+1,4)*dt
        lags=lags[(lags>=3.04-1e-10)&(lags<=24.32+1e-10)]
        vfit={}; saved={}
        try:
            for name,(z,y,spacing) in variants(d,x,dt).items():
                fit=estimate(y,spacing,lags,311.296,(3.04,24.32))
                fit['depth_range']=[float(z[0]),float(z[-1])]
                vfit[name]=fit; saved[name+'_depth']=z; saved[name+'_GR']=y
        except ValueError as exc:
            manifest['rejected'].append({'path':rel,'reason':str(exc)}); continue
        entry={'path':rel,'absolute_path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
               'well':str(las.well['WELL'].value),'depth_unit':las.curves[0].unit,'gr_unit':las.curves['GR'].unit,
               'block_rows_half_open':[start,stop],'selected_rows_half_open':[start,end],
               'depth_range':[float(d[0]),float(d[-1])],'analysis_depth_range':vfit['baseline']['depth_range'],
               'points':len(x),'dt_declared':dt,'dt_min':float(np.diff(d).min()),'dt_max':float(np.diff(d).max()),
               'max_step_error':float(np.max(abs(np.diff(d)-dt))),'rounding_tolerance_m':.0005}
        manifest['selected'].append(entry)
        np.savez_compressed(out/f'well_{len(manifest["selected"])}.npz',original_depth=d,original_GR=x,**saved)
        deltas={name:{method:fit[method]['H']-vfit['baseline'][method]['H'] for method in ['variogram','spectral']}
                for name,fit in vfit.items() if name!='baseline'}
        disagreement=abs(vfit['baseline']['variogram']['H']-vfit['baseline']['spectral']['H'])
        stable=all(abs(v)<=.10 for row in deltas.values() for v in row.values()) and disagreement<=.15
        result['real'].append({'well':path.stem,'variants':vfit,'deltas':deltas,'baseline_disagreement':disagreement,'pass':stable})
        print(path.stem, 'baseline H', {k:vfit['baseline'][k]['H'] for k in ['variogram','spectral']},'deltas',deltas,'pass',stable)
        if len(result['real'])==3:
            break
    result['real_gate']=len(result['real'])==3 and all(w['pass'] for w in result['real'])
    result['decision']='GO (bounded follow-up only)' if result['synthetic_gate'] and result['real_gate'] else 'NO-GO for stable single-H interpretation'
    dump('selection_manifest.json',manifest); dump('final_info.json',result)
    make_plots(result,out)
    report=['# Bounded MTP pilot', '',result['decision'], '',
            f'Synthetic gate: {result["synthetic_gate"]}. Real robustness gate: {result["real_gate"]}.',
            '', '| Known H | Method | Mean bias | RMSE | Pass |','|---|---|---|---|---|']
    for s in result['synthetic_summary']:
        report.append(f'|{s["H_true"]}|{s["method"]}|{s["bias"]:.4f}|{s["rmse"]:.4f}|{s["pass"]}|')
    report+=['','| Well | Baseline variogram H | Baseline spectral H | Largest absolute variant change | Pass |','|---|---|---|---|---|']
    for w in result['real']:
        change=max(abs(v) for row in w['deltas'].values() for v in row.values())
        report.append(f'|{w["well"]}|{w["variants"]["baseline"]["variogram"]["H"]:.4f}|{w["variants"]["baseline"]["spectral"]["H"]:.4f}|{change:.4f}|{w["pass"]}|')
    report+=['','## Limits and next step',
             'FORCE is already cleaned/despiked: baseline means supplied GR, not raw-tool truth. No geological accuracy, lithology prediction or graph-dimension claims. Gaussian nonstationary fBm levels have stationary fGn increments; real GR is not established to follow either model.',
             'Four seeds per known H and three deterministically selected intervals are a sanity check, not a population study. Welch frequency ordinates and variogram lags are dependent; regression R² is descriptive, not a confidence interval or proof of scaling. Spectral H uses the low-frequency fGn asymptote after differencing, with possible finite-frequency/discretization bias.',
             'Intervals may cross geological regimes. Nominal uniform spacing accepts LAS rounding within 0.0005 m; actual extrema are in the manifest. Smoothing and resampling measure processing sensitivity, not restoration or ground-truth error.',
             'If NO-GO: investigate stationarity, scale dependence and estimator disagreement before any geological or fractal interpretation. If GO: only expand controlled validation, not a full MTP build. No thresholds or seeds were tuned after results.']
    (out/'report.md').write_text('\n'.join(report)+'\n')
    print(result['decision'])
    return result


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--out_dir',default='run_1')
    run(parser.parse_args().out_dir)

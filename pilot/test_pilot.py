import importlib.util
from pathlib import Path
import numpy as np
import pytest


def module():
    assert Path('experiment.py').exists(), 'pilot implementation missing'
    import experiment
    return experiment


def test_estimation_and_controls():
    m = module()
    assert hasattr(m, 'estimate'), 'estimation missing'
    levels = m.generate(.5,8192,11)[1]
    result = m.estimate(levels,1.,np.arange(20,161,4),2048.,(20.,160.))
    for method in ['variogram','spectral']:
        assert abs(result[method]['H']-.5) < .18
    for x in [np.ones(8193), levels[:100]]:
        with pytest.raises(ValueError):
            m.estimate(x,1.,np.arange(20,161,4),2048.,(20.,160.))
    with pytest.raises(ValueError):
        m.estimate(levels,3.,np.arange(20,161,4),2048.,(20.,160.))


def test_contiguous_variants():
    m=module()
    assert hasattr(m,'blocks'), 'contiguous selection missing'
    d=np.arange(20,dtype=float); x=np.ones(20); x[5]=np.nan; d[12:]+=1
    assert m.blocks(d,x,1.) == [(0,5),(6,12),(12,20)]
    d=np.arange(4097)*.152
    x=np.sin(2*np.pi*.4*np.arange(4097))
    variants=m.variants(d,x,.152)
    for key,(z,y,dt) in variants.items():
        assert z[0]==d[40] and z[-1]==d[-41]
        np.testing.assert_allclose(np.diff(z),dt,atol=1e-10)
        assert len(z)==len(y)
    assert np.std(variants['down4'][1]) < .01*np.std(variants['baseline'][1])


def test_bounded_run_artifacts(tmp_path):
    m=module()
    assert hasattr(m,'run'), 'bounded runner missing'
    import json
    m.run(tmp_path)
    r=json.loads((tmp_path/'final_info.json').read_text())
    assert len(r['synthetic'])==12 and len(r['real'])==3
    manifest=json.loads((tmp_path/'selection_manifest.json').read_text())
    assert len(manifest['selected'])==3
    for entry in manifest['selected']:
        assert len(entry['sha256'])==64 and entry['points']==4097
    for well in r['real']:
        base=well['variants']['baseline']
        for v in well['variants'].values():
            assert v['variogram']['lags']==base['variogram']['lags']
            np.testing.assert_allclose(v['spectral']['frequencies'],base['spectral']['frequencies'])
            assert v['depth_range']==base['depth_range']
    for name in ['Figure_1.png','Figure_1.pdf','Figure_2.png','Figure_2.pdf','report.md']:
        assert (tmp_path/name).stat().st_size>100


def test_exact_generator():
    m = module()
    for h in [.2, .5, .8]:
        increments, levels, eigen = m.generate(h, 8192, 11)
        np.testing.assert_allclose(np.diff(levels), increments, atol=1e-12)
        k = np.arange(8192)
        expected = .5*((k+1.)**(2*h)-2*k**(2*h)+abs(k-1.)**(2*h))
        np.testing.assert_allclose(np.fft.ifft(eigen).real[:8192], expected, atol=1e-12)
        assert eigen.min() >= 0
        if h == .5:
            np.testing.assert_allclose(expected[1:], 0)
            assert abs(np.var(increments)-1) < .05
        np.testing.assert_array_equal(m.generate(h,8192,11)[0], increments)

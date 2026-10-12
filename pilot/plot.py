"""Plot saved pilot measurements; no invented data or uncertainty intervals."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def make_plots(result,out):
    out=Path(out)
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,
                         'pdf.fonttype':42,'savefig.dpi':300})
    colors=['#0072B2','#D55E00']
    fig,ax=plt.subplots(figsize=(6,4),layout='constrained')
    ax.plot([.1,.9],[.1,.9],color='.5',linestyle='--',label='Known H')
    for j,method in enumerate(['variogram','spectral']):
        for h in [.2,.5,.8]:
            ys=[s['fit'][method]['H'] for s in result['synthetic'] if s['H_true']==h]
            center=h+(j-.5)*.025
            ax.scatter(center+np.linspace(-.005,.005,4),ys,color=colors[j],s=22,alpha=.65)
            ax.scatter(center,np.mean(ys),color=colors[j],s=65,marker='_',label=method if h==.2 else None)
    ax.set(xlabel='Known fBm H',ylabel='Estimated H',xlim=(.1,.9))
    ax.legend(frameon=False)
    for ext in ['png','pdf']:
        fig.savefig(out/f'Figure_1.{ext}')
    plt.close(fig)
    fig,axes=plt.subplots(1,2,figsize=(9,4),layout='constrained',sharey=True)
    names=['smooth','down2','down4']
    for ax,method in zip(axes,['variogram','spectral']):
        for i,w in enumerate(result['real']):
            ax.plot(np.arange(3)+.035*(i-1),[w['deltas'][name][method] for name in names],
                    marker=['o','s','^'][i],color=['#0072B2','#D55E00','#009E73'][i],label=w['well'])
        ax.axhline(0,color='.6',lw=.8)
        for bound in [-.1,.1]: ax.axhline(bound,color='.4',ls='--',lw=.8)
        ax.set_xticks(range(3),['Gaussian\nσ=0.304 m','AA ↓2','AA ↓4'])
        ax.set_xlabel(method.capitalize())
        ax.legend(frameon=False,fontsize=8)
    axes[0].set_ylabel('Δ apparent H from supplied GR baseline')
    for ext in ['png','pdf']: fig.savefig(out/f'Figure_2.{ext}')
    plt.close(fig)


if __name__=='__main__':
    import json, argparse
    p=argparse.ArgumentParser(); p.add_argument('--out_dir',default='run_1')
    out=Path(p.parse_args().out_dir)
    make_plots(json.loads((out/'final_info.json').read_text()),out)

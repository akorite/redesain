"""Trade EV vs resolution: buying YES at p pays 1 on resolve."""
import numpy as np
rng=np.random.default_rng(9)
# buy YES at price p; true prob q; EV per share = q-p
for p,q in ((0.62,0.62),(0.62,0.70),(0.62,0.55),(0.03,0.05)):
    ev=q-p; sharpe=ev/np.sqrt(q*(1-q))
    print(f"buy YES@{p:.2f} true {q:.2f}: EV {ev:+.3f}/share  sigma {np.sqrt(q*(1-q)):.3f}")
# path: price random walk toward resolution at 0/1
T=200; q=0.6
for seed in (1,2):
    r=np.random.default_rng(seed); W=r.random(T)<q
    px=np.convolve(W.astype(float),np.ones(10)/10,'same')
    print(f"seed{seed}: empirical freq drifts to {W.mean():.2f} -> resolves {int(W.mean()>0.5)}")

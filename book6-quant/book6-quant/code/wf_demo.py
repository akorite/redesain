import numpy as np
rng=np.random.default_rng(4)
n=1200
# regime-switching returns: trending then flat then volatile
r=np.empty(n)
r[:400]=rng.normal(0.001,0.01,400)     # drift up
r[400:800]=rng.normal(0,0.005,400)     # quiet
r[800:]=rng.normal(-0.0005,0.02,400)   # volatile
def sharpe(x): return x.mean()/x.std()*np.sqrt(252)
# anchored: train [0,t), test expanding next 200
print("anchored walk-forward:")
for t0 in range(200,1000,200):
    tr=r[:t0]; te=r[t0:t0+200]
    mom=np.sign(np.convolve(tr,np.ones(20)/20,'valid')[-1])
    pnl=mom*te
    print(f"  train 0:{t0}  test {t0}:{t0+200}  IS {sharpe(tr):+.2f}  OOS {sharpe(pnl):+.2f}")
# rolling: fixed 400-bar window
print("rolling (400-bar) walk-forward:")
for t0 in range(0,800,200):
    tr=r[t0:t0+400]; te=r[t0+400:t0+600]
    if len(te)<50: break
    mom=np.sign(np.convolve(tr,np.ones(20)/20,'valid')[-1])
    print(f"  train {t0}:{t0+400}  test {t0+400}:{t0+600}  IS {sharpe(tr):+.2f}  OOS {sharpe(mom*te):+.2f}")

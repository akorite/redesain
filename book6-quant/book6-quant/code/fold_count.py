import numpy as np
rng=np.random.default_rng(4)
n=1200
r=np.empty(n)
r[:400]=rng.normal(0.001,0.01,400)
r[400:800]=rng.normal(0,0.005,400)
r[800:]=rng.normal(-0.0005,0.02,400)
def sharpe(x): return x.mean()/x.std()*np.sqrt(252)
def wf(nfolds):
    step=(n-400)//nfolds
    oos=[]
    for k in range(nfolds):
        t0=400+k*step; te=r[t0:t0+step]
        tr=r[:t0]
        mom=np.sign(np.convolve(tr,np.ones(20)/20,'valid')[-1])
        oos.append(sharpe(mom*te))
    return oos
for k in [2,3,4,6]:
    o=wf(k)
    print(f"{k} folds: mean {np.mean(o):+.2f}  sd {np.std(o):.2f}")
    print("   OOS: " + " ".join(f"{x:+.2f}" for x in o))
print("more folds -> the estimate fragments; the mean is not the spread")

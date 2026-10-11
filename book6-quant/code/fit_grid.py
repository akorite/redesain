import numpy as np
rng=np.random.default_rng(3)
def sharpe(x): return x.mean()/x.std()*np.sqrt(252)
# real-ish daily returns: flat drift + noise
n=1500; r=rng.normal(0.0002,0.02,n)
# grid of SMA pairs
best=(0,None)
for a in range(2,60):
    for b in range(a+5,200,5):
        m1=np.convolve(r,np.ones(a)/a,'valid'); m2=np.convolve(r,np.ones(b)/b,'valid')
        sig=np.sign(m1[-len(m2):]-m2)
        pnl=sig[:-1]*r[-len(sig)+1:]
        s=sharpe(pnl)
        if s>best[0]: best=(s,(a,b))
a,b=best[1]
print(f"grid {len(range(2,60))*len(range(7,200,5))} pairs searched")
print(f"best IS pair: SMA({a},{b}) sharpe {best[0]:+.2f}")
# out-of-sample: fresh seed
r2=rng.normal(0.0002,0.02,n)
m1=np.convolve(r2,np.ones(a)/a,'valid'); m2=np.convolve(r2,np.ones(b)/b,'valid')
sig=np.sign(m1[-len(m2):]-m2); pnl=sig[:-1]*r2[-len(sig)+1:]
print(f"same pair OOS sharpe: {sharpe(pnl):+.2f}")
print("the grid found noise, not edge")

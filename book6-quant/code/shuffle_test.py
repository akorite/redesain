import numpy as np
rng=np.random.default_rng(11)
def sharpe(x): return x.mean()/x.std()*np.sqrt(252)
# "real" series: same as fit_grid (flat drift + noise, no exploitable structure)
n=1500; r=rng.normal(0.0002,0.02,n)
def grid_best(rr):
    best=(0,None)
    for a in range(2,60,6):
        for b in range(a+5,200,15):
            m1=np.convolve(rr,np.ones(a)/a,'valid'); m2=np.convolve(rr,np.ones(b)/b,'valid')
            sig=np.sign(m1[-len(m2):]-m2); pnl=sig[:-1]*rr[-len(sig)+1:]
            s=sharpe(pnl)
            if s>best[0]: best=(s,(a,b))
    return best
b0=grid_best(r)
print(f"original grid: best IS sharpe {b0[0]:+.2f} at SMA{b0[1]}")
# shuffle the returns, destroy all structure, rerun the SAME grid
n_perm=200; cnt=0; mx=[]
for k in range(n_perm):
    rp = rng.permutation(r)
    bs,_ = grid_best(rp)
    mx.append(bs)
    if bs>=b0[0]: cnt+=1
print(f"200 shuffles of the SAME returns: best-IS >= {b0[0]:+.2f} in {cnt} ({cnt/len(mx)*100:.0f}%)")
print(f"shuffle best-IS mean {np.mean(mx):+.2f} -- the grid refits noise to the same height")

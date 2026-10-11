import numpy as np
# three synthetic sleeves: momentum (low vol), funding carry (low vol), market beta (high vol)
rng = np.random.default_rng(11)
n=500
mom = rng.normal(0.0006,0.010,n)      # ~1% daily vol
car = rng.normal(0.0004,0.003,n)      # ~0.3% daily vol (funding-like)
mkt = rng.normal(0.0002,0.025,n)      # ~2.5% daily vol
R = np.column_stack([mom,car,mkt])
vols = R.std(0)
print("sleeve vols:", " ".join(f"{v*100:.2f}%" for v in vols))
# equal-weight vs risk-parity (1/vol) weights
w_eq = np.ones(3)/3
w_rp = (1/vols); w_rp/=w_rp.sum()
for nm,w in [("equal",w_eq),("risk-parity",w_rp)]:
    p = (R*w).sum(1)
    print(f"{nm:>12}: w={np.round(w,3)} port vol {p.std()*100:.2f}%  sharpe {p.mean()/p.std():+.2f}")
# contribution to risk: w_i * (marginal vol) ~ w_i*vols_i for uncorrelated
ctr = w_rp*vols
print(f"risk-parity contributions ~equal: {np.round(ctr/ctr.sum(),3)}")

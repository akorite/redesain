import numpy as np
rng=np.random.default_rng(7)
def sharpe(x): return x.mean()/x.std()*np.sqrt(252)
# 300 zero-edge strategies (random PnL), pick best in-sample
n_strat, n_days = 300, 500
ts=np.empty(n_strat)
for k in range(n_strat):
    r=rng.normal(0,1,n_days)
    ts[k]=sharpe(r)
order=np.argsort(ts)[::-1]
print(f"strategies {n_strat}  days {n_days}")
print(f"true edge: all zero")
print(f"best in-sample sharpe: {ts[order[0]]:+.2f}  (index {order[0]})")
print(f"median sharpe: {np.median(ts):+.2f}")
print(f"# above sharpe 1: {(ts>1).sum()} of {n_strat}")
# expected max under H0 ~ sqrt(2 ln N)
print(f"E[max sharpe] under H0 ~ {np.sqrt(2*np.log(n_strat))/np.sqrt(n_days)*np.sqrt(252):+.2f}")

import numpy as np, csv
rng=np.random.default_rng(6)
def sharpe(x): return x.mean()/x.std()*np.sqrt(252)
def metrics(r):
    eq=np.cumsum(r); peak=np.maximum.accumulate(eq)
    dd=(eq/peak-1) if False else (eq-peak)
    mdd=dd.min()
    hit=(r>0).mean()
    return sharpe(r), mdd, hit
# a "good-looking" strategy: steady +1bp/day with occasional -3% crashes
r=np.concatenate([rng.normal(0.0008,0.004,1150), rng.normal(-0.03,0.01,10)])
np.random.default_rng(1).shuffle(r)
s,mdd,hit=metrics(r)
print(f"tail-risk strategy: sharpe {s:+.2f}  mdd {mdd:+.1%}  hit {hit:.1%}")
# a boring one: same mean, no crashes
r2=rng.normal(0.0009,0.005,1160)
s2,mdd2,hit2=metrics(r2)
print(f"boring strategy:    sharpe {s2:+.2f}  mdd {mdd2:+.1%}  hit {hit2:.1%}")
print("same mean, different product -- the suite shows what sharpe hides")

import numpy as np
rng=np.random.default_rng(12)
# put-selling profile: +0.5%/day 95% of the time, -20% 5%
r=np.where(rng.random(500)<0.05, rng.normal(-0.08,0.02,500), rng.normal(0.007,0.002,500))
s=r.mean()/r.std()*np.sqrt(252)
sk=((r-r.mean())**3).mean()/r.std()**3
print(f"put-seller profile: sharpe {s:+.2f}  skew {sk:+.2f}  worst {r.min():+.1%}")
print("high sharpe can hide a cliff: read skew and worst day too")

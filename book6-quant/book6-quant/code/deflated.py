import numpy as np
from scipy.stats import norm
rng=np.random.default_rng(11)
# N trials' max t-stat vs the multiple-testing-adjusted bar
for N in (10,100,1000):
    ts=np.abs(rng.normal(0,1,5000*N)).reshape(5000,N).max(1)
    print(f"N={N:5d}  95% of max|t| < {np.quantile(ts,0.95):.2f}")
print("Bonferroni t-bar at N=100:", f"{norm.ppf(1-0.05/100):.2f}")
print("single-test t-bar:", f"{norm.ppf(0.975):.2f}")

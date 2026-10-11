import numpy as np
rng=np.random.default_rng(9)
def se_sr(T,sr=1.0): return np.sqrt((1+sr*sr/2)/T)
for T in (63,252,756,2520):
    print(f"T={T:4d} days  se(SR)~{se_sr(T):.3f}  95% CI on SR=1: [{1-1.96*se_sr(T):.2f},{1+1.96*se_sr(T):.2f}]")
# empirical check: 2000 sims of 252 days at true SR 1
srs=np.empty(2000)
for k in range(2000):
    r=rng.normal(0.0001/0.005,1,252)*0.005
    srs[k]=r.mean()/r.std()*np.sqrt(252)
print(f"empirical se over 2000 sims (T=252): {srs.std():.3f}")

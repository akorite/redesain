import numpy as np
np.set_printoptions(precision=3, suppress=True)
rng = np.random.default_rng(0)
# sum of exponentials (very skewed) -> Gaussian as n grows
for n in [1, 4, 32]:
    s = rng.exponential(1.0, (n, 100_000)).sum(axis=0)
    z = (s - n) / np.sqrt(n)          # mean n, var n
    print(f"n={n:2d}: mean {z.mean():+.3f}  var {z.var():.3f}  "
          f"skew {np.mean(((z-z.mean())/z.std())**3):+.3f}")
# bin counts for a histogram row (n=32) matching the figure
z = (rng.exponential(1.0,(32,100_000)).sum(axis=0)-32)/np.sqrt(32)
h, e = np.histogram(z, bins=[-3,-2,-1,0,1,2,3], density=True)
print("n=32 histogram density per bin:", h)

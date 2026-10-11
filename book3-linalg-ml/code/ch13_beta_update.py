import numpy as np
rng = np.random.default_rng(1)
# Beta(2,2) prior, coin true p=0.65, update after each batch
a, b = 2., 2.
for n in [0, 10, 100, 1000]:
    flips = rng.binomial(1, 0.65, n).sum() if n else 0
    a += flips; b += n - flips
    print(f"after {n:4d} flips ({flips:3d} H): Beta({a:.0f},{b:.0f})"
          f"  post-mean {a/(a+b):.3f}  MAP {(a-1)/(a+b-2):.3f}")

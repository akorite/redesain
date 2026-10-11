"""acf_panel.py -- autocorrelation of r_t vs |r_t| on a synthetic GARCH.

Planted truth: GARCH(1,1) with w=0.000002, a=0.08, b=0.90 on daily log
returns -- returns themselves are (nearly) serially uncorrelated, but
their magnitudes cluster. This is the 'volatility clustering' signature
every real return series shows.
"""
import numpy as np

rng = np.random.default_rng(5)
T = 2000
W, A, B = 2e-6, 0.08, 0.90
sig2 = np.empty(T)
sig2[0] = W / (1 - A - B)
r = np.empty(T)
for t in range(T):
    if t:
        sig2[t] = W + A * r[t - 1] ** 2 + B * sig2[t - 1]
    r[t] = np.sqrt(sig2[t]) * rng.standard_normal()


def acf(x, k):
    x = x - x.mean()
    return np.array([np.dot(x[:-i], x[i:]) / np.dot(x, x)
                     for i in range(1, k + 1)])


a_r = acf(r, 15)
a_a = acf(np.abs(r), 15)
print("lag :   ACF(r)   ACF(|r|)")
for i in range(15):
    print(f"{i+1:3d} : {a_r[i]:+.4f}  {a_a[i]:+.4f}")
# pgfplots coordinate rows for fig04
print("\nCOORDS_R " + " ".join(f"({i+1},{a_r[i]:.4f})" for i in range(15)))
print("COORDS_A " + " ".join(f"({i+1},{a_a[i]:.4f})" for i in range(15)))

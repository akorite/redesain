"""gbm_demo.py -- WE1: synthetic geometric Brownian motion.

Plant a known drift and volatility, generate one path, and check that
(a) simple and log returns tell the same story to 2 decimals,
(b) log returns telescope exactly.
Truth planted: mu = 8%/yr, sigma = 60%/yr, daily bars (365/yr).
"""
import numpy as np
from returns import simple_returns, log_returns

rng = np.random.default_rng(7)
T = 365                      # one year of daily bars
MU, SIGMA = 0.08, 0.60       # planted truth, per year
dt = 1.0 / 365
eps = rng.standard_normal(T)
r = (MU - 0.5 * SIGMA**2) * dt + SIGMA * np.sqrt(dt) * eps   # log returns
P = 100.0 * np.exp(np.cumsum(r))
P = np.concatenate([[100.0], P])                            # prepend start

R = simple_returns(P)
rr = log_returns(P)
print("final price      =", round(P[-1], 2))
print("mean R per bar   =", round(R.mean(), 6))
print("mean r per bar   =", round(rr.mean(), 6))
print("sd   r per bar   =", round(rr.std(ddof=1), 6))
print("max|R-r| (bp)    =", round(1e4 * np.abs(R - rr).max(), 2))
print("sum(r)           =", round(rr.sum(), 6))
print("log(P_T/P_0)     =", round(np.log(P[-1] / P[0]), 6))
print("planted sigma    =", SIGMA, "-> annualised est =",
      round(rr.std(ddof=1) * np.sqrt(365), 3))

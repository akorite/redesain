"""drawdown_demo.py -- running maximum, drawdown, MDD (sec:risk).

Equity path from the planted GBM of gbm_demo (same seed), so the
numbers in the chapter and the figure agree.
"""
import numpy as np

rng = np.random.default_rng(7)
T = 365
MU, SIGMA = 0.08, 0.60
dt = 1.0 / 365
eps = rng.standard_normal(T)
W = 100.0 * np.exp(np.cumsum((MU - 0.5 * SIGMA**2) * dt
                             + SIGMA * np.sqrt(dt) * eps))
W = np.concatenate([[100.0], W])

peak = np.maximum.accumulate(W)
dd = W / peak - 1.0          # drawdown as a fraction (<= 0)
mdd = dd.min()
t_mdd = int(dd.argmin())
print("final equity  =", round(W[-1], 2))
print("max equity    =", round(peak.max(), 2))
print("MDD           =", round(mdd, 4), " at bar", t_mdd)
print("recovery bars =", int(len(W) - 1 - t_mdd), " after the trough")
# figure data: equity curve every 5 bars
sel = list(range(0, len(W), 5))
print("COORDS_W  " + " ".join(f"({i},{W[i]:.1f})" for i in sel))
print("COORDS_PK " + " ".join(f"({i},{peak[i]:.1f})" for i in sel))

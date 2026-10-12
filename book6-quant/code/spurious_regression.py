"""Regress one random walk on another, independent one.

If the regression were meaningful, R^2 would be near 0 almost always.
Run: python3 spurious_regression.py
"""
import numpy as np

rng = np.random.default_rng(7)
T, trials = 500, 2000
r2_levels, r2_changes = [], []
for _ in range(trials):
    a = np.cumsum(rng.standard_normal(T))      # random walk 1 (a "price")
    b = np.cumsum(rng.standard_normal(T))      # random walk 2, independent of 1
    r2_levels.append(np.corrcoef(a, b)[0, 1] ** 2)
    r2_changes.append(np.corrcoef(np.diff(a), np.diff(b))[0, 1] ** 2)

r2_levels, r2_changes = np.array(r2_levels), np.array(r2_changes)
print(f"levels : median R^2 = {np.median(r2_levels):.3f}, share with R^2 > 0.3 = {np.mean(r2_levels > 0.3):.3f}")
print(f"changes: median R^2 = {np.median(r2_changes):.4f}, share with R^2 > 0.3 = {np.mean(r2_changes > 0.3):.3f}")

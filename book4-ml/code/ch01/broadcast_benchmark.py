# code/ch01/broadcast_benchmark.py -- loop vs vectorised, timed for real.
# Run from the repository root:  python3 code/ch01/broadcast_benchmark.py
import math
import statistics
import time
import warnings
import numpy as np

# this platform's BLAS fires a spurious RuntimeWarning on first use of a ufunc
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    np.eye(2) @ np.ones(2)
    np.arange(4) @ np.ones(4)

rng = np.random.default_rng(0)
n, d = 10_000, 4
X = rng.normal(size=(n, d))
w = rng.normal(size=d)
mu = X.mean(axis=0)
Xl, wl, mul = X.tolist(), w.tolist(), mu.tolist()   # same data as Python lists

def bench(fn, reps=5):
    fn()                                   # warmup: BLAS/Lazy-inits excluded
    ts = []
    for _ in range(reps):
        t0 = time.perf_counter()
        out = fn()
        ts.append(time.perf_counter() - t0)
    return statistics.median(ts), out

# --- (a) row scores  s_i = x_i . w   (the workhorse of linear models) ---
t_py, s_py = bench(lambda: [
    sum(x * wi for x, wi in zip(row, wl)) for row in Xl], 3)
t_npl, s_npl = bench(lambda: np.array([X[i] @ w for i in range(n)]), 3)
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    t_vec, s_vec = bench(lambda: X @ w, 50)

# --- (b) distance of every row to the column mean, n = 10^4 ---
t_dp, d_py = bench(lambda: [
    math.sqrt(sum((x - m) ** 2 for x, m in zip(row, mul))) for row in Xl], 3)
t_dv, d_vec = bench(lambda: np.sqrt(((X - mu) ** 2).sum(axis=1)), 50)

# --- (c) pairwise distances on the first 2,000 rows ---
m = 2000
A, Al = X[:m], Xl[:m]
t_pp, P_py = bench(lambda: [
    [math.sqrt(sum((a - b) ** 2 for a, b in zip(ra, rb))) for rb in Al]
    for ra in Al], 1)
t_pv, P_vec = bench(lambda: np.sqrt(((A[:, None, :] - A[None, :, :]) ** 2).sum(-1)), 20)

print(f"X: {n} x {d} float64   (pairwise row uses first {m} rows; median of warm runs)")
print(f"{'operation':<32}{'python loop':>12}{'np call/row':>12}{'vectorised':>12}{'slowest/vec':>13}")
for name, a, b, c in [("row scores X @ w", t_py, t_npl, t_vec),
                      ("row distances to mean", t_dp, float("nan"), t_dv),
                      ("pairwise 2000x2000", t_pp, float("nan"), t_pv)]:
    bs = f"{b:>12.4f}" if b == b else f"{'--':>12}"
    worst = max(a, b) if b == b else a
    print(f"{name:<32}{a:>12.4f}{bs}{c:>12.5f}{worst / c:>12.0f}x")
print("same answer:", np.allclose(s_py, s_vec), np.allclose(s_npl, s_vec),
      np.allclose(d_py, d_vec), np.allclose(P_py, P_vec))

# emit the bar-chart data the chapter figure reads (figures/ch01/timing.dat)
import os
os.makedirs("figures/ch01", exist_ok=True)
with open("figures/ch01/timing.dat", "w") as f:
    f.write("op speedup\n")
    f.write(f"scores-loop {t_py / t_vec:.0f}\n")
    f.write(f"scores-nprow {t_npl / t_vec:.0f}\n")
    f.write(f"dist-loop {t_dp / t_dv:.0f}\n")
    f.write(f"pairwise-loop {t_pp / t_pv:.0f}\n")

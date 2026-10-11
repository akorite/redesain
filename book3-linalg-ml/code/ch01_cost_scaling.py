"""Cost of Gaussian elimination grows like n^3 (ch.1)."""
import time
import numpy as np

def eliminate(A, b):
    """Forward elimination in plain Python loops: ~ (1/3) n^3 row ops."""
    n = len(b)
    Ab = np.column_stack([A, b])
    for col in range(n - 1):
        for row in range(col + 1, n):
            Ab[row] -= (Ab[row, col] / Ab[col, col]) * Ab[col]
    return Ab

np.linalg.solve(np.eye(3), np.ones(3))          # why: warm up BLAS once
print(f"{'n':>5} {'ours (s)':>10} {'solve (s)':>10}")
for n in [50, 100, 200, 400]:
    rng = np.random.default_rng(0)
    A, b = rng.standard_normal((n, n)), rng.standard_normal(n)
    t0 = time.perf_counter(); eliminate(A, b)
    t1 = time.perf_counter(); np.linalg.solve(A, b)
    t2 = time.perf_counter()
    print(f"{n:>5} {t1 - t0:>10.4f} {t2 - t1:>10.4f}")

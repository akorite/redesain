"""Generate figures/ch01_cost.pdf: measured cost of elimination vs n."""
import time
import numpy as np
import matplotlib.pyplot as plt

def eliminate(A, b):
    n = len(b)
    Ab = np.column_stack([A, b])
    for col in range(n - 1):
        for row in range(col + 1, n):
            Ab[row] -= (Ab[row, col] / Ab[col, col]) * Ab[col]
    return Ab

def _time(fn):
    t0 = time.perf_counter(); fn(); return time.perf_counter() - t0

np.linalg.solve(np.eye(3), np.ones(3))
ns_ours = np.array([100, 200, 400, 800, 1600])
ns_solve = np.array([200, 400, 800, 1600, 3200])
t_ours, t_solve = [], []
for n in ns_ours:
    rng = np.random.default_rng(0)
    A, b = rng.standard_normal((n, n)), rng.standard_normal(n)
    t_ours.append(min(_time(lambda: eliminate(A, b)) for _ in range(3)))
for n in ns_solve:
    rng = np.random.default_rng(0)
    A, b = rng.standard_normal((n, n)), rng.standard_normal(n)
    t_solve.append(min(_time(lambda: np.linalg.solve(A, b)) for _ in range(5)))

slope_ours = np.polyfit(np.log2(ns_ours), np.log2(t_ours), 1)[0]
slope_solve = np.polyfit(np.log2(ns_solve[2:]), np.log2(t_solve[2:]), 1)[0]
print("measured slopes: ours %.2f, np.linalg.solve %.2f" % (slope_ours, slope_solve))

plt.figure(figsize=(4.6, 3.4))
plt.loglog(ns_ours, t_ours, "ko-", label="our loops")
plt.loglog(ns_solve, t_solve, "ks--", mfc="none", label="np.linalg.solve")
ref = t_ours[-1] * (ns_ours / ns_ours[-1]) ** 3
plt.loglog(ns_ours, ref, ":", color="0.45", label=r"$n^3$ guide")
plt.xlabel("system size $n$")
plt.ylabel("seconds")
plt.legend(frameon=False, loc="upper left")
plt.tight_layout()
plt.savefig("figures/ch01_cost.pdf")

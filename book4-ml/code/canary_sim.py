# canary_sim.py -- traffic-split canary: old vs new model on a shared
# stream, plus the statistics of when the split can call the delta.
import numpy as np

rng = np.random.default_rng(0)
N = 20000
# stream: y depends on x AND x2; old model only ever saw x.
x = rng.normal(0, 1, N); x2 = rng.normal(0, 1, N)
y = (x + 0.8 * x2 + rng.normal(0, 0.8, N) > 0).astype(int)

def acc(mask, pred):  return float((pred[mask] == y[mask]).mean())

old_pred = (x > 0.).astype(int)                       # incumbent rule
new_pred = (x + 0.8 * x2 > 0.).astype(int)            # learned on both
acc_old_all = acc(np.ones(N, bool), old_pred)
acc_new_all = acc(np.ones(N, bool), new_pred)
print(f"full-stream acc: old {acc_old_all:.4f}  new {acc_new_all:.4f}  "
      f"(delta {acc_new_all - acc_old_all:+.4f})")

# canary: new model scores a growing slice; measure both on it
for frac in (0.01, 0.05, 0.1, 0.5):
    n = int(N * frac)
    m = np.zeros(N, bool); m[:n] = True
    a_o, a_n = acc(m, old_pred), acc(m, new_pred)
    se = np.sqrt(a_o * (1 - a_o) / n + a_n * (1 - a_n) / n)
    d = a_n - a_o
    sig = "|d| > 2*SE -> call it" if abs(d) > 2 * se else "inside noise"
    print(f"canary {frac:4.0%} (n={n:5d}): old {a_o:.4f} new {a_n:.4f}  "
          f"d {d:+.4f}  2SE {2*se:.4f}  {sig}")

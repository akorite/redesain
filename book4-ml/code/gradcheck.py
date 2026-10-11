# code/ch07/gradcheck.py -- finite differences verify backprop,
# then catch a deliberately planted bias bug.
# Run from the repository root:  python3 code/ch07/gradcheck.py
import numpy as np

rng = np.random.default_rng(0)
d, h, C, n = 5, 4, 3, 7
X = rng.normal(size=(n, d))
y = rng.integers(0, C, n)
W1 = rng.normal(0, 0.5, (d, h)); b1 = np.zeros(h)
W2 = rng.normal(0, 0.5, (h, C)); b2 = np.zeros(C)

def loss_of(W1, b1, W2, b2):
    a1 = np.maximum(0, X @ W1 + b1)
    z = a1 @ W2 + b2
    z = z - z.max(1, keepdims=True)
    e = np.exp(z); p = e / e.sum(1, keepdims=True)
    return -np.log(p[np.arange(n), y]).mean()

def analytic():
    a1 = np.maximum(0, X @ W1 + b1)
    z = a1 @ W2 + b2
    z = z - z.max(1, keepdims=True)
    e = np.exp(z); p = e / e.sum(1, keepdims=True)
    dz = p.copy(); dz[np.arange(n), y] -= 1; dz /= n
    dW2 = a1.T @ dz
    da1 = dz @ W2.T
    dz1 = da1 * (X @ W1 + b1 > 0)
    return X.T @ dz1, dz1.sum(0), dW2

def numeric(param_idx, i, j=None):
    eps = 1e-6
    P = [W1, b1, W2][param_idx]
    orig = P[i] if j is None else P[i, j]
    if j is None: P[i] = orig + eps
    else:         P[i, j] = orig + eps
    hi = loss_of(W1, b1, W2, b2)
    if j is None: P[i] = orig - eps
    else:         P[i, j] = orig - eps
    lo = loss_of(W1, b1, W2, b2)
    if j is None: P[i] = orig
    else:         P[i, j] = orig
    return (hi - lo) / (2 * eps)

dW1, db1, dW2 = analytic()
print("check five entries of dW1 (analytic vs numeric):")
for i in [0, 2, 4]:
    for j in [0, 3]:
        an, nu = dW1[i, j], numeric(0, i, j)
        print(f"  W1[{i},{j}]: {an:+.6f} vs {nu:+.6f}   "
              f"diff {abs(an-nu):.1e}")
print("check two entries of db1:")
for i in [0, 3]:
    an, nu = db1[i], numeric(1, i)
    print(f"  b1[{i}]: {an:+.6f} vs {nu:+.6f}   diff {abs(an-nu):.1e}")

# --- the planted bug: forget one bias row in the sum --------------------
print("\nnow break it: drop row 0 of db1 on purpose")
db1_bug = db1.copy(); db1_bug[0] = 0
an, nu = db1_bug[0], numeric(1, 0)
print(f"  buggy b1[0]: {an:+.6f} vs numeric {nu:+.6f}   "
      f"diff {abs(an-nu):.1e}  <-- gradcheck catches it instantly")

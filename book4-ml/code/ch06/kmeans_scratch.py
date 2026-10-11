# code/ch06/kmeans_scratch.py -- Lloyd's algorithm + k-means++ init.
# Run from the repository root:  python3 code/ch06/kmeans_scratch.py
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
rng = np.random.default_rng(7)

def kmeanspp(X, k, rng):
    C = [X[rng.integers(len(X))]]
    for _ in range(k - 1):
        d = np.min(((X[:, None, :] - np.array(C)[None]) ** 2).sum(-1), axis=1)
        C.append(X[rng.choice(len(X), p=d / d.sum())])
    return np.array(C)

def lloyd(X, k, rng, steps=50):
    C = kmeanspp(X, k, rng)
    for it in range(steps):
        d = ((X[:, None, :] - C[None]) ** 2).sum(-1)
        z = d.argmin(1)
        newC = np.array([X[z == j].mean(0) if (z == j).any() else C[j]
                         for j in range(k)])
        if np.allclose(newC, C):
            break
        C = newC
    return z, C, it + 1, ((X - C[z]) ** 2).sum()

for k in [2, 3]:
    z, C, its, inertia = lloyd(X, k, rng)
    # purity: best label per cluster
    pur = sum(max(np.bincount(y[z == j], minlength=3))
              for j in range(k)) / len(y)
    print(f"k={k}: inertia {inertia:8.1f}  purity-vs-species {pur:.3f}  "
          f"converged in {its} iters")

print("\ninit sensitivity at k=3 (10 seeds):")
for s in range(10):
    z, C, its, inertia = lloyd(X, 3, np.random.default_rng(s))
    print(f"  seed {s}: inertia {inertia:8.1f}")

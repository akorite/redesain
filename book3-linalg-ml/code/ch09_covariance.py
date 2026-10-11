import numpy as np
np.set_printoptions(precision=4, suppress=True)

# correlated 2-D data: x1 height-ish, x2 = 0.8 x1 + noise
rng = np.random.default_rng(4)
n = 400
x1 = rng.standard_normal(n)
x2 = 0.8 * x1 + 0.4 * rng.standard_normal(n)
X = np.column_stack([x1, x2])
X = X - X.mean(axis=0)
C = X.T @ X / (n - 1)
print("covariance C ="); print(C)
w, Q = np.linalg.eigh(C)
order = np.argsort(w)[::-1]
w, Q = w[order], Q[:, order]
print("eigenvalues:", w)
print("eigenvectors (cols):"); print(Q)
var_frac = w / w.sum()
print("variance fraction:", var_frac)
proj = X @ Q[:, 0]
print("reconstruction error keeping PC1:",
      np.mean((X - np.outer(proj, Q[:, 0]))**2))
print("PC1 direction angle (deg):", np.degrees(np.arctan2(Q[1,0], Q[0,0])))

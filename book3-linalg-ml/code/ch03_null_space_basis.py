import numpy as np
from scipy.linalg import null_space

A = np.array([[1., 2., 0., 3.],
              [2., 4., 1., 4.],
              [1., 2., 1., 1.]])

def rref(M, tol=1e-10):
    M = M.copy().astype(float)
    rows, cols = M.shape
    pivots = []
    r = 0
    for c in range(cols):
        if r >= rows:
            break
        k = np.argmax(np.abs(M[r:, c])) + r
        if abs(M[k, c]) < tol:
            continue
        M[[r, k]] = M[[k, r]]
        M[r] = M[r] / M[r, c]
        for i in range(rows):
            if i != r:
                M[i] -= M[i, c] * M[r]
        pivots.append(c)
        r += 1
    return M, pivots

R, pivots = rref(A)
print("RREF =")
print(R)
print("pivot columns:", pivots)

free = [c for c in range(A.shape[1]) if c not in pivots]
basis = []
for f in free:
    x = np.zeros(A.shape[1])
    x[f] = 1.0
    for row, p in enumerate(pivots):
        x[p] = -R[row, f]
    basis.append(x)
basis = np.array(basis).T
print("free columns:", free)
print("null-space basis (columns):")
print(basis)
print("A @ basis ~ 0:", np.allclose(A @ basis, 0))
print("scipy null_space:")
print(np.round(null_space(A), 6))

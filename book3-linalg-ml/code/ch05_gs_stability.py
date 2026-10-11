import numpy as np
np.set_printoptions(precision=2, suppress=True)
np.seterr(all="ignore")

def classical_gs(A):
    Q = np.zeros_like(A)
    for j in range(A.shape[1]):
        v = A[:, j].copy()
        for i in range(j):
            v -= (Q[:, i] @ A[:, j]) * Q[:, i]
        Q[:, j] = v / np.linalg.norm(v)
    return Q

def modified_gs(A):
    Q = np.zeros_like(A)
    V = A.copy()
    for j in range(A.shape[1]):
        Q[:, j] = V[:, j] / np.linalg.norm(V[:, j])
        for k in range(j + 1, A.shape[1]):
            V[:, k] -= (Q[:, j] @ V[:, k]) * Q[:, j]
    return Q

# nearly-dependent columns: the classical stress test
eps = 1e-8
A = np.array([[1., 1., 1.],
              [eps, 0., 0.],
              [0., eps, 0.],
              [0., 0., eps]])

Qc = classical_gs(A)
Qm = modified_gs(A)
print("classical  |Q^T Q - I| =", np.linalg.norm(Qc.T @ Qc - np.eye(3), ord=np.inf))
print(Qc.T @ Qc)
print("modified   |Q^T Q - I| =", np.linalg.norm(Qm.T @ Qm - np.eye(3), ord=np.inf))
print(Qm.T @ Qm)
Q_lib, _ = np.linalg.qr(A)
print("np.linalg.qr |Q^T Q - I| =",
      np.linalg.norm(Q_lib.T @ Q_lib - np.eye(3), ord=np.inf))

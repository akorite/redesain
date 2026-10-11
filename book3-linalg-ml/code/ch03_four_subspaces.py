import numpy as np
from scipy.linalg import null_space

A = np.array([[1., 2., 0., 3.],
              [2., 4., 1., 4.],
              [1., 2., 1., 1.]])
m, n = A.shape

r = np.linalg.matrix_rank(A)
C = A[:, [0, 2]]                    # pivot columns -> basis of col(A)
N = null_space(A)                   # basis of ker(A)
N_left = null_space(A.T)            # basis of ker(A^T) = left null space
R = null_space(A.T).T @ A           # cheap check is below instead

print("rank r =", r)
print("dim col(A)  =", C.shape[1], " (should be r)")
print("dim ker(A)  =", N.shape[1], " (should be n - r =", n - r, ")")
print("dim row(A)  =", r, " (should be r)")
print("dim ker(A^T)=", N_left.shape[1], " (should be m - r =", m - r, ")")
print("counts: r + (n-r) =", r + N.shape[1], "= n;",
      "r + (m-r) =", r + N_left.shape[1], "= m")
print("basis of col(A) (pivot columns of A):")
print(C)
print("basis of ker(A^T):")
print(np.round(N_left, 6))
print("sanity: N_left.T @ A ~ 0:", np.allclose(N_left.T @ A, 0))

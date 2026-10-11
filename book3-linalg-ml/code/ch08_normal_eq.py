import numpy as np
np.set_printoptions(precision=4, suppress=True)

A = np.array([[1., 1.], [1., 2.], [1., 3.], [1., 4.]])
b = np.array([2., 3., 3., 5.])
print("A ="); print(A); print("b =", b)

AtA = A.T @ A; Atb = A.T @ b
print("A^T A ="); print(AtA); print("A^T b =", Atb)
x = np.linalg.solve(AtA, Atb)
print("xhat (intercept, slope) =", x)
r = b - A @ x
print("residual r =", r)
print("A^T r =", A.T @ r, "(orthogonal to col(A): OK)")
print("RSS =", r @ r)

import numpy as np
np.set_printoptions(precision=4, suppress=True)

# plane spanned by columns of A; project b = (2, 1, 3, -1) onto it
A = np.array([[1., 0.],
              [0., 1.],
              [1., 1.],
              [1., -1.]])
b = np.array([2., 1., 3., -1.])

P = A @ np.linalg.inv(A.T @ A) @ A.T
p = P @ b
print("P =")
print(P)
print("p = P @ b =", p)
print("in col(A)?", np.allclose(p, A @ np.linalg.solve(A.T @ A, A.T @ b)))
print("residual b - p =", b - p)
print("residual perpendicular to col(A)?", np.allclose(A.T @ (b - p), 0))
print("P^2 = P:", np.allclose(P @ P, P))
print("P^T = P:", np.allclose(P.T, P))
print("||b||^2 = ||p||^2 + ||b-p||^2:",
      np.isclose(b @ b, p @ p + (b - p) @ (b - p)))

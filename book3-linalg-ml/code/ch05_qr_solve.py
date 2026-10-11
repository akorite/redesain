import numpy as np
np.set_printoptions(precision=4, suppress=True)

# QR of the chapter's 3x3 and solve Ax = b via Q^T b + back-substitution
A = np.array([[1., 1., 0.],
              [1., 0., 1.],
              [0., 1., 1.]])
b = np.array([3., 2., 1.])

Q, R = np.linalg.qr(A)
print("Q =")
print(Q)
print("R =")
print(R)
print("Q^T Q = I:", np.allclose(Q.T @ Q, np.eye(3)))
print("QR = A:", np.allclose(Q @ R, A))

y = Q.T @ b
x = np.linalg.solve(R, y)          # triangular -> back substitution
print("x via QR =", x)
print("np.linalg.solve =", np.linalg.solve(A, b))
print("residual:", np.linalg.norm(A @ x - b))

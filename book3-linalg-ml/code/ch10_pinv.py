import numpy as np
np.set_printoptions(precision=6, suppress=True)

# pseudoinverse = V Sigma^+ U^T, built by hand
A = np.array([[1., 1.], [1., 2.], [1., 3.], [1., 4.]])
b = np.array([2., 3., 3., 5.])
U, S, Vt = np.linalg.svd(A, full_matrices=False)
Splus = np.diag(1.0 / S)
Aplus_hand = Vt.T @ Splus @ U.T
Aplus_np = np.linalg.pinv(A)
print("A+ (hand):"); print(Aplus_hand)
print("A+ (np.linalg.pinv):"); print(Aplus_np)
print("agree:", np.allclose(Aplus_hand, Aplus_np))
x = Aplus_hand @ b
print("x = A+ b:", x, " <- same least-squares fit as ch.8")
print("A A+ A == A:", np.allclose(A @ Aplus_hand @ A, A))

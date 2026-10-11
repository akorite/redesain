import numpy as np
np.set_printoptions(precision=4, suppress=True)

A = np.array([[4., 4.], [-3., 3.]])
print("A ="); print(A)
AtA = A.T @ A
w, V = np.linalg.eigh(AtA)          # ascending order
order = np.argsort(w)[::-1]
w, V = w[order], V[:, order]
s = np.sqrt(w)
Sigma = np.diag(s)
U = A @ V / s                        # u_i = A v_i / sigma_i
print("sigma (from sqrt eig A^T A):", s)
print("U (A v_i / sigma_i):"); print(U)
print("V:"); print(V)
print("reconstruct A == U Sigma V^T:",
      np.allclose(U @ Sigma @ V.T, A))
Un, Sn, Vnt = np.linalg.svd(A)
print("np.linalg.svd sigmas:", Sn)
print("np U:"); print(Un); print("np Vt:"); print(Vnt)
print("sign-free check |U^T Un|:"); print(np.abs(U.T @ Un).round(4))

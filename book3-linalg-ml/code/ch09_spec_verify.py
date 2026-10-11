import numpy as np
np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(3)

M = rng.standard_normal((4, 4))
A = M + M.T          # symmetric by construction
print("A ="); print(A)
print("symmetric:", np.allclose(A, A.T))

w, Q = np.linalg.eigh(A)   # eig for symmetric matrices
print("eigenvalues:", w)
print("Q orthonormal (Q^T Q = I):", np.allclose(Q.T @ Q, np.eye(4)))
Lam = np.diag(w)
print("A == Q Lambda Q^T:", np.allclose(Q @ Lam @ Q.T, A))
print("A^3 == Q Lambda^3 Q^T:",
      np.allclose(Q @ np.diag(w**3) @ Q.T, A @ A @ A))
# non-symmetric contrast: same eigenvalues? no orthogonal basis
B = np.array([[0., -1.], [1., 0.]])
print("rotation eig:", np.linalg.eigvals(B), "(complex: not symmetric)")

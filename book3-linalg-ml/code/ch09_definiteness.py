import numpy as np
np.set_printoptions(precision=4, suppress=True)

def pivots(A):
    A = A.astype(float).copy(); n = A.shape[0]; ps = []
    for j in range(n):
        ps.append(A[j, j])
        if abs(A[j, j]) < 1e-12: break
        A[j+1:, j:] -= np.outer(A[j+1:, j] / A[j, j], A[j, j:])
    return np.array(ps)

mats = {
    "PD   [[2,-1,0],[-1,2,-1],[0,-1,2]]":
        np.array([[2., -1., 0.], [-1., 2., -1.], [0., -1., 2.]]),
    "PSD  [[1,1,1],[1,1,1],[1,1,1]]":
        np.ones((3, 3)),
    "IND  [[1,0],[0,-1]]":
        np.array([[1., 0.], [0., -1.]]),
    "PD?  [[1,2],[2,1]]":
        np.array([[1., 2.], [2., 1.]]),
}
for name, M in mats.items():
    w = np.linalg.eigvalsh(M)
    print(f"{name}: eigs {w}  pivots {pivots(M)}")

# A^T A is always PSD
rng = np.random.default_rng(0)
A = rng.standard_normal((5, 3))
G = A.T @ A
print("Gram G=A^T A eigenvalues:", np.linalg.eigvalsh(G))
x = rng.standard_normal(3)
print("x^T G x = ||Ax||^2 =", x @ G @ x, " = ||Ax||^2 check:",
      np.isclose(x @ G @ x, (A @ x) @ (A @ x)))

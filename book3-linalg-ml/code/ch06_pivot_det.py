import numpy as np
np.set_printoptions(precision=4, suppress=True)

def pivot_det(A):
    """det via elimination: product of pivots times (-1)^swaps."""
    A = A.astype(float).copy()
    n = A.shape[0]
    swaps = 0
    det = 1.0
    for j in range(n):
        piv = np.argmax(np.abs(A[j:, j])) + j
        if abs(A[piv, j]) < 1e-12:
            return 0.0
        if piv != j:
            A[[j, piv]] = A[[piv, j]]
            swaps += 1
        det *= A[j, j]
        A[j+1:, j:] -= np.outer(A[j+1:, j] / A[j, j], A[j, j:])
    return det * (-1.0) ** swaps

# 3x3 from the chapter: det = 8 by cofactors AND by pivots
A = np.array([[2., 1., 0.],
              [1., 3., 1.],
              [0., 1., 2.]])
print("matrix:")
print(A)
print("pivot_det =", pivot_det(A))
print("np.linalg.det =", np.linalg.det(A))

# swap-count check on a matrix needing a swap
B = np.array([[0., 2., 1.],
              [1., 0., 1.],
              [2., 1., 0.]])
print("swap-needed matrix pivot_det =", pivot_det(B),
      "np.linalg.det =", np.linalg.det(B))

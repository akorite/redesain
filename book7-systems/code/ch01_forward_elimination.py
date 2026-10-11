"""Forward elimination + back substitution on a 3x3 system (ch.1)."""
import numpy as np

A = np.array([[2., 1., 1.],
              [4., -6., 0.],
              [-2., 7., 2.]])
b = np.array([5., -2., 9.])
n = len(b)

Ab = np.column_stack([A, b])     # the augmented matrix [A | b]
for col in range(n - 1):         # eliminate below each pivot, left to right
    for row in range(col + 1, n):
        m = Ab[row, col] / Ab[col, col]   # why: this multiplier kills Ab[row, col]
        Ab[row] -= m * Ab[col]
print("echelon form [U | c]:")
print(Ab)

x = np.zeros(n)                  # back substitution reads U bottom to top
for row in range(n - 1, -1, -1):
    x[row] = (Ab[row, n] - Ab[row, row + 1:n] @ x[row + 1:n]) / Ab[row, row]
print("x =", x)
print("np.linalg.solve agrees:", np.linalg.solve(A, b))
print("residual ||Ax-b|| =", np.linalg.norm(A @ x - b))

"""Gauss-Jordan inverse on the worked-example matrix, vs np.linalg.inv."""
import numpy as np

A = np.array([[1., 2., 0.], [2., 5., 1.], [0., 1., 3.]])
n = A.shape[0]
AI = np.column_stack([A, np.eye(n)])

for col in range(n):
    # normalize pivot row, then zero the column everywhere else
    AI[col] = AI[col] / AI[col, col]
    for row in range(n):
        if row != col:
            AI[row] -= AI[row, col] * AI[col]

A_inv = AI[:, n:]
print("A_inv by Gauss-Jordan:")
print(A_inv)
print("np.linalg.inv agrees:", np.allclose(A_inv, np.linalg.inv(A)))
print("A @ A_inv:")
print(A @ A_inv)

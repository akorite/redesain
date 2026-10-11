"""A permutation matrix reorders dataset rows; P.T is its inverse."""
import numpy as np

# a tiny "dataset": each row tagged with its original index
X = np.array([[0., 10.], [1., 11.], [2., 12.], [3., 13.]])
sigma = [2, 0, 3, 1]              # new order of rows

n = len(sigma)
P = np.zeros((n, n))
P[np.arange(n), sigma] = 1        # row i of PX is row sigma[i] of X

print("P =\n", P)
print("P @ X =\n", P @ X)
print("X[sigma] =\n", X[sigma])
print("same thing:", np.allclose(P @ X, X[sigma]))
print("P.T @ P = I:", np.allclose(P.T @ P, np.eye(n)))
print("undo with P.T:", np.allclose(P.T @ (P @ X), X))

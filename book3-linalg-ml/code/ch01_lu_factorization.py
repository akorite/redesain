"""LU factorization with a row exchange, checked two ways (ch.1)."""
import numpy as np
from scipy.linalg import lu

A = np.array([[1., 1., 2.],
              [2., 2., 3.],
              [1., 0., 1.]])

# Hand result from the worked example: swap rows 2<->3 first (that order is P).
P = np.array([[1., 0., 0.],
              [0., 0., 1.],
              [0., 1., 0.]])
L = np.array([[1., 0., 0.],
              [1., 1., 0.],
              [2., 0., 1.]])
U = np.array([[1., 1., 2.],
              [0., -1., -1.],
              [0., 0., -1.]])
print("PA =\n", P @ A)
print("L @ U =\n", L @ U)
print("||PA - LU|| =", np.linalg.norm(P @ A - L @ U))

# scipy also returns PA = LU but with partial pivoting: it swaps rows 1<->2
# (largest pivot). A different, still correct, PA = LU.
P_sp, L_sp, U_sp = lu(A)
print("scipy P =\n", P_sp)
print("||P_sp A - L_sp U_sp|| =", np.linalg.norm(P_sp.T @ A - L_sp @ U_sp))

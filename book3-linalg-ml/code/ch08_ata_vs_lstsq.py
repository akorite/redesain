import numpy as np
np.set_printoptions(precision=6, suppress=True)

# x and x^2 over a window 1e-3 wide: the columns are nearly parallel
rng = np.random.default_rng(0)
n = 200
x = 1 + 0.001 * rng.random(n)
y = 2 - 3 * x + 0.5 * x**2            # exact quadratic data, no noise
A = np.column_stack([np.ones(n), x, x**2])
print("cond(A)      = %.3e" % np.linalg.cond(A))
print("cond(A^T A)  = %.3e   <- the square" % np.linalg.cond(A.T @ A))
x_ata = np.linalg.solve(A.T @ A, A.T @ y)
x_lstsq, res, rank, sv = np.linalg.lstsq(A, y, rcond=None)
print("x via A^T A solve   :", x_ata)
print("x via np.linalg.lstsq:", x_lstsq)
print("truth               : [ 2. -3.  0.5]")
print("err A^T A : %.3e" % np.linalg.norm(x_ata - np.array([2., -3., .5])))
print("err lstsq : %.3e" % np.linalg.norm(x_lstsq - np.array([2., -3., .5])))

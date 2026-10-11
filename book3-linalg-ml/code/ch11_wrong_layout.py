import numpy as np
np.set_printoptions(precision=4, suppress=True)

# f: R^2 -> R^3, Jacobian should be 3x2 (rows=outputs, cols=inputs)
def f(v):
    x, y = v
    return np.array([x*x + y, np.sin(x)*y, x - 2*y])

x0 = np.array([0.7, 1.2])
def jacobian_fd(f, x, h=1e-6):
    m = len(f(x)); n = len(x)
    J = np.zeros((m, n))
    for j in range(n):
        d = np.zeros(n); d[j] = h
        J[:, j] = (f(x + d) - f(x - d)) / (2*h)
    return J

J = jacobian_fd(f, x0)
print("correct Jacobian (3x2):"); print(J)
J_bad = jacobian_fd(f, x0).T   # the classic layout bug
v = np.array([1., 0.])
print("J @ v (right direction) :", J @ v)
try:
    print("J_bad @ v:", J_bad @ v)
except ValueError as e:
    print("J_bad @ v ->", e)
print("J_bad gives a 2x3: applying it to an input vector CRASHES")

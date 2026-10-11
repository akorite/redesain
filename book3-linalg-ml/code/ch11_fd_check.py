import numpy as np
np.set_printoptions(precision=6, suppress=True)

A = np.array([[2., 1.], [0., 3.], [1., -1.]])
b = np.array([1., 0., 2.])
x = np.array([0.4, -0.7])

def f(v):                        # f(x) = ||A x - b||^2
    r = A @ v - b
    return float(r @ r)

def g(v):                        # smooth non-polynomial: exp(v1)*sin(v2)
    return np.exp(v[0]) * np.sin(v[1])

def grad_g(v):
    return np.array([np.exp(v[0])*np.sin(v[1]), np.exp(v[0])*np.cos(v[1])])

def grad_fd(fun, v, h=1e-5):     # central difference
    gr = np.zeros_like(v)
    for i in range(len(v)):
        d = np.zeros_like(v); d[i] = h
        gr[i] = (fun(v + d) - fun(v - d)) / (2 * h)
    return gr

ga = 2 * A.T @ (A @ x - b)
print("--- quadratic f=||Ax-b||^2 (central FD exact to roundoff) ---")
for h in [1e-1, 1e-3, 1e-5, 1e-7, 1e-9]:
    err = np.linalg.norm(grad_fd(f, x, h) - ga)
    print(f"h={h:.0e}  fd={grad_fd(f,x,h)}  abs-err={err:.3e}")
print("analytic 2A^T(Ax-b):", ga)
print("--- non-polynomial g=exp(x1)sin(x2): the U-shape ---")
xg = np.array([0.4, -0.7]); gg = grad_g(xg)
for h in [1e-1, 1e-3, 1e-5, 1e-7, 1e-9]:
    err = np.linalg.norm(grad_fd(g, xg, h) - gg)
    print(f"h={h:.0e}  fd={grad_fd(g,xg,h)}  abs-err={err:.3e}")

import sympy as sp

a11, a12, a21, a22 = sp.symbols('a11 a12 a21 a22')
x1, x2, b1, b2 = sp.symbols('x1 x2 b1 b2')
A = sp.Matrix([[a11, a12], [a21, a22]])
x = sp.Matrix([x1, x2]); b = sp.Matrix([b1, b2])
r = A * x - b
f = (r.T * r)[0]
print("f = ||Ax-b||^2 ="); print(sp.expand(f))
g = sp.Matrix([sp.diff(f, x1), sp.diff(f, x2)])
print("df/dx1 =", sp.expand(g[0]))
print("df/dx2 =", sp.expand(g[1]))
print("== 2*A.T*(A*x - b)?",
      sp.simplify(g - 2*A.T*(A*x - b)) == sp.zeros(2, 1))
# and the quadratic form x^T A x -> (A + A^T) x
A2 = sp.Matrix([[2, 1], [1, 3]])
q = (x.T * A2 * x)[0]
gq = sp.Matrix([sp.diff(q, x1), sp.diff(q, x2)])
print("grad x^T A x =", gq.T, " == 2Ax for symmetric A:",
      gq == 2*A2*x)

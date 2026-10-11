import numpy as np

# gradient descent on f(x)=0.5 x^T A x - b^T x, A = [[3,1],[1,1]]
A = np.array([[3.,1.],[1.,1.]]); b = np.array([1.,2.])
f = lambda x: .5*x@A@x - b@x
grad = lambda x: A@x - b
xstar = np.linalg.solve(A, b)
print("exact solution (normal equations):", xstar)

def gd(x0, eta, k):
    x = np.array(x0, float); hist=[x.copy()]
    for _ in range(k): x = x - eta*grad(x); hist.append(x.copy())
    return np.array(hist)

lam = np.linalg.eigvalsh(A)
print("eig(A) =", lam, " -> divergence for eta >", round(2/lam[-1],3))

for eta in [0.01, 0.2, 0.49, 0.70]:
    h = gd([2.5, 2.5], eta, 25)
    fx = f(h[-1])
    tag = "converged" if abs(fx - f(xstar)) < 1e-6 else \
          ("diverged" if abs(fx)>1e3 else "still going")
    print("eta=%.2f: after 25 steps f=%.6g err=%.3g  %s"
          % (eta, fx, fx-f(xstar), tag))

# convergence rate on quadratic: r = max(|1-eta*lmin|,|1-eta*lmax|)
for eta in [0.2, 0.49]:
    r = max(abs(1-eta*lam[0]), abs(1-eta*lam[1]))
    print("eta=%.2f theoretical rate r=%.3f -> x%.3f/step" % (eta, r, r))

# Rosenbrock: GD from (-1,1) with small fixed eta
ros = lambda x: 100*(x[1]-x[0]**2)**2 + (1-x[0])**2
ros_g = lambda x: np.array([-400*x[0]*(x[1]-x[0]**2)-2*(1-x[0]),
                            200*(x[1]-x[0]**2)])
x = np.array([-1.,1.]); path=[x.copy()]
for i in range(20000):
    x = x - 0.001*ros_g(x); path.append(x.copy())
print("rosenbrock 20k steps eta=1e-3: x=(%.4f,%.4f) f=%.5f"
      % (x[0],x[1],ros(x)))

import numpy as np
np.set_printoptions(precision=3, suppress=True)

# f = x^2 - x y + y^2, grad = (2x - y, -x + 2y); min at origin
def grad(v):
    x, y = v
    return np.array([2*x - y, -x + 2*y])

print("gradient field samples (position -> grad):")
for v in [np.array([1.,0.]), np.array([0.,1.]), np.array([1.,1.]),
          np.array([-1.,0.]), np.array([0.,-1.]), np.array([2.,1.])]:
    print(" ", v, "->", grad(v))
print("level sets: x^2 - xy + y^2 = c are ellipses;")
print("grad is normal to the level set everywhere (e.g. at (1,1)):")
v = np.array([1., 1.])
t = np.array([np.cos(np.pi/3)*v[0]-np.sin(np.pi/3)*v[1],
              np.sin(np.pi/3)*v[0]+np.cos(np.pi/3)*v[1]])  # not needed
# tangent to level curve at v: f(v)=1, parametrize numerically
th = np.linspace(0, 2*np.pi, 2001)
# unit-circle-in-metric tangent direction: solve f(v + eps*d)=1
d = np.array([0.5*np.sqrt(3), 0.5])  # candidate tangent
# actual: tangent d satisfies grad . d = 0
g = grad(v)
d = np.array([-g[1], g[0]])
print("  grad(1,1)=", g, " tangent dir=", d/np.linalg.norm(d),
      " dot=", np.dot(g, d/np.linalg.norm(d)))

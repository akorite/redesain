import numpy as np
np.set_printoptions(precision=4, suppress=True)
np.random.seed(7)

# does |det A| scale the volume of any set? test with a random 2x2 and 3x3
# and a point cloud: compare areas of the unit square before/after.
def poly_area(P):
    # 2D polygon area via shoelace
    x, y = P[:, 0], P[:, 1]
    return 0.5 * abs(np.sum(x * np.roll(y, -1) - y * np.roll(x, -1)))

A = np.array([[2., 1.], [1., 1.5]])
# unit square + a rotated-ish rectangle + a triangle
shapes = {
    "unit square": np.array([[0, 0], [1, 0], [1, 1], [0, 1.]]),
    "rectangle": np.array([[0, 0], [2, 0], [2, 0.5], [0, 0.5]]),
    "triangle": np.array([[0, 0], [1, 0], [0.5, 1.2]]),
}
print("A =")
print(A)
print("|det A| =", abs(np.linalg.det(A)))
for name, S in shapes.items():
    before = poly_area(S)
    after = poly_area(S @ A.T)
    print(f"{name:12s} area {before:.4f} -> {after:.4f}  "
          f"ratio {after/before:.4f}")

# 3D: volume of a random tetrahedron scales the same way
B = np.random.randn(3, 3)
M = np.array([[1., 0., 1.], [2., 1., 0.], [0., 1., 1.]])
det_tet = abs(np.linalg.det(np.c_[M[1]-M[0], M[2]-M[0], M[3]-M[0]])) if False else None
# volume of parallelepiped = |det| of edge matrix
E = np.array([[1., 0.5, 0.], [0., 1., 0.5], [0.5, 0., 1.]])
v0 = abs(np.linalg.det(E))
v1 = abs(np.linalg.det(B @ E))
print("3D parallelepiped: |det E| =", v0,
      " |det(B E)| =", v1, " ratio =", v1 / v0,
      " |det B| =", abs(np.linalg.det(B)))

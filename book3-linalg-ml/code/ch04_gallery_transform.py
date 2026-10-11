import numpy as np
np.set_printoptions(precision=3, suppress=True)

# the catalog maps as matrices
theta = np.pi / 6
rot = np.array([[np.cos(theta), -np.sin(theta)],
                [np.sin(theta),  np.cos(theta)]])
refl = np.array([[1., 0.], [0., -1.]])          # reflect across x-axis
shear = np.array([[1., 0.5], [0., 1.]])          # shear in x
proj = np.array([[1., 0.], [0., 0.]])            # project onto x-axis

# point cloud: the unit square + the letter F's bounding corners
pts = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.],
                [0.25, 0.75], [0.75, 0.75]])

for name, M in [("rotation", rot), ("reflection", refl),
                ("shear", shear), ("projection", proj)]:
    print(f"{name:>12} det={np.linalg.det(M):+.3f}")
    print(np.round(pts @ M.T, 2))
print("rotation preserves lengths:",
      np.allclose(np.linalg.norm(pts, axis=1),
                  np.linalg.norm(pts @ rot.T, axis=1)))
print("projection is idempotent:", np.allclose(proj @ proj, proj))

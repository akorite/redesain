import numpy as np
np.set_printoptions(precision=6, suppress=True)

# det small != singular; det==0 is the only collapse.
A = np.array([[1., 0.], [0., 1.]])          # det = 1
B = np.array([[100., 0.], [0., 0.001]])     # det = 0.1 -- small!
C = np.array([[1., 1.], [1., 1.0001]])      # det = 1e-4 -- nearly singular
D = np.array([[1., 1.], [1., 1.]])          # det = 0 -- singular
for name, M in [("I", A), ("diag(100,0.001)", B),
                ("near-dep", C), ("dup-rows", D)]:
    d = np.linalg.det(M)
    c = np.linalg.cond(M)
    inv_ok = "yes"
    try:
        _ = np.linalg.inv(M)
    except np.linalg.LinAlgError:
        inv_ok = "NO"
    print(f"{name:16s} det={d:12.6f}  cond={c:12.4f}  invertible={inv_ok}")

# normalized check: scale B down so columns are unit-ish
B2 = B / np.abs(B).max()
print("rescaled diag(1, 1e-5): det =", np.linalg.det(B2),
      " cond =", np.linalg.cond(B2))

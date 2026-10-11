import numpy as np

np.seterr(all="ignore")
rng = np.random.default_rng(7)

def to_basis(A, B):
    return np.linalg.inv(B) @ A @ B

ok_tr, ok_det = 0, 0
for _ in range(100):
    A = rng.standard_normal((2, 2))
    B = rng.standard_normal((2, 2))
    while abs(np.linalg.det(B)) < 0.1:
        B = rng.standard_normal((2, 2))
    TB = to_basis(A, B)
    ok_tr += np.isclose(np.trace(TB), np.trace(A))
    ok_det += np.isclose(np.linalg.det(TB), np.linalg.det(A))
print(f"tr preserved:  {ok_tr}/100")
print(f"det preserved: {ok_det}/100")

# code/ch04/linreg_scratch.py -- OLS via normal equations + ridge closed form.
# Run from the repository root:  python3 code/ch04/linreg_scratch.py
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

X, y = load_diabetes(return_X_y=True)   # already centred+scaled by sklearn
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=7)
n, d = Xtr.shape
Xb = np.c_[Xtr, np.ones(n)]             # intercept column
Xte_b = np.c_[Xte, np.ones(len(Xte))]

# --- OLS: theta = (X^T X)^{-1} X^T y  --------------------------------
theta = np.linalg.solve(Xb.T @ Xb, Xb.T @ ytr)
pred = Xte_b @ theta
mse = ((pred - yte) ** 2).mean()
r2 = 1 - ((pred - yte) ** 2).sum() / ((yte - yte.mean()) ** 2).sum()
print(f"OLS: test MSE {mse:.1f}  R2 {r2:.3f}")
print("coefs:", np.round(theta[:-1], 2))

# --- ridge: theta = (X^T X + lam I)^{-1} X^T y  (no penalty on bias) --
print(f"\n{'lambda':>9} {'test MSE':>9} {'||theta||':>10}")
for lam in [0, 0.01, 0.1, 1, 10, 100, 1000]:
    I = np.eye(d + 1); I[-1, -1] = 0
    th = np.linalg.solve(Xb.T @ Xb + lam * I, Xb.T @ ytr)
    p = Xte_b @ th
    print(f"{lam:>9.2f} {((p - yte)**2).mean():>9.1f} "
          f"{np.linalg.norm(th[:-1]):>10.2f}")

# --- the singular rescue ------------------------------------------------
print("\nSingular X^T X: duplicate a column and watch OLS blow up,")
X2 = np.c_[Xtr, Xtr[:, 3] * 2]         # col d = 2 * col 3 -> rank deficient
X2b = np.c_[X2, np.ones(n)]
try:
    th_bad = np.linalg.solve(X2b.T @ X2b, X2b.T @ ytr)
    print("  OLS ||theta|| on redundant design:", f"{np.linalg.norm(th_bad):.2e}")
except np.linalg.LinAlgError:
    print("  OLS failed outright (singular matrix)")
for lam in [1e-6, 1.0]:
    I = np.eye(d + 2); I[-1, -1] = 0
    th_ok = np.linalg.solve(X2b.T @ X2b + lam * I, X2b.T @ ytr)
    print(f"  ridge lam={lam}: ||theta|| {np.linalg.norm(th_ok):.3f}")

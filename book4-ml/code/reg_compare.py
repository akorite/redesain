# code/ch04/reg_compare.py -- scratch vs sklearn, ridge/lasso paths.
# Run from the repository root:  python3 code/ch04/reg_compare.py
import numpy as np
from sklearn.datasets import load_diabetes, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso, LinearRegression
from sklearn.preprocessing import StandardScaler

X, y = load_diabetes(return_X_y=True)
names = load_diabetes().feature_names
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=7)

print("=== diabetes: OLS vs Ridge(1.0) vs Lasso(0.05) coefs ===")
ols = LinearRegression().fit(Xtr, ytr)
rdg = Ridge(alpha=1.0).fit(Xtr, ytr)
las = Lasso(alpha=0.05).fit(Xtr, ytr)
print(f"{'feature':>7} {'OLS':>8} {'Ridge':>8} {'Lasso':>8}")
for i, nm in enumerate(names):
    print(f"{nm:>7} {ols.coef_[i]:>8.2f} {rdg.coef_[i]:>8.2f} "
          f"{las.coef_[i]:>8.2f}")
print(f"test R2: OLS {ols.score(Xte, yte):.3f}  "
      f"Ridge {rdg.score(Xte, yte):.3f}  Lasso {las.score(Xte, yte):.3f}")

print("\n=== california: which features die first under lasso? ===")
Xc, yc = fetch_california_housing(return_X_y=True)
cn = fetch_california_housing().feature_names
Xc = StandardScaler().fit_transform(Xc)
for a in [0.001, 0.01, 0.1]:
    m = Lasso(alpha=a, max_iter=5000).fit(Xc, yc)
    alive = [f"{nm}={c:.2f}" for nm, c in zip(cn, m.coef_) if abs(c) > 1e-6]
    print(f"alpha={a}: kept {len(alive)}/8 -> {alive}")

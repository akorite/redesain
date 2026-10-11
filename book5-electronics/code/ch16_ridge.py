import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)
import numpy as np
from mlscratch import Ridge, LinearRegression

rng = np.random.default_rng(2)
n_tr, n_te, d = 12, 500, 10   # nearly determined: OLS overfits
Xtr = rng.normal(0, 1, (n_tr, d))
Xte = rng.normal(0, 1, (n_te, d))
w_true = np.array([3., -2., 1.5, 0., 0., 0.5, 0., 0., 0., 0.])
sig = 3.0
ytr = Xtr @ w_true + sig * rng.normal(0, 1, n_tr)
yte = Xte @ w_true + sig * rng.normal(0, 1, n_te)

ols = LinearRegression().fit(Xtr, ytr)
tr = ((ols.predict(Xtr) - ytr) ** 2).mean()
te = ((ols.predict(Xte) - yte) ** 2).mean()
print(f"OLS   : |w|_1={np.abs(ols.w_[1:]).sum():6.2f}  "
      f"train MSE={tr:7.3f}  test MSE={te:7.3f}")
for lam in [0.01, 0.1, 0.5, 1.0, 3.0, 10.0, 100.0]:
    r = Ridge(lam=lam).fit(Xtr, ytr)
    tr = ((r.predict(Xtr) - ytr) ** 2).mean()
    te = ((r.predict(Xte) - yte) ** 2).mean()
    print(f"lam={lam:6.2f}: |w|_1={np.abs(r.w_).sum():6.2f}  "
          f"train MSE={tr:7.3f}  test MSE={te:7.3f}")

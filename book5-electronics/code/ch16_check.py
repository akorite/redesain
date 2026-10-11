import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)  # macOS BLAS spurious warns
import numpy as np
from mlscratch import LinearRegression, Ridge, GaussianNB, PCA

rng = np.random.default_rng(1)
X = rng.normal(0, 1, (40, 5))
w_true = np.array([2.0, -1.0, 0.5, 0.0, 1.5])
y = X @ w_true + 1.0 + 0.1 * rng.normal(0, 1, 40)

# check 1: ridge -> OLS as lam -> 0
ols = LinearRegression().fit(X, y)
r0 = Ridge(lam=1e-8).fit(X, y)
print(f"|ridge(lam->0).w - OLS.w|_max = "
      f"{np.abs(r0.w_ - ols.w_[1:]).max():.2e}")

# check 2: PCA inverse_transform ~ reconstruction on train data
pca = PCA(2).fit(X)
Xr = pca.inverse_transform(pca.transform(X))
rec = np.abs(Xr - X).max()
print(f"PCA k=2 max recon err = {rec:.3f} "
      f"(data var {X.var():.3f} -> kept "
      f"{pca.variance_ratio_.sum():.3f})")

# check 3: FD check of the ridge normal equations residual
lam = 0.7
d = X.shape[1]
w = rng.normal(0, 1, d)
def J(v):
    return ((X @ v - y) ** 2).sum() + lam * (v ** 2).sum()
h = 1e-6
fd = (J(w + h * np.eye(d)[2]) - J(w - h * np.eye(d)[2])) / (2 * h)
an = 2 * (X.T @ X @ w - X.T @ y + lam * w)[2]
print(f"ridge grad FD={fd:.4f} analytic={an:.4f} relerr="
      f"{abs(fd-an)/abs(an):.2e}")

# check 4: GaussianNB agrees with a manual Bayes score
gnb = GaussianNB().fit(X, y > 0)
i = 0
manual = []
for c in gnb.classes_:
    m, v, pr = gnb.theta_[int(c)], gnb.var_[int(c)], gnb.prior_[int(c)]
    ll = -0.5 * (((X[i] - m) ** 2) / v).sum() \
        - 0.5 * np.log(2 * np.pi * v).sum() + np.log(pr)
    manual.append(ll)
print(f"GNB predict={gnb.predict(X[i:i+1])[0]:.0f}  "
      f"manual argmax={np.argmax(manual)}")

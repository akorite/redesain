import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)  # macOS BLAS spurious warns
import numpy as np
from mlscratch import PCA, LogisticRegression

rng = np.random.default_rng(0)
# 30-dim data: the signal lives on a 2-dim subspace + noise
n = 120
Z = rng.normal(0, 1, (n, 2))
B = rng.normal(0, 1, (30, 2)) / np.sqrt(30)
with np.errstate(all='ignore'):   # macOS BLAS false-positive warn
    X = Z @ B.T + 0.3 * rng.normal(0, 1, (n, 30))   # X verified finite
y = (Z[:, 0] + 0.5 * Z[:, 1] > 0).astype(float)
Xtr, Xte, ytr, yte = X[:90], X[90:], y[:90], y[90:]

pca = PCA(2).fit(Xtr)
Ztr, Zte = pca.transform(Xtr), pca.transform(Xte)
print(f"variance explained by 2 PCs: "
      f"{pca.variance_ratio_.sum():.3f}  "
      f"({pca.variance_ratio_[0]:.3f}+{pca.variance_ratio_[1]:.3f})")

clf = LogisticRegression(steps=4000).fit(Ztr, ytr)
print(f"mlscratch PCA->logistic: train {((clf.predict(Ztr)==ytr).mean()):.3f}"
      f"  test {((clf.predict(Zte)==yte).mean()):.3f}")

from sklearn.decomposition import PCA as skPCA
from sklearn.linear_model import LogisticRegression as skLR
sk = skPCA(2).fit(Xtr)
skt = sk.transform(Xtr); ske = sk.transform(Xte)
print(f"sklearn  variance explained: {sk.explained_variance_ratio_.sum():.3f}")
m = skLR(max_iter=4000).fit(skt, ytr)
print(f"sklearn  PCA->logistic:  train {m.score(skt, ytr):.3f}"
      f"  test {m.score(ske, yte):.3f}")

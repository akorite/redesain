# code/ch06/pca_svd.py -- PCA via NumPy SVD on digits.
# Centre, decompose, project, reconstruct -- and count variance kept.
# Run from the repository root:  python3 code/ch06/pca_svd.py
import numpy as np
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
mu = X.mean(0)
Xc = X - mu
U, S, Vt = np.linalg.svd(Xc, full_matrices=False)

var = S ** 2 / (len(Xc) - 1)                    # per-component variance
share = var / var.sum()
cum = np.cumsum(share)
print("components to reach:")
for t in [0.5, 0.8, 0.9, 0.95, 0.99]:
    print(f"  {t:.0%} of variance: {int(np.searchsorted(cum, t)) + 1:>2} of 64")

# reconstruct digit 0 (an '8' at index 179) from top-k components
i = 179
for k in [10, 30, 60]:
    approx = mu + (Xc[i] @ Vt[:k].T) @ Vt[:k]
    err = ((X[i] - approx) ** 2).sum() / (X[i] ** 2).sum()
    print(f"k={k}: squared-error share {err:.3f}")
print("\n(each extra component is the SVD's next singular vector --")
print(" no gradients, no k-means, just linear algebra you already have.)")

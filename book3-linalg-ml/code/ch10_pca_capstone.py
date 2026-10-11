import numpy as np
from sklearn.decomposition import PCA
np.set_printoptions(precision=4, suppress=True)

class PCA_scratch:
    """centering -> SVD -> projection. This is all PCA is."""
    def fit(self, X):
        self.mean_ = X.mean(axis=0)
        U, S, Vt = np.linalg.svd(X - self.mean_, full_matrices=False)
        self.components_ = Vt
        self.singular_values_ = S
        n = X.shape[0]
        self.explained_variance_ratio_ = S**2 / (n - 1)
        self.explained_variance_ratio_ /= self.explained_variance_ratio_.sum()
        return self
    def transform(self, X):
        return (X - self.mean_) @ self.components_.T

rng = np.random.default_rng(7)
n = 500
t = rng.standard_normal(n)
X = np.column_stack([3*t + 0.2*rng.standard_normal(n),
                     t - 0.4*rng.standard_normal(n),
                     0.1*rng.standard_normal(n)])
ours = PCA_scratch().fit(X)
ref = PCA().fit(X)
print("explained-variance ratio ours  :", ours.explained_variance_ratio_)
print("explained-variance ratio sklearn:", ref.explained_variance_ratio_)
print("components agree up to sign:",
      np.allclose(np.abs(ours.components_), np.abs(ref.components_)))
Z = ours.transform(X)
print("transformed shape:", Z.shape, " col means:", Z.mean(axis=0))
print("first two components carry %.1f%% of variance"
      % (100 * ours.explained_variance_ratio_[:2].sum()))

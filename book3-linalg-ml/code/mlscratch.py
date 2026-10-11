# mlscratch.py -- the book's from-scratch ML library. numpy only.
# Consolidates: ch8 normal equations, ch10 PCA, ch13 Bayes/logistic,
# ch14 gradient descent. Interface: fit/predict (+transform for PCA).

import numpy as np


class LinearRegression:
    """ch8: normal equations. w_ = (X^T X)^-1 X^T y w/ intercept col."""
    def fit(self, X, y):
        A = np.c_[np.ones(len(X)), X]
        self.w_ = np.linalg.solve(A.T @ A, A.T @ y)
        return self

    def predict(self, X):
        return np.c_[np.ones(len(X)), X] @ self.w_


class Ridge:
    """Hand-derivation result: (X^T X + lam I) w = X^T y.
    Intercept NOT penalized (augmented matrix leaves it out)."""
    def __init__(self, lam=1.0):
        self.lam = lam

    def fit(self, X, y):
        d = X.shape[1]
        xm, ym = X.mean(0), y.mean()          # intercept un-penalized
        A = np.vstack([X - xm, np.sqrt(self.lam) * np.eye(d)])
        b = np.concatenate([y - ym, np.zeros(d)])
        self.w_ = np.linalg.solve(A.T @ A, A.T @ b)
        self.b_ = ym - xm @ self.w_
        return self

    def predict(self, X):
        return X @ self.w_ + self.b_


class LogisticRegression:
    """ch13/14: full-batch GD on stable NLL log(1+e^z) - y*z."""
    def __init__(self, eta=0.5, steps=4000):
        self.eta, self.steps = eta, steps

    def fit(self, X, y):
        n = len(X)
        self.w_ = np.zeros(X.shape[1]); self.b_ = 0.0
        for _ in range(self.steps):
            z = X @ self.w_ + self.b_
            p = 1 / (1 + np.exp(-np.clip(z, -30, 30)))
            self.w_ -= self.eta * X.T @ (p - y) / n
            self.b_ -= self.eta * (p - y).mean()
        return self

    def predict_proba(self, X):
        z = np.clip(X @ self.w_ + self.b_, -30, 30)
        return 1 / (1 + np.exp(-z))

    def predict(self, X):
        return (self.predict_proba(X) > 0.5).astype(float)


class GaussianNB:
    """ch13: Gaussian naive Bayes via per-class MLE."""
    def fit(self, X, y):
        self.classes_ = np.unique(y)
        self.theta_, self.var_, self.prior_ = [], [], []
        for c in self.classes_:
            Xc = X[y == c]
            self.theta_.append(Xc.mean(0))
            self.var_.append(Xc.var(0) + 1e-9)
            self.prior_.append(len(Xc) / len(X))
        return self

    def _jll(self, X):          # joint log-likelihood per class
        out = []
        for m, v, pr in zip(self.theta_, self.var_, self.prior_):
            ll = -0.5 * (((X - m) ** 2) / v).sum(1)
            ll -= 0.5 * np.log(2 * np.pi * v).sum()
            out.append(ll + np.log(pr))
        return np.array(out).T

    def predict(self, X):
        return self.classes_[self._jll(X).argmax(1)]


class PCA:
    """ch10: eigendecomposition of the covariance. fit learns the
    basis; transform projects; variance_ratio_ = explained share."""
    def __init__(self, k):
        self.k = k

    def fit(self, X):
        self.mean_ = X.mean(0)
        C = np.cov((X - self.mean_).T)
        w, V = np.linalg.eigh(C)
        idx = w.argsort()[::-1][:self.k]
        self.components_ = V[:, idx]
        self.variance_ratio_ = w[idx] / w.sum()
        return self

    def transform(self, X):
        return (X - self.mean_) @ self.components_

    def inverse_transform(self, Z):
        return Z @ self.components_.T + self.mean_

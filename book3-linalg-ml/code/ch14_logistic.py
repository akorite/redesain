import numpy as np
from sklearn.linear_model import LogisticRegression

rng = np.random.default_rng(7)
n = 60
X = rng.normal(0, 1.2, (n, 2))
true = np.array([1.5, -1.0]); tb = 0.3
y = (X@true + tb + rng.normal(0, 0.9, n) > 0).astype(float)

def sigmoid(z): return 1/(1+np.exp(-z))

# CAPSTONE mlscratch.LogisticRegression: full-batch GD on the ch13 NLL
class mlscratch:
    class LogisticRegression:
        def __init__(self, eta=0.5, iters=3000):
            self.eta, self.iters = eta, iters
        def fit(self, X, y):
            self.w = np.zeros(X.shape[1]); self.b = 0.0
            for _ in range(self.iters):
                p = sigmoid(X@self.w + self.b)
                self.w -= self.eta * X.T@(p-y)/len(y)
                self.b -= self.eta * (p-y).mean()
            return self
        def predict(self, X):
            return (sigmoid(X@self.w+self.b) > .5).astype(float)

mine = mlscratch.LogisticRegression().fit(X, y)
sk = LogisticRegression().fit(X, y)
acc_mine = (mine.predict(X) == y).mean()
acc_sk = sk.score(X, y)
print("mlscratch  w=%s b=%.3f  train acc %.3f"
      % (np.round(mine.w,3), mine.b, acc_mine))
print("sklearn    w=%s b=%.3f  train acc %.3f"
      % (np.round(sk.coef_[0],3), sk.intercept_[0], acc_sk))

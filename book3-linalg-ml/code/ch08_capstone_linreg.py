import numpy as np
from sklearn.linear_model import LinearRegression
np.set_printoptions(precision=4, suppress=True)

# mlscratch: our own least-squares fitter, QR route from ch.5
class LinearRegression_scratch:
    def fit(self, A, y):
        A1 = np.column_stack([np.ones(len(A)), A])  # intercept column!
        Q, R = np.linalg.qr(A1)
        self.coef_ = np.linalg.solve(R, Q.T @ y)
        self.intercept_, self.slopes_ = self.coef_[0], self.coef_[1:]
        return self
    def predict(self, A):
        return self.intercept_ + A @ self.slopes_
    def r2(self, A, y):
        r = y - self.predict(A)
        return 1 - (r @ r) / ((y - y.mean()) @ (y - y.mean()))

# real-ish dataset: floor area, rooms, age -> apartment price
rng = np.random.default_rng(2)
n = 300
area = rng.uniform(30, 120, n)
rooms = rng.integers(1, 5, n).astype(float)
age = rng.uniform(0, 40, n)
price = 8 + 2.1 * area + 4 * rooms - 0.15 * age + 6 * rng.standard_normal(n)
X = np.column_stack([area, rooms, age])

ours = LinearRegression_scratch().fit(X, price)
ref = LinearRegression().fit(X, price)
print("ours   intercept %.4f  slopes %s" % (ours.intercept_, ours.slopes_))
print("sklearn intercept %.4f  slopes %s" % (ref.intercept_, ref.coef_))
print("max |coef diff| = %.2e" % np.abs(ours.coef_ - np.append(ref.intercept_, ref.coef_)).max())
print("R^2 ours   = %.4f" % ours.r2(X, price))
print("R^2 sklearn= %.4f" % ref.score(X, price))

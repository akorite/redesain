# code/ch03/knn_scratch.py -- k-NN from scratch on the real digits set.
# Run from the repository root:  python3 code/ch03/knn_scratch.py
import numpy as np
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
rng = np.random.default_rng(11)
perm = rng.permutation(len(y))
tr, te = perm[:1400], perm[1400:]          # 1400 train / 397 test

def knn_predict(Xtr, ytr, Xte, k):
    # squared euclidean via the (a-b)^2 = a^2 - 2ab + b^2 expansion
    d2 = (Xte**2).sum(1)[:, None] - 2 * Xte @ Xtr.T + (Xtr**2).sum(1)[None, :]
    nn = ytr[np.argsort(d2, axis=1)[:, :k]]
    # majority vote per row
    return np.array([np.bincount(row, minlength=10).argmax() for row in nn])

print(f"{'k':>4} {'train_acc':>10} {'test_acc':>10}")
for k in [1, 3, 5, 11, 25]:
    acc_tr = (knn_predict(X[tr], y[tr], X[tr], k) == y[tr]).mean()
    acc_te = (knn_predict(X[tr], y[tr], X[te], k) == y[te]).mean()
    print(f"{k:>4} {acc_tr:>10.3f} {acc_te:>10.3f}")

# code/ch04/logreg_scratch.py -- logistic regression by gradient descent
# on the two most separable breast_cancer features.
# Run from the repository root:  python3 code/ch04/logreg_scratch.py
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

X, y = load_breast_cancer(return_X_y=True)
X = X[:, [23, 2]]                        # worst radius + mean perimeter
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2,
                                    random_state=7, stratify=y)
mu, sd = Xtr.mean(0), Xtr.std(0)
Xtr, Xte = (Xtr - mu) / sd, (Xte - mu) / sd
n = len(Xtr)
Xb = np.c_[Xtr, np.ones(n)]
Xte_b = np.c_[Xte, np.ones(len(Xte))]

def nll(w):
    z = Xb @ w
    # -log sigma(z) for y=1, -log(1-sigma(z)) for y=0, stably:
    return (np.logaddexp(0, z) - ytr * z).sum()

w = np.zeros(3)
lr, steps = 0.5, 2000
for it in range(steps):
    z = Xb @ w
    p = 1 / (1 + np.exp(-z))
    grad = Xb.T @ (p - ytr) / n
    w -= lr * grad
    if it in [0, 9, 99, 499, 1999]:
        print(f"step {it:>5}: NLL {nll(w):.3f}")

pred = (1 / (1 + np.exp(-Xte_b @ w)) > 0.5).astype(int)
acc = (pred == yte).mean()
tp = int(((pred == 1) & (yte == 1)).sum())
fp = int(((pred == 1) & (yte == 0)).sum())
fn = int(((pred == 0) & (yte == 1)).sum())
print(f"\nw = {np.round(w, 3)}")
print(f"test acc {acc:.3f}   precision {tp/(tp+fp):.3f}   "
      f"recall {tp/(tp+fn):.3f}")

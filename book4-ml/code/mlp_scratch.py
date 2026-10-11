# code/ch07/mlp_scratch.py -- a 2-layer MLP in raw NumPy on digits.
# Forward, backprop (chain rule), softmax+CE loss, SGD loop. ~60 lines.
# Run from the repository root:  python3 code/ch07/mlp_scratch.py
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True)
X = X / 16.0
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25,
                                    random_state=7, stratify=y)
rng = np.random.default_rng(7)
d, h, C = 64, 48, 10
W1 = rng.normal(0, np.sqrt(2 / d), (d, h)); b1 = np.zeros(h)
W2 = rng.normal(0, np.sqrt(2 / h), (h, C)); b2 = np.zeros(C)

def relu(z):    return np.maximum(0, z)
def relu_(z):   return (z > 0).astype(float)
def softmax(z):
    z = z - z.max(1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(1, keepdims=True)

def fwd(Xb):
    z1 = Xb @ W1 + b1
    a1 = relu(z1)
    z2 = a1 @ W2 + b2
    p = softmax(z2)
    return z1, a1, z2, p

def loss(p, yb):
    return -np.log(p[np.arange(len(yb)), yb] + 1e-12).mean()

def bwd(Xb, yb, z1, a1, z2, p):
    m = len(Xb)
    dz2 = p.copy(); dz2[np.arange(m), yb] -= 1; dz2 /= m
    dW2 = a1.T @ dz2; db2 = dz2.sum(0)
    da1 = dz2 @ W2.T; dz1 = da1 * relu_(z1)
    dW1 = Xb.T @ dz1; db1 = dz1.sum(0)
    return dW1, db1, dW2, db2

lr, epochs = 0.5, 60
for ep in range(epochs + 1):
    z1, a1, z2, p = fwd(Xtr)
    if ep % 10 == 0:
        acc_tr = (p.argmax(1) == ytr).mean()
        acc_te = (fwd(Xte)[3].argmax(1) == yte).mean()
        print(f"epoch {ep:>3}: loss {loss(p, ytr):.3f}  "
              f"train acc {acc_tr:.3f}  test acc {acc_te:.3f}")
    if ep == epochs:
        break
    dW1, db1, dW2, db2 = bwd(Xtr, ytr, z1, a1, z2, p)
    for W, dW in [(W1, dW1), (b1, db1), (W2, dW2), (b2, db2)]:
        W -= lr * dW

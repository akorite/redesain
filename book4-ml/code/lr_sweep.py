# code/ch08/lr_sweep.py -- the lr dial as a table: too low, good, too high.
# SGD+momentum on the same digits MLP for 30 epochs each.
# Run from the repository root:  python3 code/ch08/lr_sweep.py
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from optim_scratch import init, loss_acc   # same machinery

X, y = load_digits(return_X_y=True); X = X / 16.0
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25,
                                    random_state=7, stratify=y)

def fwd(P, Xb):
    W1,b1,W2,b2 = P
    z1 = Xb@W1+b1; a1 = np.maximum(0,z1)
    z2 = a1@W2+b2; z2 -= z2.max(1,keepdims=True)
    e = np.exp(z2); return z1, a1, e/e.sum(1,keepdims=True)

def grads(P, Xb, yb):
    W1,b1,W2,b2 = P
    z1,a1,p = fwd(P, Xb); m = len(Xb)
    dz = p.copy(); dz[np.arange(m),yb] -= 1; dz /= m
    return [Xb.T@((dz@W2.T)*(z1>0)), ((dz@W2.T)*(z1>0)).sum(0),
            a1.T@dz, dz.sum(0)]

def run(lr, epochs=30, B=64, beta=0.9):
    P = init(); n = len(Xtr)
    mom = [np.zeros_like(w) for w in P]
    for ep in range(epochs):
        idx = np.random.default_rng(ep).permutation(n)
        for s in range(0, n, B):
            G = grads(P, Xtr[idx[s:s+B]], ytr[idx[s:s+B]])
            for i in range(4):
                mom[i] = beta*mom[i] - lr*G[i]; P[i] += mom[i]
        if ep in (0, 1, 2):
            l,_ = loss_acc(P, Xtr, ytr)
    l, a = loss_acc(P, Xte, yte)
    return l, a

print(f"{'lr':>8} {'final loss':>10} {'test acc':>9}  verdict")
for lr in [0.001, 0.005, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]:
    l, a = run(lr)
    v = 'diverged/stalls' if l > 2.0 else \
        ('too slow' if l > 0.8 else 'trains')
    print(f"{lr:>8} {l:>10.3f} {a:>9.3f}  {v}")

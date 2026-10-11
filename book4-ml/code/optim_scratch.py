# code/ch08/optim_scratch.py -- four optimisers, one shared training loop.
# Full-batch GD vs minibatch SGD vs SGD+momentum vs Adam on digits MLP.
# Run from the repository root:  python3 code/ch08/optim_scratch.py
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True); X = X / 16.0
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25,
                                    random_state=7, stratify=y)
d, h, C = 64, 48, 10

def init(seed=7):
    rng = np.random.default_rng(seed)
    return [rng.normal(0, np.sqrt(2/d), (d,h)), np.zeros(h),
            rng.normal(0, np.sqrt(2/h), (h,C)), np.zeros(C)]

def fwd(P, Xb):
    W1,b1,W2,b2 = P
    z1 = Xb@W1+b1; a1 = np.maximum(0,z1)
    z2 = a1@W2+b2; z2 -= z2.max(1,keepdims=True)
    e = np.exp(z2); return z1, a1, e/e.sum(1,keepdims=True)

def grads(P, Xb, yb):
    W1,b1,W2,b2 = P
    z1,a1,p = fwd(P, Xb); m = len(Xb)
    dz = p.copy(); dz[np.arange(m),yb] -= 1; dz /= m
    dW2 = a1.T@dz; db2 = dz.sum(0)
    dz1 = (dz@W2.T)*(z1>0)
    return [Xb.T@dz1, dz1.sum(0), dW2, db2]

def loss_acc(P, Xb, yb):
    p = fwd(P, Xb)[2]
    return (-np.log(p[np.arange(len(yb)),yb]+1e-12).mean(),
            (p.argmax(1)==yb).mean())

def run(mode, lr, epochs=60, B=64, beta=0.9):
    P = init()
    n = len(Xtr)
    mom = [np.zeros_like(w) for w in P]          # momentum buffer
    m2  = [np.zeros_like(w) for w in P]          # adam 2nd moment
    t = 0; trace = []
    for ep in range(epochs):
        idx = np.arange(n) if mode=='gd' else \
              np.random.default_rng(ep).permutation(n)
        for s in range(0, n, (n if mode=='gd' else B)):
            b = idx[s:s+(n if mode=='gd' else B)]
            G = grads(P, Xtr[b], ytr[b]); t += 1
            for i in range(4):
                if mode in ('sgd','gd'):
                    P[i] -= lr*G[i]
                elif mode=='mom':
                    mom[i] = beta*mom[i] - lr*G[i]; P[i] += mom[i]
                elif mode=='adam':
                    m2[i]  = .999*m2[i]+.001*G[i]**2
                    mom[i] = beta*mom[i]+(1-beta)*G[i]
                    mh = mom[i]/(1-beta**t); vh = m2[i]/(1-.999**t)
                    P[i] -= lr*mh/(np.sqrt(vh)+1e-8)
        trace.append(loss_acc(P, Xtr, ytr)[0])
    l, a = loss_acc(P, Xte, yte)
    return trace, a

if __name__ != '__main__':
    pass  # imported by lr_sweep.py for init/loss_acc only
else:
  for name, mode, lr in [("full-batch GD  lr=.5 ", 'gd',  .5),
                       ("SGD B=64      lr=.05", 'sgd', .05),
                       ("SGD+momentum  lr=.05", 'mom', .05),
                       ("Adam          lr=.01", 'adam',.01)]:
      tr, acc = run(mode, lr)
      print(f"{name}: loss {tr[0]:.2f}->{tr[-1]:.3f}"
            f"  (ep10 {tr[9]:.3f})  test acc {acc:.3f}")

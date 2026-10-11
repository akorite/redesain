import numpy as np

rng = np.random.default_rng(2)

# ---- ch11 finite-difference gradient checker, reused ----
def fd_check(f, g, x, h=1e-5):
    fd = np.zeros_like(x)
    for i in range(len(x)):
        xp = x.copy(); xp[i] += h
        xm = x.copy(); xm[i] -= h
        fd[i] = (f(xp) - f(xm)) / (2*h)
    return np.linalg.norm(fd - g(x))

# ---- two-layer net: d -> h -> 1, mse loss on a regression blob ----
d, h, n = 3, 4, 40
X = rng.normal(0, 1, (n, d))
yw = np.array([1., -1., .5])
y = X@yw + rng.normal(0, .1, n)

W1 = rng.normal(0, .2, (d, h)); b1 = np.zeros(h)
W2 = rng.normal(0, .2, (h, 1)); b2 = np.zeros(1)
theta = np.concatenate([W1.ravel(), b1, W2.ravel(), b2])

def unpack(t):
    i1, i2 = d*h, d*h+h
    return t[:i1].reshape(d,h), t[i1:i2], t[i2:i2+h].reshape(h,1), t[i2+h:]

def loss(t):
    W1, b1, W2, b2 = unpack(t)
    H = np.tanh(X@W1 + b1)
    return np.mean((H@W2 + b2 - y.reshape(-1,1))**2)

def grad(t):
    W1, b1, W2, b2 = unpack(t)
    H = np.tanh(X@W1 + b1)
    R = H@W2 + b2 - y.reshape(-1,1)         # residual n x 1
    dW2 = H.T@R * 2/n; db2 = R.mean(0)*2
    dH = R@W2.T * (1-H**2)                  # backprop through tanh
    dW1 = X.T@dH * 2/n; db1 = dH.mean(0)*2
    return np.concatenate([dW1.ravel(), db1, dW2.ravel(), db2])

print("FD gradient check max abs err:", fd_check(loss, grad, theta))

# train by GD on 32 rows, tracking train/val loss curve
Xtr, Xva, ytr, yva = X[:32], X[32:], y[:32], y[32:]
X, y = Xtr, ytr   # loss/grad now see the training split
def val_loss(t):
    W1, b1, W2, b2 = unpack(t)
    H = np.tanh(Xva@W1 + b1)
    return np.mean((H@W2 + b2 - yva.reshape(-1,1))**2)
tr, va = [], []
for i in range(20001):
    theta = theta - 0.2*grad(theta)
    if i % 5000 == 0: tr.append(loss(theta)); va.append(val_loss(theta))
print("train loss at iters 0..20000:", np.round(tr,4))
print("val   loss at iters 0..20000:", np.round(va,4))

# compare against sklearn MLPRegressor on same data
from sklearn.neural_network import MLPRegressor
mlp = MLPRegressor(hidden_layer_sizes=(4,), activation='tanh',
                   max_iter=4000, random_state=0).fit(X, y)
print("mlscratch train/val MSE %.4f/%.4f   sklearn MLP train/val %.4f/%.4f"
      % (loss(theta), val_loss(theta),
         np.mean((mlp.predict(Xtr)-ytr)**2),
         np.mean((mlp.predict(Xva)-yva)**2)))

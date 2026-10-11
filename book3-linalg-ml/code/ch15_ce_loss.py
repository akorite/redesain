import numpy as np

rng = np.random.default_rng(0)
n = 60
X = rng.normal(0, 1, (n, 2))
y = (X[:, 0] - 0.8 * X[:, 1] > 0.4).astype(float)

w = np.zeros(2); b = 0.0
eta = 0.5
for step in range(400):
    z = X @ w + b
    zc = np.clip(z, -30, 30)
    p = 1 / (1 + np.exp(-zc))
    loss = (np.logaddexp(0, z) - z * y).mean()
    gw = X.T @ (p - y) / n; gb = (p - y).mean()
    w -= eta * gw; b -= eta * gb
    if step % 80 == 0 or step == 399:
        acc = ((p > 0.5) == y).mean()
        print(f"step {step:3d}: CE loss = {loss:.4f}  acc = {acc:.3f}")

# confident-but-wrong penalty: true label 1, model says p=0.05
for q in [0.99, 0.7, 0.5, 0.05]:
    print(f"p={q}: CE = {-np.log2(q):.3f} bits")

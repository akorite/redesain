import numpy as np
np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(3)
# 1-D logistic regression data
x = rng.normal(0, 1, 40)
y = (x + rng.normal(0, 0.9, 40) > 0).astype(float)
def nll(w, b):
    z = w*x + b
    return np.sum(np.logaddexp(0, z) - y*z)   # stable NLL
# convexity check: NLL midpoint <= average (Jensen on 200 random pairs)
bad = 0
for _ in range(200):
    w1,b1 = rng.normal(0,3,2); w2,b2 = rng.normal(0,3,2)
    if nll((w1+w2)/2,(b1+b2)/2) > (nll(w1,b1)+nll(w2,b2))/2: bad += 1
print("convexity violations:", bad, "/200")
# numeric minimum by grid
W, B = np.meshgrid(np.linspace(-5,5,101), np.linspace(-5,5,101))
Z = np.zeros_like(W)
for i in range(W.shape[0]):
    for j in range(W.shape[1]): Z[i,j] = nll(W[i,j], B[i,j])
i,j = np.unravel_index(Z.argmin(), Z.shape)
print("grid minimum NLL %.3f at w=%.2f b=%.2f" % (Z[i,j], W[i,j], B[i,j]))

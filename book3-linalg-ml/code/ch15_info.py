import numpy as np

rng = np.random.default_rng(4)

def H(p):
    p = np.asarray(p, dtype=float)
    return -(p[p > 0] * np.log2(p[p > 0])).sum()

def kl(p, q):            # nats via ln? keep bits: log2 throughout
    p, q = np.asarray(p, float), np.asarray(q, float)
    m = p > 0
    return (p[m] * np.log2(p[m] / q[m])).sum()

def ce(p, q):
    q = np.asarray(q, float)
    return -(np.asarray(p, float) * np.log2(q)).sum()

coins = [0.5, 0.9, 0.99]
for p in coins:
    print(f"h({p}) = {H([p, 1-p]):.3f} bits")
print(f"h(die) = {H([1/6]*6):.3f} bits")

p = np.array([0.9, 0.09, 0.01])
q = np.array([0.4, 0.4, 0.2])
print(f"KL(p||q) = {kl(p, q):.4f}   KL(q||p) = {kl(q, p):.4f}")
print(f"H(p,q)   = {ce(p, q):.4f} = H(p) {H(p):.4f} + KL {kl(p, q):.4f}")

bad = 0
for _ in range(2000):
    a = rng.dirichlet(np.ones(3)); b = rng.dirichlet(np.ones(3))
    if kl(a, b) < -1e-12: bad += 1
print(f"Gibbs violations in 2000 random pairs: {bad}")

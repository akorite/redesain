# cartpole_linear.py -- linear-function-approximation Q-learning on a
# hand-rolled CartPole (classic physics, no gym dependency).
# state = (x, x_dot, theta, theta_dot); actions 0=left 1=right.
# The point of the listing: it *partially* learns then diverges -- the
# deadly triad made visible.
import numpy as np

rng = np.random.default_rng(0)

# --- classic cartpole dynamics (Euler, tau=0.02) --------------------
GRAV, MASSCART, MASSPOLE, LEN, FORCE, TAU = 9.8, 1.0, 0.1, 0.5, 10.0, 0.02
TOT = MASSCART + MASSPOLE
def dyn(s, a):
    x, xd, th, thd = s
    f = FORCE if a == 1 else -FORCE
    c, si = np.cos(th), np.sin(th)
    tmp = (f + MASSPOLE * LEN * thd**2 * si) / TOT
    thdd = (GRAV * si - c * tmp) / (LEN * (4/3 - MASSPOLE * c**2 / TOT))
    xdd = tmp - MASSPOLE * LEN * thdd * c / TOT
    return np.array([x + TAU * xd, xd + TAU * xdd,
                     th + TAU * thd, thd + TAU * thdd])

def episode(qw, eps, cap=500):
    s = rng.uniform(-0.05, 0.05, 4); hist = []
    for t in range(cap):
        feat = np.concatenate([s, s**2])              # 8 quadratic feats
        q = feat @ qw                                  # qw: (8,2)
        a = int(rng.random() < eps or np.argmax(q))
        ns = dyn(s, a)
        done = abs(ns[0]) > 2.4 or abs(ns[2]) > 0.2095
        r = 0.0 if done else 1.0
        nfeat = np.concatenate([ns, ns**2])
        target = r if done else r + 0.99 * float((nfeat @ qw).max())
        qw[:, a] += 0.01 * feat * (target - float(q @ np.eye(2)[a]))
        s = ns; hist.append(t)
        if done: return t + 1, True
    return cap, False

qw = np.zeros((8, 2))
lens = []
for ep in range(400):
    eps = max(0.05, 0.3 * (0.995 ** ep))
    n, done = episode(qw, eps)
    lens.append(n)
    if ep in (0, 49, 99, 199, 299, 399):
        print(f"ep {ep}: steps {n}  eps {eps:.2f}  "
          f"|w| {np.abs(qw).max():.2f}")

lens = np.array(lens)
print(f"mean steps eps 0-99: {lens[:100].mean():.0f}")
print(f"mean steps eps 100-199: {lens[100:200].mean():.0f}")
print(f"mean steps eps 200-299: {lens[200:300].mean():.0f}")
print(f"mean steps eps 300-399: {lens[300:].mean():.0f}")
print(f"|w| final: {np.abs(qw).max():.2f}  "
      f"(healthy run would stay ~O(1))")
np.save('/tmp/cartpole_lens.npy', lens)
print("saved /tmp/cartpole_lens.npy")

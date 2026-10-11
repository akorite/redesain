# sample_compare.py -- two generative baselines on `digits`:
# (a) pixel-independent Bernoulli: p(x_d) per pixel;
# (b) real autoregressive: p(x_d | x_{d-1}, position d) -- each pixel
#     conditioned on the previous one, the chain factorisation made
#     concrete on 8x8 digits.
import numpy as np
from sklearn.datasets import load_digits

d = load_digits()
X = (d.images.reshape(-1, 64) > 6).astype(float)   # binarised 8x8
Xtr, Xte = X[:1400], X[1400:]
rng = np.random.default_rng(0)

def nll_px(probs, X):
    p = np.clip(probs, 1e-9, 1 - 1e-9)
    return float(-(X * np.log(p) + (1 - X) * np.log(1 - p)).mean())

# (a) independent: p_i = mean pixel i
p_i = Xtr.mean(0)
indep = np.repeat(p_i[None], len(Xte), 0)

# (b) AR: estimate p(x_d=1 | x_{d-1}=v) per position d>=1 from train
cond = np.zeros((64, 2))                       # P(x_d=1 | prev = v)
for dpos in range(1, 64):
    for v in (0, 1):
        sel = Xtr[:, dpos - 1] == v
        cond[dpos, int(v)] = Xtr[sel, dpos].mean() if sel.any() else p_i[dpos]
cond[0] = p_i[0]
ar_p = np.zeros_like(Xte)
ar_p[:, 0] = p_i[0]
ar_p[:, 1:] = cond[1:, 0][None, :] * (1 - Xte[:, :-1]) \
    + cond[1:, 1][None, :] * Xte[:, :-1]

print(f"digits: {len(X)} imgs, {len(Xtr)} train / {len(Xte)} test, binarised")
print(f"NLL/pixel  independent : {nll_px(indep, Xte):.4f}")
print(f"NLL/pixel  AR(prev-px) : {nll_px(ar_p, Xte):.4f}  (context helps)")

# samples for the figure: independent by p_i; AR by ancestral sampling
def bern(p):
    return (rng.random(p.shape) < p).astype(float)
ar_s = np.zeros((24, 64)); ar_s[:, 0] = bern(np.full(24, p_i[0]))
for dpos in range(1, 64):
    pr = cond[dpos, ar_s[:, dpos - 1].astype(int)]
    ar_s[:, dpos] = bern(pr)
np.save('sample_real.npy', Xte[:24].reshape(-1, 8, 8))
np.save('sample_indep.npy', bern(np.repeat(p_i[None], 24, 0)).reshape(-1, 8, 8))
np.save('sample_ar.npy', ar_s.reshape(-1, 8, 8))
print("saved 24-sample grids (real / independent / AR-prev-pixel)")

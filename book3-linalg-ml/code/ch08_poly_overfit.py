import numpy as np
np.set_printoptions(precision=4, suppress=True)

rng = np.random.default_rng(1)
x = np.sort(rng.uniform(0, 1, 12))
y = np.sin(2 * np.pi * x) + 0.15 * rng.standard_normal(12)

def fit_eval(deg):
    A = np.vander(x, deg + 1, increasing=True)
    c, res, *_ = np.linalg.lstsq(A, y, rcond=None)
    rss_train = ((y - A @ c)**2).sum()
    xg = np.linspace(0, 1, 400)
    yg = np.sin(2 * np.pi * xg)
    rss_true = ((yg - np.vander(xg, deg + 1, increasing=True) @ c)**2).mean()
    return rss_train, rss_true

print("deg  train-RSS   true-RMS-error")
for d in [1, 3, 5, 11]:
    tr, te = fit_eval(d)
    print(f"{d:2d}   {tr:8.4f}   {te:9.4f}")

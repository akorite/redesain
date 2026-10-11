"""figdata.py -- emits pgfplots coordinate rows for the ch01 figures.

Run it whenever the figures' numbers should be refreshed; paste the
printed COORDS into figures/ch01-*.tex.
"""
import json
import urllib.request

import numpy as np

rng = np.random.default_rng(7)
T = 365
MU, SIGMA = 0.08, 0.60
dt = 1.0 / 365
eps = rng.standard_normal(T)
r_gbm = (MU - 0.5 * SIGMA**2) * dt + SIGMA * np.sqrt(dt) * eps
P = 100.0 * np.exp(np.cumsum(r_gbm))
P = np.concatenate([[100.0], P])
R = P[1:] / P[:-1] - 1.0

sel = list(range(0, len(P), 5))
print("FIG01_P " + " ".join(f"({i},{P[i]:.1f})" for i in sel))
sel2 = list(range(0, len(r_gbm), 5))
print("FIG01_R " + " ".join(f"({i},{r_gbm[i]*100:.2f})" for i in sel2))
diff_bp = (R - r_gbm) * 1e4
print("FIG02 " + " ".join(f"({i},{diff_bp[i]:.2f})" for i in sel2))

# ---- vol estimator curves (same construction as vol_estimators.py)
rng = np.random.default_rng(11)
TRUE_SIG = np.array([0.30] * 120 + [0.90] * 120)
close = [100.0]
high, low = [], []
for s in TRUE_SIG:
    c0 = close[-1]
    sd = s * np.sqrt(dt)
    up = c0 * np.exp(sd * abs(rng.standard_normal()))
    dn = c0 * np.exp(-sd * abs(rng.standard_normal()))
    c1 = c0 * np.exp(sd * rng.standard_normal())
    high.append(max(up, c1))
    low.append(min(dn, c1))
    close.append(c1)
c = np.array(close[1:])
h, l = np.array(high), np.array(low)
rv = np.diff(np.log(c))
est_cc = np.array([rv[i - 30:i].std(ddof=1)
                   for i in range(30, len(rv) + 1)]) * np.sqrt(365)
park = np.log(h / l) ** 2 / (4 * np.log(2))
est_pk = np.sqrt(np.array([park[i - 30:i].mean()
                           for i in range(30, len(park) + 1)]) * 365)
ALPHA = 0.06
v = np.empty(len(rv))
v[0] = rv[0] ** 2
for t in range(1, len(rv)):
    v[t] = ALPHA * rv[t] ** 2 + (1 - ALPHA) * v[t - 1]
est_ew = np.sqrt(v * 365)
idx = list(range(0, len(est_cc), 5))
print("FIG7_TRUE " + " ".join(f"({i},{TRUE_SIG[i]:.2f})"
                            for i in range(0, 240, 5)))
print("FIG7_CC  " + " ".join(f"({i+30},{est_cc[i]:.3f})" for i in idx))
print("FIG7_PK  " + " ".join(f"({i+30},{est_pk[i]:.3f})" for i in idx))
print("FIG7_EW  " + " ".join(f"({i},{est_ew[i]:.3f})"
                            for i in range(0, len(est_ew), 5)))

# ---- real BTC QQ data (Kraken, same fetch as kraken_daily.py)
URL = ("https://api.kraken.com/0/public/OHLC"
       "?pair=XBTUSD&interval=1440&since=1704067200")
with urllib.request.urlopen(URL, timeout=30) as f:
    j = json.load(f)
key = next(k for k in j["result"] if k != "last")
rows = j["result"][key]
cl = np.array([float(row[4]) for row in rows])
rb = np.diff(np.log(cl))
z = np.sort((rb - rb.mean()) / rb.std())


def norm_ppf(p):
    """Acklam's inverse-normal-CDF approximation (|err| < 1.15e-9)."""
    a = [-3.969683028665376e+01, 2.209460984245205e+02,
         -2.759285104469687e+02, 1.383577518672690e+02,
         -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02,
         -1.556989798598866e+02, 6.680131188771972e+01,
         -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01,
         -2.400758277161838e+00, -2.549732539343734e+00,
         4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01,
         2.445134137142996e+00, 3.754408661907416e+00]
    p = np.asarray(p, dtype=float)
    x = np.empty_like(p)
    lo = p < 0.02425
    hi = p > 1 - 0.02425
    mid = ~(lo | hi)
    q = np.sqrt(-2 * np.log(p[lo]))
    x[lo] = (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q
             + c[5]) / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    q = np.sqrt(-2 * np.log(1 - p[hi]))
    x[hi] = -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q
              + c[5]) / ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    pm = p[mid] - 0.5
    rr = pm * pm
    x[mid] = (((((a[0] * rr + a[1]) * rr + a[2]) * rr + a[3]) * rr + a[4])
              * rr + a[5]) * pm / (((((b[0] * rr + b[1]) * rr + b[2]) * rr
              + b[3]) * rr + b[4]) * rr + 1)
    return x


n = len(z)
probs = (np.arange(1, n + 1) - 0.5) / n
th = norm_ppf(probs)
sel = list(range(0, n, 40))
print("FIG3_QQ " + " ".join(f"({th[i]:.2f},{z[i]:.2f})" for i in sel))
print(f"# n={n} bars used; QQ pairs printed every 40th bar")

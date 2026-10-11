"""vol_estimators.py -- WE2 + the ch01 synthetic experiment.

Plant a volatility path that REGIME-SWITCHES: sigma = 30%/yr for the
first 120 days, then 90%/yr for 120 days. Three estimators race to
track the switch:
  close-to-close rolling std (window 30),
  Parkinson range estimator (uses h,l as well as c),
  EWMA (alpha = 0.06, RiskMetrics-style).
The printed question: which recovers truth fastest after the jump?
"""
import numpy as np

rng = np.random.default_rng(11)
TRUE_SIG = np.array([0.30] * 120 + [0.90] * 120)   # planted truth, /yr
dt = 1.0 / 365

# OHLC from a random walk driven by the planted sigma path.
# Synthetic intraday range: high/low around close via two extra steps.
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
r = np.diff(np.log(c))

# estimator 1: rolling close-to-close std, window 30, annualised
est_cc = np.array([r[i - 30:i].std(ddof=1) for i in range(30, len(r) + 1)])
est_cc *= np.sqrt(365)

# estimator 2: Parkinson (range) estimator, window 30
park = np.log(h / l) ** 2 / (4 * np.log(2))
est_pk = np.sqrt(np.array([park[i - 30:i].mean()
                           for i in range(30, len(park) + 1)]) * 365)

# estimator 3: EWMA with smoothing weight alpha = 0.06 on squared returns
ALPHA = 0.06
v = np.empty(len(r))
v[0] = r[0] ** 2
for t in range(1, len(r)):
    v[t] = ALPHA * r[t] ** 2 + (1 - ALPHA) * v[t - 1]
est_ew = np.sqrt(v * 365)

t_switch = 120
for name, est in [("close-close", est_cc), ("Parkinson", est_pk),
                  ("EWMA a=0.06", est_ew)]:
    # align index: est[i] estimates sigma over bars ending at i+30/len
    lag = len(r) - len(est)
    pre = est[t_switch - 30 - lag:t_switch - lag].mean()
    post = est[t_switch + 30 - lag:t_switch + 60 - lag].mean()
    # bars until the estimate first exceeds 0.60 after the switch
    xs = np.where(est[t_switch - lag:] > 0.60)[0]
    bars = int(xs[0]) + 1 if len(xs) else -1
    print(f"{name:12s} mean pre-switch={pre:.3f} "
          f"post-30d={post:.3f} bars-to-0.60={bars}")
print("truth: 0.30 for 120 bars, then 0.90")

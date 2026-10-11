"""ch02: ADF test on the four canonical series + cointegrated spread.
statsmodels 0.14.6 (pinned in README)."""
import numpy as np
from statsmodels.tsa.stattools import adfuller
from simulate_ts import white_noise, ar1, ou, random_walk, coint_pair

def report(name, x, regression="c"):
    stat, p, lags, n, crit, _ = adfuller(x, regression=regression,
                                       autolag="AIC")
    verdict = "REJECT unit root (stationary)" if p < 0.05 else \
              "cannot reject (non-stationary by this test)"
    print(f"{name:12s} ADF={stat:+7.3f}  p={p:.4f}  "
          f"crit5%={crit['5%']:+.3f}  -> {verdict}")

if __name__ == "__main__":
    T = 500
    report("white noise", white_noise(T))
    report("AR(1) .85", ar1(T))
    report("OU .12", ou(T))
    report("random walk", random_walk(T))
    x, y, z = coint_pair(T)
    report("coint sprd z", z)
    report("coint y=2x+z", y)
    # borderline: AR(1) with phi=0.98 looks like a walk at T=500
    print()
    print("borderline AR(1) phi=0.98, T=500 (three seeds):")
    for s in (3, 7, 11):
        e = np.random.default_rng(s).normal(0, 1, T)
        v = np.zeros(T)
        for t in range(1, T):
            v[t] = 0.98 * v[t-1] + e[t]
        stat, p, *_ = adfuller(v, autolag="AIC")[:2]
        print(f"  seed {s:2d}: ADF={stat:+6.3f} p={p:.3f} "
              f"{'stationary' if p < 0.05 else 'not detected'}")

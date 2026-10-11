"""ch02: recover a planted OU half-life by the AR(1) regression."""
import numpy as np
from simulate_ts import ou

for theta, tag in ((0.05, "slow"), (0.12, "mid"), (0.30, "fast")):
    x = ou(T=4000, mu=2.0, theta=theta, sigma=0.4, seed=17)
    b, a = np.polyfit(x[:-1], x[1:], 1)
    theta_hat = 1 - b
    mu_hat = a / theta_hat
    hl = np.log(2) / theta_hat
    print(f"planted theta={theta:.2f} mu=2.00 hl={np.log(2)/theta:5.1f} | "
          f"recovered: theta={theta_hat:.3f} mu={mu_hat:.2f} "
          f"hl={hl:5.1f} bars")

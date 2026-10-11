"""ch02: Ljung-Box whiteness check on residuals vs raw returns."""
import numpy as np
from statsmodels.stats.diagnostic import acorr_ljungbox
from simulate_ts import white_noise, ar1

T = 500
wn = white_noise(T)
a1 = ar1(T)
for name, x in (("white noise", wn), ("AR(1) .85 raw", a1)):
    lb = acorr_ljungbox(x, lags=[10], return_df=True)
    print(f"{name:14s} LB(10)={lb['lb_stat'].iloc[0]:7.2f} "
          f"p={lb['lb_pvalue'].iloc[0]:.4f} "
          f"{'-> autocorrelation remains' if lb['lb_pvalue'].iloc[0] < 0.05 else '-> consistent with white noise'}")

# residuals after fitting AR(1): the autocorrelation should be gone
phi_hat = np.corrcoef(a1[:-1], a1[1:])[0, 1] * a1[1:].std() / a1[:-1].std()
res = a1[1:] - phi_hat * a1[:-1]
lb = acorr_ljungbox(res, lags=[10], return_df=True)
print(f"AR(1) resid    LB(10)={lb['lb_stat'].iloc[0]:7.2f} "
      f"p={lb['lb_pvalue'].iloc[0]:.4f} -> consistent with white noise")
print(f"(phi_hat={phi_hat:.3f} vs planted 0.85)")

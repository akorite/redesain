import pandas as pd, numpy as np
from statsmodels.tsa.stattools import adfuller
d = pd.read_csv("data/btc_daily.csv")
y = np.log(d["c"]).to_numpy()
t = np.arange(len(y))
# trend-stationary candidate: residuals from linear trend
b,a = np.polyfit(t, y, 1)
res = y - (b*t+a)
s1 = adfuller(res, regression="n", autolag="AIC")
# difference-stationary: returns
r = np.diff(y)
s2 = adfuller(r, regression="n", autolag="AIC")
print(f"detrended log-price ADF stat {s1[0]:+.3f}  (crit5% {s1[4]['5%']:.3f})")
print(f"differenced (returns) ADF stat {s2[0]:+.3f}  (crit5% {s2[4]['5%']:.3f})")
print(f"trend slope {b*365*100:+.1f}% per yr, R2 of trend fit = {1-np.var(res)/np.var(y):.3f}")
print(f"verdict: returns reject hard ({s2[0]:.1f}); detrended only marginally\n     ({s1[0]:.2f} vs {s1[4]['5%']:.2f}) -- thin evidence for trend-stationarity")
# half-life proxy on returns-autocorr-free residual

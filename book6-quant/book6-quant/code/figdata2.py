"""ch02: emit pgfplots coordinate lists for every ch02 figure."""
import numpy as np
from statsmodels.tsa.stattools import acf
from simulate_ts import white_noise, ar1, ou, random_walk, coint_pair

def dec(coords, k=5):
    return coords[::k] + [coords[-1]]

def emit(name, pts):
    print(name, " ".join(f"({t},{v:.3f})" for t, v in pts))

T = 500
wn, a1, o, rw = white_noise(T), ar1(T), ou(T), random_walk(T)
emit("C_WN", dec(list(enumerate(wn))))
emit("C_AR", dec(list(enumerate(a1))))
emit("C_OU", dec(list(enumerate(o))))
emit("C_RW", dec(list(enumerate(rw))))
for tag, x in (("WN", wn), ("AR", a1), ("OU", o), ("RW", rw)):
    emit("ACF_" + tag, list(enumerate(acf(x, nlags=15)[1:], start=1)))
# OU path with shorter window for the annotated fig
o2 = ou(300, mu=4.0, theta=0.12, sigma=0.35, seed=9)
emit("C_OUP", dec(list(enumerate(o2)), k=3))
x, y, z = coint_pair(T)
emit("C_CX", dec(list(enumerate(x))))
emit("C_CY", dec(list(enumerate(y))))
emit("C_CZ", dec(list(enumerate(z))))
# BTC cached
c = np.loadtxt("data/btc_daily.csv", delimiter=",", skiprows=1, usecols=4)
lp = np.log(c); r = np.diff(lp)
emit("C_BLP", dec(list(enumerate(lp)), k=4))
emit("C_BRT", dec(list(enumerate(r)), k=4))

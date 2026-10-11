import numpy as np
# sqrt-law: instantaneous impact bp = Y * sigma_d * sqrt(participation)
# sigma_d daily 3%, Y=0.7 (from chapter), adv-normalised size Q/ADV=0.10
Y, sig, Q = 0.7, 0.03, 0.10
print("cost vs participation for Q/ADV = 10%, daily vol 3%")
for p in [0.02,0.05,0.10,0.20,0.40]:
    impact = Y*sig*np.sqrt(Q/p)*1e4 if False else Y*sig*np.sqrt(p)*1e4
    days = Q/p
    # timing risk: sigma over the trading window, cost proxy = sigma*sqrt(days)*k
    risk = sig*np.sqrt(days)*1e4
    print(f"part {p:4.0%}: impact {impact:5.1f}bp  duration {days:4.1f}d  1-sigma risk {risk:6.1f}bp")
print("impact falls with slower trading, risk grows -- the execution frontier")

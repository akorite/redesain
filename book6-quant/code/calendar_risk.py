import pandas as pd, numpy as np
t = pd.read_csv("data/btc_daily.csv")
t["d"] = pd.to_datetime(t["time"], unit="s")
r = np.log(t["c"]).diff().dropna()
dow = t["d"].dt.dayofweek[1:]
print("return vol by weekday (annualised):")
for d in range(7):
    v = r[dow==d].std()*np.sqrt(365)
    print(f"  {['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][d]}: {v*100:.0f}%  n={(dow==d).sum()}")
# the classical trap: equities algos assume 24/7; crypto has no weekend effect the same way
wknd = r[dow>=5]; wkdy = r[dow<5]
print(f"weekend vol {wknd.std()*np.sqrt(365)*100:.0f}% vs weekday {wkdy.std()*np.sqrt(365)*100:.0f}%")
print("bar calendars must be built from venue time -- a 'daily' bar that crosses DST is 23h or 25h twice a year")

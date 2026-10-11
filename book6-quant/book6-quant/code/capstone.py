import pandas as pd, numpy as np, json
# CAPSTONE: two-sleeve portfolio on pinned real data.
# sleeve A: BTC spot (Kraken daily bars) -- market beta.
# sleeve B: funding carry -- long spot + short perp nets ~zero delta and
#           earns the funding stream; its daily return ~ daily funding paid.
t = pd.read_csv("data/btc_daily.csv")
r = np.log(t["c"]).diff().dropna().values
f = json.load(open("data/hl_funding_btc.json"))
hourly = np.array([float(x['fundingRate']) for x in f])
days_f = len(hourly)//24
daily_f = hourly[:days_f*24].reshape(days_f,24).sum(1)
carry = daily_f  # hedged sleeve: beta cancels, funding accrues
print(f"funding sleeve: {days_f} days, mean {daily_f.mean()*1e4:.2f}bp/day, vol {daily_f.std()*1e4:.2f}bp")
va = r[:days_f].std(); vb = carry.std()
wa, wb = (1/va), (1/vb); s=wa+wb; wa,wb = wa/s, wb/s
port = wa*r[:days_f] + wb*carry
def st(x,n):
    eq=np.exp(np.nancumsum(x)); mdd=np.min(eq/np.maximum.accumulate(eq)-1)*100
    print(f"{n:>12}: ret {(eq[-1]-1)*100:+6.1f}%  sharpe {x.mean()/x.std()*np.sqrt(365):+.2f}  mdd {mdd:.0f}%")
st(r[:days_f], "btc spot")
st(carry, "funding carry")
st(port, f"rp (w {wa:.3f}/{wb:.3f})")
print(f"corr(spot, carry) = {np.corrcoef(r[:days_f],carry)[0,1]:+.3f}")
print("lesson: the hedged sleeve's tiny vol lets RP hand it huge weight -- real portfolios cap that with leverage and capacity limits")

import json, numpy as np
f = json.load(open("data/hl_funding_btc.json"))
fr = np.array([float(x["fundingRate"]) for x in f])
prem = np.array([float(x["premium"]) for x in f])
hours = len(fr)
print(f"window: {hours}h of BTC funding on Hyperliquid")
print(f"mean funding = {fr.mean()*1e4:.3f} bp/h  ({fr.mean()*24*365*100:.2f}% per yr if sustained)")
print(f"mean premium = {prem.mean()*1e4:.3f} bp/h")
print(f"median funding = {np.median(fr)*1e4:.3f} bp/h  at-floor hours {(np.isclose(fr,0.0000125)).mean()*100:.0f}%")
# cost of a long held the whole window
n = 100000.0
cost = n * fr.sum()
print(f"carry on $100k long over {hours}h = ${cost:,.2f} = {fr.sum()*1e4:.1f} bp")
# worst 8h stretch
w = np.convolve(fr, np.ones(8), "valid")
print(f"worst 8h funding stretch = {w.max()*1e4:.2f} bp  best = {w.min()*1e4:.2f} bp")

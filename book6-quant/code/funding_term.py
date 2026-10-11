import json, numpy as np
f = json.load(open("data/hl_funding_btc.json"))
fr = np.array([float(x["fundingRate"]) for x in f])
# term structure: does funding predict next-day premium?
prem = np.array([float(x["premium"]) for x in f])
# autocorr of premium deviations
d = prem - prem.mean()
acf1 = np.corrcoef(d[:-1],d[1:])[0,1]
acf24 = np.corrcoef(d[:-24],d[24:])[0,1]
# funding paid vs premium realised per 24h block
blk = len(fr)//24
fp = np.array([fr[i*24:(i+1)*24].sum() for i in range(blk)])
pp = np.array([prem[i*24:(i+1)*24].sum() for i in range(blk)])
print(f"premium persistence: lag-1 {acf1:+.3f}  lag-24 {acf24:+.3f}")
print(f"corr(24h funding paid, 24h premium) = {np.corrcoef(fp,pp)[0,1]:+.3f}")
print(f"blocks where funding exceeded premium x2: {(fp>2*np.abs(pp)).sum()}/{blk}")
print(f"annualised carry if sustained: {fr.mean()*24*365*100:.1f}%  realized premium: {prem.mean()*24*365*100:.1f}%")

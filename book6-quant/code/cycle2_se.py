"""ch18: is +0.12bp/h distinguishable from zero on 499 hours?
SE on the mean, and the window length needed to reach 2 SEs."""
import json, math
f = json.load(open('data/hl_funding_btc.json'))
fr = [float(x['fundingRate']) for x in f]
prem = [float(x['premium']) for x in f]
carry = [fr[i] - (prem[i]-prem[i-1]) for i in range(1,len(fr))]
n=len(carry); m=sum(carry)/n
sd=math.sqrt(sum((x-m)**2 for x in carry)/(n-1))
se=sd/math.sqrt(n)
print(f"mean {m*1e4:+.2f}bp/h  sd {sd*1e4:.2f}bp/h  se {se*1e4:.3f}bp/h")
print(f"t-stat {m/se:+.2f} on n={n}h (~{n//24} days)")
need = (2*sd/m)**2 if m>0 else 0
print(f"hours for t=2 at this mean/sd: {need:,.0f} (~{need/24/365:.1f} yr)")
print("note: carry is autocorrelated (premium mean-reverts),")
print("so the honest n is smaller than 499 -- need is understated")

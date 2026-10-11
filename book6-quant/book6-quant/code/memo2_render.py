"""ch18: memo #2 -- computed, not quoted."""
import json, math
f = json.load(open('data/hl_funding_btc.json'))
fr = [float(x['fundingRate']) for x in f]
prem = [float(x['premium']) for x in f]
carry = [fr[i]-(prem[i]-prem[i-1]) for i in range(1,len(fr))]
n=len(carry); m=sum(carry)/n
sd=math.sqrt(sum((x-m)**2 for x in carry)/(n-1)); se=sd/math.sqrt(n)
print("MEMO: HL BTC funding carry, pinned tape (500h)")
print(f"  realized {m*1e4:+.2f}bp/h ({m*24*365*100:+.1f}%/yr), t={m/se:+.1f}")
print("  claim: CONDITIONAL -- real on this window; re-verify on")
print("  a 90d tape before sizing. Venue+wicks are the risk, not the mean.")

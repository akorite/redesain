"""ch18: realized funding-carry on the pinned HL tape.
Carry = short perp + long spot. Per hour the short-perp leg earns
funding and pays d(perp-spot basis): carry_t = fr_t - d(prem_t)."""
import json, math
f = json.load(open('data/hl_funding_btc.json'))
fr = [float(x['fundingRate']) for x in f]
prem = [float(x['premium']) for x in f]
carry = [fr[i] - (prem[i]-prem[i-1]) for i in range(1,len(fr))]
ann = sum(carry)/len(carry)*24*365*100
m = sum(carry)/len(carry)
sd = math.sqrt(sum((x-m)**2 for x in carry)/len(carry))
sh = m/sd*math.sqrt(24*365) if sd>0 else 0
pos = sum(1 for x in carry if x>0)
eq=1.0
for x in carry: eq*=math.exp(x)
print(f"hours: {len(carry)}   mean carry {m*1e4:+.2f}bp/h  ann {ann:+.1f}%")
print(f"sharpe(hourly, ann) {sh:+.2f}   positive hours {pos}/{len(carry)}")
print(f"equity over window {eq:.4f}  (period ~{len(carry)//24} days)")
print("the floor pays -- but the basis takes it back hourly")

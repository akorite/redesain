"""ch18: sizing the carry under a liquidation buffer.
Short perp leg at Lx: liq when perp rises L/... -> keep equity buffer
so a 2x-adverse basis move doesn't touch margin. Reuses ch04's formula."""
import json
f = json.load(open('data/hl_funding_btc.json'))
fr = [float(x['fundingRate']) for x in f]
prem = [float(x['premium']) for x in f]
carry = [fr[i]-(prem[i]-prem[i-1]) for i in range(1,len(fr))]
ann = sum(carry)/len(carry)*24*365
for L in (2,3,5):
    # buffer: hold fraction b of notional as margin, rest the carry books
    # liq if adverse perp move > buffer fraction (approx, MM small)
    b = 1.0/L
    print(f"{L}x notional: buffer {b*100:.0f}% -> liq needs ~{b*100:.0f}% adverse basis move")
print(f"unlevered carry on this window: {ann*100:+.1f}%/yr; at 3x ~{3*ann*100:+.0f}%/yr")
print("the binding constraint is the venue: one adverse wick >33% ends 3x")

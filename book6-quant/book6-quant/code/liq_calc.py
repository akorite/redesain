"""Liquidation price math: long entry, initial margin, maintenance margin."""
def liq_long(entry,qty,im,mm):
    # wallet = im*entry*qty ; liq when loss = wallet - mm*pos
    return entry*(1-im)/(1-mm)
entry,qty,im,mm=50000,0.5,1/25,0.005
liq=entry*(1-im)/(1-mm)
print(f"entry {entry} qty {qty} lev 25x (IM {im*100:.1f}%, MM {mm*100:.1f}%)")
print(f"liquidation price = entry*(1-IM)/(1-MM) = {liq:,.0f}")
print(f"drop to liq = {(1-liq/entry)*100:.2f}%  vs naive 1/leverage = {100/25:.2f}%")
# check: loss at liq == wallet - mm*position
loss=qty*(entry-liq); wallet=qty*entry*im; mmp=qty*liq*mm
print(f"check: loss {loss:,.0f} = wallet {wallet:,.0f} - MM {mmp:,.0f} ? {abs(loss-(wallet-mmp))<1e-6}")
for lev in (2,5,10,25,50):
    im2=1/lev; l=entry*(1-im2)/(1-mm)
    print(f"  {lev:>2}x: liq {l:,.0f}  ({(1-l/entry)*100:.2f}% away)")

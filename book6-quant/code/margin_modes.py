# isolated vs cross margin on the same losing perp position
# pos: long $10k BTC @ entry 50000, lev 5x -> IM 2000. free acct collateral: 3000.
entry, notional, im, free = 50000, 10000, 2000, 3000
mm = 0.005  # maintenance margin 0.5% of notional
def liq_iso():
    # loss that eats IM down to MM: (entry-p)*n = im - mm*n ; n=notional/entry=0.2
    n = notional/entry
    return entry - (im - mm*notional)/n
def liq_cross():
    # same, but the whole 3000 free collateral also absorbs losses
    n = notional/entry
    return entry - (im + free - mm*notional)/n
print(f"position: long {notional} @ {entry}, 5x, IM={im}, free acct={free}, MM=0.5%")
print(f"isolated liq px {liq_iso():.0f} ({(liq_iso()/entry-1)*100:+.1f}%)")
print(f"cross    liq px {liq_cross():.0f} ({(liq_cross()/entry-1)*100:+.1f}%)")
print(f"cross buys {liq_iso()-liq_cross():.0f} more room -- but ALL collateral is at risk, not just {im}")
# cascading: two positions sharing cross collateral
print("cross risk: a second losing pos drains the same pool -> both liq together; isolation caps loss at IM each")

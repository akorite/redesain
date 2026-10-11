ask = [(100.00,20),(100.05,30),(100.15,50)]
def sweep(q, cap, levels):
    got=0; cost=0
    for p,s in levels:
        if p>cap: break
        take=min(s,q-got); cost+=take*p; got+=take
        if got>=q: break
    return got,cost
# MARKETABLE LIMIT buy 60 @<=100.10: third level 100.15 exceeds cap
got,cost = sweep(60,100.10,ask)
print(f"limit buy 60 @<=100.10: fills {got} avg {cost/got:.4f}; 10 rest as bid @100.10 (price cap shields the last level)")
# IOC: fills what crosses now, kills the rest -- nothing rests
print(f"IOC buy 60 @<=100.10: fills {got}, kills {60-got} -- zero resting, zero cap exposure beyond")
# FOK: needs full 60 within cap; only 50 avail -> aborts
print(f"FOK buy 60 @<=100.10: abort ({got} avail < 60) -- all-or-nothing protects partial fills")
# post-only: rest or die -- never takes
print(f"post-only @99.95: joins bid (maker); an order that would cross is cancelled, not filled")
# iceberg: visible tranche understates true size
print(f"iceberg sell 80 show 10: tape reads 10 ask, book refills x7 -- displayed depth understates 8x")

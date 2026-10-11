import numpy as np
# you rest behind 60 units at best bid. queue drains via market sells
# eating ahead volume + cancels. in "panic" the flow is informed:
# after your fill the mid keeps falling (markout) -- the adverse-selection bill.
for name, lam, drift in [("calm", 0.5, 0.00), ("busy", 2.0, -0.0001), ("panic", 8.0, -0.001)]:
    rng2 = np.random.default_rng(5); waits=[]; mark=[]
    for trial in range(2000):
        q=60; t=0
        while q>0 and t<400:
            t += rng2.exponential(1/(lam+0.02*60))
            if rng2.random() < lam/(lam+0.02*60): q -= rng2.integers(1,4)
            else: q -= 1
        if q<=0:
            waits.append(t)
            mark.append(drift*t*1e4)   # adverse drift while waiting, in bp
    print(f"{name:>5}: fill prob 1.00  median wait {np.median(waits):5.1f}s  exp markout {np.mean(mark):+6.1f}bp")
print("faster fills arrive when informed flow trades through you")

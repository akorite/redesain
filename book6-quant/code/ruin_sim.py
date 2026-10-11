import numpy as np
rng=np.random.default_rng(21)
# gambler's ruin: p=0.55, unit bets, bankroll N
p=0.55
for N in (5,10,20,40):
    ruin=0; T=4000
    for _ in range(T):
        b=N
        while 0<b<3*N:
            b += 1 if rng.random()<p else -1
        if b==0: ruin+=1
    print(f"bankroll {N} units: ruin {ruin/T:.1%} of paths (barrier 3x)")

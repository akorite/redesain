# ch15_amdahl.py -- speedup limit for a program with serial fraction s on p cores.
#   speedup(p) = 1 / (s + (1 - s) / p)        ceiling = 1 / s
for s in (0.05, 0.10, 0.20):
    row = "  ".join(f"p={p:<3d} {1 / (s + (1 - s) / p):5.2f}x" for p in (2, 4, 8, 64))
    print(f"serial {s:4.0%}: {row}   ceiling {1 / s:5.1f}x")
# what fraction must be parallel to reach 6x on 8 cores?
p, target = 8, 6.0
s = (1 / target - 1 / p) / (1 - 1 / p)
print(f"6.0x on 8 cores needs serial fraction <= {s:.4f} ({s:.1%})")

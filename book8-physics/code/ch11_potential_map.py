"""ch11: V on a grid from point charges; check -dV/dx ~ Ex numerically,
and energy of assembling a 3-charge configuration (k=1 units)."""
import math

def V(charges, x, y):
    return sum(q/math.hypot(x-xq, y-yq) for q, xq, yq in charges)

def E(charges, x, y):
    ex = ey = 0.0
    for q, xq, yq in charges:
        dx, dy = x-xq, y-yq
        r3 = (dx*dx+dy*dy)**1.5
        ex += q*dx/r3; ey += q*dy/r3
    return ex, ey

charges = [(1.0, -0.5, 0.0), (-1.0, 0.5, 0.0)]
print("Check -dV/dx ~ Ex at sample points (k=1):")
for x, y in [(1.2, 0.3), (0.8, -0.4), (2.0, 0.8)]:
    h = 1e-4
    dVdx = (V(charges, x+h, y) - V(charges, x-h, y))/(2*h)
    ex, ey = E(charges, x, y)
    print(f"  ({x},{y}): -dV/dx={-dVdx:+.4f}  Ex={ex:+.4f}  match={abs(-dVdx-ex)<0.01}")

# assemble [+1 at (-1,0)], [+1 at (1,0)], [-1 at (0,1)]
print("\nAssembly work step by step (sum q_i*V_others):")
placed = []
total = 0.0
for q, x, y in [(1.0,-1,0),(1.0,1,0),(-1.0,0,1)]:
    if placed:
        w = q*V(placed, x, y)
        total += w
        print(f"  bring {q:+} to ({x},{y}): W={w:+.4f}")
    else:
        print(f"  bring {q:+} to ({x},{y}): W=0 (first)")
    placed.append((q,x,y))
print(f"  total assembly energy U = {total:+.4f} (=sum k q_i q_j/r_ij)")
# cross-check pairwise
s = sum(q1*q2/math.hypot(x1-x2,y1-y2) for (q1,x1,y1) in [(1,-1,0),(1,1,0),(-1,0,1)] for (q2,x2,y2) in [(1,1,0),(-1,0,1)] if (x1,y1)!=(x2,y2) and (x1,y1)<(x2,y2)==False) if False else None
pairs = [(1,-1,0),(1,1,0),(-1,0,1)]
tot2 = 0
for i in range(3):
    for j in range(i+1,3):
        q1,x1,y1 = pairs[i]; q2,x2,y2 = pairs[j]
        tot2 += q1*q2/math.hypot(x1-x2,y1-y2)
print(f"  pairwise cross-check: {tot2:+.4f}")

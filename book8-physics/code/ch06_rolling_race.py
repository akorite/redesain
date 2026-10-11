"""ch06: rolling race down an incline for shape factors beta in I=beta*m*r^2.

Energy: mgh = 1/2 m v^2 (1+beta)  ->  v = sqrt(2gh/(1+beta)).
Also prints the energy partition and finish order.
"""
import math

G = 9.8
H = 2.0            # drop height, m

shapes = [("point mass (slide)", 0.0), ("solid sphere", 0.4),
          ("solid disk", 0.5), ("hoop", 1.0)]

print(f"incline drop h={H} m")
print(f"{'shape':<22}{'beta':>6}{'v (m/s)':>10}{'K_tr':>8}{'K_rot':>8}")
results = []
for name, beta in shapes:
    v = math.sqrt(2*G*H/(1+beta))
    Ktr = 0.5*v*v          # per unit mass
    Krot = 0.5*beta*v*v
    results.append((v, name))
    print(f"{name:<22}{beta:>6.1f}{v:>10.3f}{Ktr:>8.2f}{Krot:>8.2f}")
order = sorted(results, reverse=True)
print("\nfinish order: " + " > ".join(n for _, n in order))
print(f"sphere beats hoop by {(results[1][0]-results[3][0])/results[3][0]*100:.1f}% of hoop's speed")

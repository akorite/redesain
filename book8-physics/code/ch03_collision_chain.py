"""ch03: event-stepped collisions of N blocks on a rail.

Each collision conserves momentum; inelasticity set by restitution e
(e=1 elastic, e=0 perfectly inelastic). Prints sum p and sum K before
and after every event.
"""

def collide(m1, v1, m2, v2, e):
    """Post-collision velocities for restitution e along the rail."""
    v1p = (m1*v1 + m2*v2 - m2*e*(v1-v2)) / (m1+m2)
    v2p = (m1*v1 + m2*v2 + m1*e*(v1-v2)) / (m1+m2)
    return v1p, v2p

def totals(blocks):
    p = sum(m*v for m, v in blocks)
    K = sum(0.5*m*v*v for m, v in blocks)
    return p, K

# three blocks: 1 kg at 4 m/s hits 2 kg at rest, then that pair hits 3 kg
blocks = [(1.0, 4.0), (2.0, 0.0), (3.0, 0.0)]
p0, K0 = totals(blocks)
print(f"initial:            p={p0:6.3f} kg m/s   K={K0:6.3f} J")

# collision 1: perfectly inelastic (e=0)
v1, v2 = collide(1.0, 4.0, 2.0, 0.0, 0.0)
blocks = [(3.0, v1), (3.0, 0.0)]       # 1+2 stuck = 3 kg at v1
p, K = totals(blocks)
print(f"after e=0 (1kg+2kg): p={p:6.3f} kg m/s   K={K:6.3f} J  "
      f"(K lost {K0-K:.3f} J = {(K0-K)/K0*100:.1f}%)")

# collision 2: elastic (e=1) between the stuck 3kg and the waiting 3kg
v1, v2 = collide(3.0, v1, 3.0, 0.0, 1.0)
p, K = totals([(3.0, v1), (3.0, v2)])
print(f"after e=1 (3kg+3kg): p={p:6.3f} kg m/s   K={K:6.3f} J  "
      f"v1'={v1:+.3f} v2'={v2:+.3f}")

# restitution sweep: e from 0 to 1 between equal masses, first at 4 m/s
for e in (0.0, 0.5, 1.0):
    va, vb = collide(2.0, 4.0, 2.0, 0.0, e)
    Ki = 0.5*2.0*4.0*4.0
    _, Kf = totals([(2.0, va), (2.0, vb)])
    print(f"e={e}: va'={va:+.3f} vb'={vb:+.3f}  K={Kf:.3f} J "
          f"(lost {(Ki-Kf)/Ki*100:.1f}%)")

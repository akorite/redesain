"""ch13: q v x B motion. Naive Euler spirals outward (energy grows).
A Boris-style exact rotation of v keeps |v| constant and tracks the
theory circle r=mv/qB."""
import math

q, m, B, v0 = 1.0, 1.0, 1.0, 1.0
r_th = m*v0/(q*B)

def naive(dt, steps):
    x, y, vx, vy = r_th, 0.0, 0.0, -v0
    for _ in range(steps):
        x += vx*dt; y += vy*dt
        vx, vy = vx + q*vy*B/m*dt, vy - q*vx*B/m*dt
    return math.hypot(vx, vy), math.hypot(x, y)

def boris(dt, steps):
    """v rotates by angle qB dt/m exactly; position follows."""
    x, y, vx, vy = r_th, 0.0, 0.0, -v0
    om = q*B/m*dt
    c, s = math.cos(om), math.sin(om)
    mn = mx = r_th
    for _ in range(steps):
        vx, vy = c*vx + s*vy, -s*vx + c*vy   # exact rotation
        x += vx*dt; y += vy*dt
        r = math.hypot(x, y)
        mn, mx = min(mn, r), max(mx, r)
    return math.hypot(vx, vy), mn, mx

print(f"theory: r={r_th}, |v|={v0} forever (B does no work)")
for dt in (0.1, 0.01):
    vv, rr = naive(dt, int(60/dt))
    print(f"naive Euler dt={dt}: |v|={vv:.3f}  r={rr:.3f}   <-- secular drift")
for dt in (0.1, 0.01):
    vv, mn, mx = boris(dt, int(60/dt))
    print(f"Boris dt={dt}: |v|={vv:.4f}  r in [{mn:.4f},{mx:.4f}] (theory {r_th})")

# helix: add vz
print(f"\nhelix pitch: vz={0.5} -> pitch={0.5*2*math.pi*m/(q*B):.3f} (period T={2*math.pi*m/(q*B):.3f} indep of v)")

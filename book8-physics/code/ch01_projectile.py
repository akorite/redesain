"""Projectile motion: Euler integration vs the closed-form solution.

v0 = 20 m/s, theta = 45 deg, g = 9.8 m/s^2, flat ground.
Shows the time-step error shrinking like h (Euler is first-order),
then adds quadratic drag and measures the range it steals.
"""
import math

V0, THETA, G = 20.0, math.radians(45.0), 9.8

def analytic_range(v0, th, g=G, h=0.0):
    """Range when landing at height h above launch (signed, h <= peak)."""
    v = v0 * math.sin(th)
    u = v0 * math.cos(th)
    disc = v * v - 2 * g * h  # later root of y(t) = h
    return u * (v + math.sqrt(disc)) / g

def euler_range(v0, th, dt, k=0.0):
    """Simulate x(t), y(t) by forward Euler until y < 0; return range."""
    x = y = 0.0
    vx, vy = v0 * math.cos(th), v0 * math.sin(th)
    while y >= -1e-12:
        speed = math.hypot(vx, vy)
        ax, ay = -k * speed * vx, -G - k * speed * vy
        x += vx * dt; y += vy * dt
        vx += ax * dt; vy += ay * dt
    return x

R_exact = analytic_range(V0, THETA)
print(f"analytic range: {R_exact:8.4f} m")
for dt in (0.1, 0.01, 0.001):
    r = euler_range(V0, THETA, dt)
    print(f"euler dt={dt:<6} range={r:8.4f} m  error={r - R_exact:+7.4f} m")
k = 0.02  # quadratic drag: a_drag = -k |v| v  (per unit mass)
r_drag = euler_range(V0, THETA, 0.001, k)
print(f"with quadratic drag k={k}: range={r_drag:7.4f} m "
      f"({100 * (R_exact - r_drag) / R_exact:.1f}% shorter)")
# elevated target: land on a 5 m ledge, and 5 m below
for h in (5.0, -5.0):
    r_el = analytic_range(V0, THETA, h=h)
    print(f"landing at h={h:+5.1f} m: range={r_el:7.4f} m "
          f"(vs {R_exact:.4f} on flat ground)")

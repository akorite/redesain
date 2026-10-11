"""ch02: quadratic drag fall -- Euler-Cromer vs analytic v(t).

Solves dv/dt = g - (cd/m) v^2 for a falling body. Analytic:
v(t) = vt * tanh(g t / vt), vt = sqrt(m g / cd).
"""
import math

G = 9.8

def analytic_v(t, vt):
    return vt * math.tanh(G * t / vt)

def eulercromer(cd_over_m, dt, t_end):
    """Integrate dv/dt = g - k v^2 with Euler-Cromer (v first, then x)."""
    v, x, t = 0.0, 0.0, 0.0
    while t < t_end:
        v += (G - cd_over_m * v * v) * dt   # update velocity first
        x += v * dt                          # then position with NEW v
        t += dt
    return v, x

m, cd = 80.0, 0.30          # skydiver-ish: 80 kg, cd=0.30 kg/m
k = cd / m
vt = math.sqrt(m * G / cd)
print(f"terminal velocity analytic: {vt:.4f} m/s")
for dt in (0.5, 0.1, 0.01):
    v, x = eulercromer(k, dt, 20.0)
    print(f"euler-cromer dt={dt:<5} v(20s)={v:7.4f} m/s  "
          f"err={v - analytic_v(20.0, vt):+.4f}  fall={x:.1f} m")
# approach: fraction of vt at t = vt/g
tt = vt / G
print(f"at t=vt/g={tt:.2f}s: v={analytic_v(tt, vt):.4f} m/s = "
      f"{analytic_v(tt, vt)/vt*100:.1f}% of vt")
# linear vs quadratic drag comparison at low v
for vtest in (5, 20, 50):
    a_lin = 0.2 * vtest            # cv model with c=0.2
    a_quad = k * vtest * vtest     # cd v^2 model
    print(f"v={vtest:3} m/s: linear drag a={a_lin:5.3f} m/s^2, "
          f"quadratic a={a_quad:6.3f} m/s^2")

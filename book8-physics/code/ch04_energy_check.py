"""ch04: energy drift -- plain Euler vs symplectic (semi-implicit) Euler
on a frictionless block-spring  x'' = -(k/m) x.

Exact energy is conserved; watch each integrator's drift.
"""

m, k, x0 = 1.0, 4.0, 1.0      # kg, N/m, m  (omega = 2 rad/s)
def energy(x, v):
    return 0.5*k*x*x + 0.5*m*v*v

def run(scheme, dt, steps):
    x, v = x0, 0.0
    for _ in range(steps):
        if scheme == "euler":
            x_new = x + v * dt
            v = v - (k/m) * x * dt        # BOTH updates use OLD values
            x = x_new
        else:                              # symplectic
            v += -(k/m) * x * dt          # update v first
            x += v * dt                   # then x with the NEW v
    return x, v

E0 = energy(x0, 0.0)
print(f"E0 = {E0:.4f} J")
print(f"{'scheme':<12}{'dt':>7}{'periods':>9}{'E_end':>12}{'drift':>10}")
for scheme in ("euler", "symplectic"):
    for dt in (0.1, 0.05):
        periods = 10
        steps = int(periods * (2*3.14159265/(k/m)**0.5) / dt)
        x, v = run(scheme, dt, steps)
        E = energy(x, v)
        print(f"{scheme:<12}{dt:>7}{periods:>9}{E:>14.2f}{(E-E0)/E0*100:>12.1f}%")
# long-run: 100 periods, coarse step
x, v = run("euler", 0.1, int(100 * 3.14159265))
print(f"euler 100 periods, dt=0.1: E={energy(x,v):.3f} J "
      f"(x {energy(x,v)/E0:.1f} of original -- secular growth)")
x, v = run("symplectic", 0.1, int(100 * 3.14159265))
print(f"sympl 100 periods, dt=0.1: E={energy(x,v):.3f} J "
      f"(bounded oscillation, no secular drift)")

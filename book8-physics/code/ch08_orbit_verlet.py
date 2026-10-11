"""ch08: velocity-Verlet orbit integrator.
a = -GM r / r^3. Track E and L drift; recover T^2 ~ a^3.
"""
import math

GM = 1.0

def orbit(a, e, steps=200000):
    """Elliptical orbit: start at perihelion r=a(1-e), v=sqrt(GM(1+e)/a(1-e))."""
    x, y = a*(1-e), 0.0
    vx, vy = 0.0, math.sqrt(GM*(1+e)/(a*(1-e)))
    r = math.hypot(x, y)
    E0 = 0.5*vy*vy - GM/r
    L0 = x*vy - y*vx
    # crude period estimate to set dt
    T = 2*math.pi*math.sqrt(a**3/GM)
    dt = T/steps
    maxdriftE = maxdriftL = 0.0
    for i in range(steps):
        r3 = r*r*r
        ax_, ay_ = -GM*x/r3, -GM*y/r3
        x += vx*dt + 0.5*ax_*dt*dt
        y += vy*dt + 0.5*ay_*dt*dt
        r_new = math.hypot(x, y)
        ax2, ay2 = -GM*x/(r_new**3), -GM*y/(r_new**3)
        vx += 0.5*(ax_+ax2)*dt
        vy += 0.5*(ay_+ay2)*dt
        r = r_new
        E = 0.5*(vx*vx+vy*vy) - GM/r
        L = x*vy - y*vx
        maxdriftE = max(maxdriftE, abs(E-E0)/abs(E0))
        maxdriftL = max(maxdriftL, abs(L-L0)/abs(L0))
    return maxdriftE*100, maxdriftL*100, T

for a, e in [(1.0, 0.0), (1.0, 0.5), (1.5, 0.7)]:
    dE, dL, T = orbit(a, e)
    print(f"a={a} e={e}: drift E={dE:.3f}% L={dL:.3f}%  T={T:.3f}")

# Kepler third law: T^2 vs a^3
print("\nKepler III check (T^2/a^3 should be const):")
for a in (0.8, 1.0, 1.3, 1.6):
    T = 2*math.pi*math.sqrt(a**3/GM)
    print(f"  a={a}: T={T:.3f}  T^2/a^3={T*T/a**3:.4f}")

"""ch12: RC charging integrated numerically vs analytic; measure tau
from the trace; energy audit (where did half the battery energy go?)."""
import math

EMF, R, C = 10.0, 2.0e3, 1.0e-3   # 10V, 2k, 1mF -> tau=2.0s

# analytic
tau = R*C
print(f"tau = RC = {tau:.3f} s")

# numeric Euler
dt = 0.005
q = 0.0
t_half = None
t_63 = None
t = 0.0
while t < 6*tau:
    i = (EMF - q/C)/R
    q += i*dt
    t += dt
    if t_63 is None and q >= 0.6321*C*EMF:
        t_63 = t
    if t_half is None and q >= 0.5*C*EMF:
        t_half = t
print(f"numeric: q(t) reaches 63.2% of CV at t={t_63:.3f} s (theory tau={tau:.3f})")
print(f"half-charge at t={t_half:.3f} s (theory tau*ln2={tau*math.log(2):.3f})")

# energy audit over a long charge
E_battery = EMF*C*EMF       # battery supplies EMF * total charge
U_cap = 0.5*C*EMF**2
print(f"\nenergy audit: battery supplies {E_battery:.4f} J")
print(f"  stored in C: {U_cap:.4f} J  ({U_cap/E_battery*100:.0f}%)")
print(f"  burned in R: {E_battery-U_cap:.4f} J  ({(E_battery-U_cap)/E_battery*100:.0f}%)")

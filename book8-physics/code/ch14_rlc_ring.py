"""RLC ring-down: simulate V_C(t), measure the damped period, compare with theory."""
import numpy as np
L, C, R = 50e-3, 100e-6, 5.0   # H, F, ohm
w0 = 1 / np.sqrt(L * C)
wd = np.sqrt(w0**2 - (R / (2 * L))**2)
dt, n = 1e-5, 15000
q, i, t_cross, qprev = 100e-6, 0.0, [], 100e-6
for k in range(n):
    q, i = q + i * dt, i + (-q / C - i * R) * dt / L
    if qprev > 0 and q <= 0:
        t_cross.append(k * dt)
    qprev = q
periods = np.diff(t_cross)
print(f"omega0 = {w0:.1f} rad/s   theory wd = {wd:.1f} rad/s")
print(f"measured zero-crossing periods (s): {[f'{p:.5f}' for p in periods[:3]]}")
print(f"measured wd = {2*np.pi/periods.mean():.1f} rad/s")
print(f"amplitude envelope tau = 2L/R = {2*L/R*1000:.1f} ms")
print(f"energy halves in {(L/R)*np.log(2)*1000:.1f} ms   Q = {w0*L/R:.1f}")

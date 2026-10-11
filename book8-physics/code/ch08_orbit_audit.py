"""Elliptical orbit: track E and L over one period; verify vis-viva at apsides."""
import numpy as np
GM, dt = 4 * np.pi**2, 1e-4            # AU^3/yr^2 units
r = np.array([1.0, 0.0]); v = np.array([0.0, 6.0])   # v < vcirc=2pi -> ellipse
E0 = 0.5 * np.dot(v, v) - GM / np.linalg.norm(r)
L0 = r[0] * v[1] - r[1] * v[0]
rmin, rmax, emin, emax = 1e9, 0, 1e9, -1e9
for i in range(30000):
    a = -GM * r / np.linalg.norm(r)**3
    v = v + a * dt
    r = r + v * dt
    E = 0.5 * np.dot(v, v) - GM / np.linalg.norm(r)
    rr = np.linalg.norm(r)
    rmin, rmax = min(rmin, rr), max(rmax, rr)
    emin, emax = min(emin, E), max(emax, E)
print(f"angular momentum drift: {(r[0]*v[1]-r[1]*v[0])-L0:+.2e}")
print(f"energy drift over run : {emax-emin:.2e}  (E0 = {E0:.4f})")
print(f"r_min = {rmin:.4f} AU   r_max = {rmax:.4f} AU")
a_sem = (rmin + rmax) / 2
print(f"a = {a_sem:.4f} AU   vis-viva check: E = -GM/2a = {-GM/(2*a_sem):.4f}")

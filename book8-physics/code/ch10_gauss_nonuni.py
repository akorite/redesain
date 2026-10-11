"""E(r) for a non-uniform sphere rho = rho0 (1 - r^2/R^2), numeric vs analytic."""
import numpy as np

rho0, R, eps0 = 2.0e-6, 0.10, 8.854e-12   # C/m^3, m
def q_enc(r):
    if r >= R:
        return 8 * np.pi * rho0 * R**3 / 15
    return 4 * np.pi * rho0 * (r**3 / 3 - r**5 / (5 * R**2))
def E_analytic(r):
    return q_enc(r) / (4 * np.pi * eps0 * r**2)
def E_numeric(r):                          # integrate the shells ourselves
    rr = np.linspace(0, min(r, R), 20000)
    q = np.trapezoid(4 * np.pi * rr**2 * rho0 * (1 - rr**2 / R**2), rr)
    return q / (4 * np.pi * eps0 * r**2)

print("r/R    E_analytic (N/C)   E_numeric (N/C)")
for f in [0.2, 0.4, 0.6, 0.8, 1.0, 1.2]:
    r = f * R
    print(f"{f:4.1f}   {E_analytic(r):12.1f}      {E_numeric(r):12.1f}")
rs = np.linspace(1e-4, 0.15, 4000)
rpk = rs[np.argmax([E_analytic(r) for r in rs])]
print(f"peak field at r = {rpk/R:.3f} R   (theory: r = sqrt(5)/3 R = {np.sqrt(5)/3:.3f} R)")
print(f"seam audit: E(R-) {E_analytic(R-1e-4):.1f} vs E(R+) {E_analytic(R+1e-4):.1f} N/C")

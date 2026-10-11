"""ch09: E-field of a point-charge set: dipole far-field + on-axis ring
checks vs Coulomb theory (pure Python, k=1 units)."""
import math

def E(charges, x, y, z=0.0):
    """charges: list of (q, xq, yq, zq). Returns (Ex, Ey, Ez)."""
    ex = ey = ez = 0.0
    for q, xq, yq, zq in charges:
        dx, dy, dz = x-xq, y-yq, z-zq
        r2 = dx*dx + dy*dy + dz*dz
        r3 = r2**1.5
        ex += q*dx/r3; ey += q*dy/r3; ez += q*dz/r3
    return ex, ey, ez

# 1) dipole along x: +q at (a/2,0,0), -q at (-a/2,0,0)
a = 0.1
dip = [(1.0, a/2,0,0), (-1.0, -a/2,0,0)]
print("Dipole far-field ON axis (expect |E| -> 2p/r^3, p=qa=0.1):")
for r in (1.0, 2.0, 4.0):
    ex, ey, ez = E(dip, r, 0, 0)
    th = 2*0.1/r**3
    print(f"  r={r}: |E|={abs(ex):.4f}  theory={th:.4f}  ratio={abs(ex)/th:.3f}")
print("Dipole EQUATOR (expect |E| -> p/r^3):")
for r in (1.0, 2.0):
    ex, ey, ez = E(dip, 0, r, 0)
    th = 0.1/r**3
    print(f"  r={r}: |Ex|={abs(ex):.4f}  theory={th:.4f}")

# 2) ring in yz-plane, axis along x
R, N = 0.5, 200
ring = [(1.0/N, 0.0, R*math.cos(2*math.pi*i/N), R*math.sin(2*math.pi*i/N)) for i in range(N)]
print(f"\nRing N={N} on axis (expect Ex=x/(x^2+R^2)^1.5, Ey=Ez=0):")
for x in (0.2, 0.5, 1.0, 2.0):
    ex, ey, ez = E(ring, x, 0, 0)
    th = x/(x*x+R*R)**1.5
    print(f"  x={x}: Ex={ex:.4f}  theory={th:.4f}  err={abs(ex-th)/th*100:.2f}%  trans={abs(ey)+abs(ez):.1e}")

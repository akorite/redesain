"""ch10: numeric flux through a cube around a point charge -> Q/eps0.
Pure Python; no eps0 needed (work in k=1 units, flux theory = 4*pi*q)."""
import math

def flux_cube(q, half, n):
    """Point charge at origin; cube faces at x,y,z = +-half. n x n grid per face."""
    flux = 0.0
    dA = (2*half/n)**2
    for face in range(6):
        for i in range(n):
            for j in range(n):
                u = -half + (i+0.5)*2*half/n
                v = -half + (j+0.5)*2*half/n
                if face == 0:   p, nvec = ( half, u, v), (1,0,0)
                elif face == 1: p, nvec = (-half, u, v), (-1,0,0)
                elif face == 2: p, nvec = (u,  half, v), (0,1,0)
                elif face == 3: p, nvec = (u, -half, v), (0,-1,0)
                elif face == 4: p, nvec = (u, v,  half), (0,0,1)
                else:           p, nvec = (u, v, -half), (0,0,-1)
                r2 = sum(c*c for c in p)
                r  = math.sqrt(r2)
                En = sum(q*c/r**3 * nv for c, nv in zip(p, nvec))
                flux += En*dA
    return flux

print("Flux of point charge q=1 through enclosing cube (theory 4*pi=12.566):")
for n in (10, 30, 90, 270):
    fl = flux_cube(1.0, 0.5, n)
    print(f"  n={n:>3}: Phi={fl:.4f}  err={abs(fl-4*math.pi)/(4*math.pi)*100:.2f}%")
# charge outside the cube -> zero flux
print("\nCharge OUTSIDE cube (expect ~0): ", end="")
x0 = 2.0
tot = 0.0
n = 60; half = 0.5; dA = (2*half/n)**2
for face in range(6):
    for i in range(n):
        for j in range(n):
            u = -half + (i+0.5)*2*half/n; v = -half + (j+0.5)*2*half/n
            if face == 0:   p, nvec = ( half, u, v), (1,0,0)
            elif face == 1: p, nvec = (-half, u, v), (-1,0,0)
            elif face == 2: p, nvec = (u,  half, v), (0,1,0)
            elif face == 3: p, nvec = (u, -half, v), (0,-1,0)
            elif face == 4: p, nvec = (u, v,  half), (0,0,1)
            else:           p, nvec = (u, v, -half), (0,0,-1)
            dx = (p[0]-x0, p[1], p[2]); r2 = sum(c*c for c in dx); r = math.sqrt(r2)
            tot += sum(c/r**3*nv for c,nv in zip(dx,nvec))*dA
print(f"Phi={tot:.4f}")

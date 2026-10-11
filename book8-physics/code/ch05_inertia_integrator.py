"""ch05: moment of inertia of a lamina by grid quadrature.

I = integral r^2 dm over a unit-density rectangle/disk; compares with the
analytic values and shows the parallel-axis contribution.
"""
import math

def inertia_rect(a, b, nx=400, ny=400):
    """I about the centroid axis perpendicular to an a x b lamina, density=1."""
    dx, dy = a/nx, b/ny
    s = 0.0
    for i in range(nx):
        x = -a/2 + (i+0.5)*dx
        for j in range(ny):
            y = -b/2 + (j+0.5)*dy
            s += (x*x + y*y) * dx*dy
    return s                       # mass-normalise by a*b

def inertia_disk(R, n=300):
    """I about the centre of a unit disk, polar grid."""
    dr, dth = R/n, 2*math.pi/n
    s = 0.0
    for i in range(n):
        r = (i+0.5)*dr
        for j in range(n):
            s += r*r * r*dr*dth   # r^2 * dA, dA = r dr dth
    return s

# rectangle 2 x 1: exact I/M = (a^2+b^2)/12
a, b = 2.0, 1.0
I_num = inertia_rect(a, b)
I_exact = a*b*(a*a+b*b)/12
print(f"rectangle {a}x{b}: numeric I={I_num:.4f}, exact={I_exact:.4f}, "
      f"err={abs(I_num-I_exact)/I_exact*100:.2f}%")
print(f"  per unit mass: I/M={I_num/(a*b):.4f} vs (a^2+b^2)/12={5/12:.4f}")

# disk R=1: exact I/M = R^2/2
R = 1.0
I_num = inertia_disk(R)
I_exact = math.pi*R**4/2
print(f"disk R={R}: numeric I={I_num:.4f}, exact={I_exact:.4f}, "
      f"err={abs(I_num-I_exact)/I_exact*100:.2f}%")
print(f"  per unit mass: I/M={I_num/math.pi:.4f} vs R^2/2=0.5000")

# parallel axis: same disk about a rim point, distance R from centre
M = math.pi * R*R
I_rim = I_num + M*R*R
print(f"disk about rim: I={I_rim:.4f} = I_cm + M R^2 "
      f"({I_num:.4f} + {M*R*R:.4f}); ratio to I_cm = {I_rim/I_num:.2f}")

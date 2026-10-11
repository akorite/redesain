"""N-slit far-field intensity: measure, don't assert, the sharpening."""
import numpy as np
def intensity(phi, N):
    return (np.sin(N * phi / 2) / np.sin(phi / 2))**2
phi = np.linspace(1e-6, 2 * np.pi - 1e-6, 400001)
for N in [2, 3, 8]:
    I = intensity(phi, N)
    # count secondary maxima between the first two principal maxima (0 < phi < 2pi)
    seg = I[1:]
    peaks = int(np.sum((seg[1:-1] > seg[:-2]) & (seg[1:-1] > seg[2:]) & (seg[1:-1] > 1)))
    print(f"N={N}: principal max = {N*N:3d} E0^2,  secondary maxima measured = {peaks}")
# sharpening: first zero sits at phi = 2pi/N -> angular half-width ~ 1/N
for N in [2, 3, 8]:
    print(f"N={N}: first zero at sin(theta) = lambda/({N} d)   line width ~ 1/{N}")

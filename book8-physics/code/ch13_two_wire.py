"""Two parallel wires: force per metre, the ampere definition, a busbar's field."""
import numpy as np
mu0 = 4 * np.pi * 1e-7
def force_per_m(I1, I2, d):
    return mu0 * I1 * I2 / (2 * np.pi * d)

print("   d (m)    F/L (N/m)   for I1=I2=100 A")
for d in [0.01, 0.05, 0.10, 0.50, 1.00]:
    print(f"{d:8.2f}   {force_per_m(100,100,d):10.4f}")
# the ampere definition check: solve force_per_m(I,I,1) = 2e-7
I = np.sqrt(2e-7 * 2 * np.pi * 1.0 / mu0)
print(f"I giving exactly 2e-7 N/m at d=1 m: {I:.4f} A")
# field midway between two antiparallel 100 A busbars 10 cm apart
d = 0.10
Bmid = 2 * mu0 * 100 / (2 * np.pi * (d / 2))
print(f"B midway between antiparallel 100 A bars 10 cm apart: {Bmid*1e6:.1f} uT")

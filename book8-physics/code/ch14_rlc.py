"""ch14: (a) sliding rod on rails: motional EMF -> I -> force -> power
audit (electrical generated = mechanical dissipated);
(b) RLC series ringing: measured vs predicted omega_d and decay."""
import math

# (a) sliding rod
B, L, R, v = 0.8, 0.5, 4.0, 3.0
emf = B*L*v
I = emf/R
F = I*L*B
print(f"rod: emf=BLv={emf:.3f} V, I={I:.3f} A, retarding F={F:.3f} N")
print(f"  mech power F*v={F*v:.3f} W  |  elec power emf*I={emf*I:.3f} W  |  I^2 R={I*I*R:.3f} W")

# (b) RLC ringing: V'' form -> q'' + (R/L) q' + q/(LC) = 0
L2, C2, R2 = 0.05, 1e-4, 2.0
w0 = 1/math.sqrt(L2*C2)
g  = R2/L2
wd = math.sqrt(w0**2 - g**2/4)
print(f"\nRLC: w0={w0:.1f}, gamma={g:.1f}, wd_theory={wd:.1f}")

# integrate q(t), find two successive maxima
q, dq, t, dt = 1e-3, 0.0, 0.0, 1e-6
prev_dq = dq
maxima = []
while t < 0.05 and len(maxima) < 3:
    d2q = -(R2/L2)*dq - q/(L2*C2)
    dq += d2q*dt
    q  += dq*dt
    t  += dt
    if prev_dq > 0 and dq <= 0:
        maxima.append((t, q))
    prev_dq = dq
print("maxima:", [(f"{tt:.4f}s", f"{qq:.2e}") for tt, qq in maxima])
if len(maxima) >= 3:
    T_meas = maxima[2][0]-maxima[1][0]
    print(f"wd_measured = {2*math.pi/T_meas:.1f} (theory {wd:.1f})")
    env = maxima[2][1]/maxima[1][1]
    print(f"decay ratio/cycle = {env:.3f} (theory e^(-gT/2)={math.exp(-g*T_meas/2):.3f})")

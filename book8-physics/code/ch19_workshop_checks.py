"""Capstone workshop: numeric checks for the contest problems' stated
answers (W6, W7, W9, W13, W16, W17, W18, W19)."""
import math

g, RE, G, ME = 9.8, 6.37e6, 6.674e-11, 5.97e24

print("W6 physical pendulum (meter stick, pivot at 20cm mark):")
d = 0.3; I = 1/12 + d*d
T = 2*math.pi*math.sqrt(I/(g*d))
print(f"  I={I:.4f}, d={d}: T={T:.3f} s")

print("\nW7 Hohmann 1.5RE -> 2.5RE:")
r1, r2 = 1.5*RE, 2.5*RE
vc = math.sqrt(G*ME/r1)
a = (r1+r2)/2
v1 = math.sqrt(G*ME*(2/r1 - 1/a))
v2 = math.sqrt(G*ME*(2/r2 - 1/a))
dv = (v1-vc) + (math.sqrt(G*ME/r2)-v2)
print(f"  vc={vc:.0f} m/s, dv1={v1-vc:.0f}, dv2={math.sqrt(G*ME/r2)-v2:.0f}, total={dv:.0f} m/s")

print("\nW9 tunnel through Earth (uniform density):")
T = 2*math.pi*math.sqrt(RE/g)
print(f"  T={T:.0f} s = {T/60:.1f} min; half = {T/120:.1f} min")

print("\nW13 two equal charges released, r0 -> inf:")
q, m, r0 = 1e-6, 0.01, 0.1
mu = m/2
v_rel = math.sqrt(2*8.99e9*q*q*(1/r0)/mu)
print(f"  relative v={v_rel:.2f} m/s, each v={v_rel/2:.2f} m/s")

print("\nW16 RC energy audit:")
E, C = 10.0, 1e-3
print(f"  battery = {E*E*C:.3f} J, stored = {0.5*C*E*E:.3f} J, burned = {E*E*C-0.5*C*E*E:.3f} J")

print("\nW17 velocity selector:")
Ef, B = 3000.0, 0.01
print(f"  v=E/B={Ef/B:.3e} m/s; only undeflected particles pass")

print("\nW18 falling rod terminal velocity:")
m2, L2, R2, B2 = 0.05, 0.4, 2.0, 0.5
vt = m2*g*R2/(B2*B2*L2*L2)
print(f"  v_t=mgR/(B^2 L^2)={vt:.2f} m/s")

print("\nW19 RLC ringing frequency:")
L3, C3 = 10e-3, 1e-6
print(f"  w0=1/sqrt(LC)={1/math.sqrt(L3*C3):.1f} rad/s, f={1/(2*math.pi*math.sqrt(L3*C3)):.0f} Hz")

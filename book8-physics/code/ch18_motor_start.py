"""ch18: DC motor start-up transient. Electrical: V = IR + L dI/dt + E_b,
E_b = Kv*w. Mechanical: J dw/dt = Kt*I - b*w. Euler-Cromer; print
inrush vs steady current, no-load speed, stall current."""
import math

V, R, L = 12.0, 1.5, 0.002
Kv = Kt = 0.02      # same constant in SI
J, b = 1e-4, 1e-5
I, w, t, dt = 0.0, 0.0, 0.0, 1e-5
Imax, tpeak = 0.0, 0.0
samples = []
while t < 30.0:
    dI = (V - I*R - Kv*w)/L
    I += dI*dt
    dw = (Kt*I - b*w)/J
    w += dw*dt
    t += dt
    if I > Imax: Imax, tpeak = I, t
    if any(abs(t-mk)<dt/2 for mk in (0.001,0.05,0.2,1.0,5.0,29.9)):
        samples.append((round(t,3), round(I,3), round(w,1), round(Kv*w,3)))
print("t(s)  I(A)   w(rad/s)  E_b(V)")
for s in samples: print("  ".join(map(str,s)))
print(f"inrush peak I = {Imax:.2f} A at t={tpeak*1e3:.2f} ms")
w_ss = w; I_ss = I
print(f"steady: I={I_ss:.3f} A, w={w_ss:.1f} rad/s = {w_ss*60/2/math.pi:.0f} rpm")
# analytic steady state: Kt*I = b*w, V = IR + Kv*w
# I = b*w/Kt -> V = b*w*R/Kt + Kv*w
w_an = V/(b*R/Kt + Kv)
print(f"analytic w_ss = {w_an:.1f} rad/s, I_ss = {b*w_an/Kt:.3f} A")
print(f"stall current (w=0) = V/R = {V/R:.2f} A")
print(f"stall torque = Kt*I_stall = {Kt*V/R:.4f} N.m")

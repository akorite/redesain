"""ch07: driven damped oscillator via RK4; sweep the drive frequency and
print measured steady amplitude vs the analytic resonance curve.

x'' + gamma x' + w0^2 x = F0/m cos(wd t)
steady amplitude A(wd) = (F0/m) / sqrt((w0^2-wd^2)^2 + (gamma wd)^2)
"""
import math

GAMMA, W0, F0M = 0.4, 2.0, 1.0

def rk4_amp(wd, dt=0.02, t_end=120.0):
    x = v = 0.0
    def acc(x_, v_, t_):
        return F0M*math.cos(wd*t_) - GAMMA*v_ - W0*W0*x_
    t = 0.0
    amp = 0.0
    while t < t_end:
        k1x, k1v = v*dt, acc(x, v, t)*dt
        k2x, k2v = (v+k1v/2)*dt, acc(x+k1x/2, v+k1v/2, t+dt/2)*dt
        k3x, k3v = (v+k2v/2)*dt, acc(x+k2x/2, v+k2v/2, t+dt/2)*dt
        k4x, k4v = (v+k3v)*dt, acc(x+k3x, v+k3v, t+dt)*dt
        x += (k1x+2*k2x+2*k3x+k4x)/6
        v += (k1v+2*k2v+2*k3v+k4v)/6
        t += dt
        if t > t_end*0.75:            # steady state: last quarter
            amp = max(amp, abs(x))
    return amp

def theory(wd):
    return F0M/math.sqrt((W0**2-wd**2)**2 + (GAMMA*wd)**2)

print(f"gamma={GAMMA}, w0={W0}: theory peak at sqrt(w0^2-g^2/2)="
      f"{math.sqrt(W0**2-GAMMA**2/2):.3f} rad/s")
print(f"{'wd':>5} {'A_meas':>8} {'A_theory':>9} {'err':>6}")
for wd in (1.2, 1.6, 1.9, 2.0, 2.1, 2.4, 3.0):
    am = rk4_amp(wd)
    at = theory(wd)
    print(f"{wd:>5} {am:>8.3f} {at:>9.3f} {abs(am-at)/at*100:>5.1f}%")
# Q check: amplitude at resonance / static response
w_res = math.sqrt(W0**2 - GAMMA**2/2)
print(f"Q = w0/gamma = {W0/GAMMA:.1f}; A(w_res)/A(0) = "
      f"{theory(w_res)/theory(0):.2f} (theory)")

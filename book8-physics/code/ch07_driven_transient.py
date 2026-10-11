"""Driven oscillator transient: beat ring-up, then steady state vs theory."""
import numpy as np
m, k, b, F0, w = 1.0, 100.0, 1.0, 1.0, 8.0
w0 = np.sqrt(k / m)
A_theory = F0 / np.sqrt((m * (w0**2 - w**2))**2 + (b * w)**2)
dt, n = 1e-3, 60000
x, v, peaks = 0.0, 0.0, []
for i in range(1, n):
    a = (F0 * np.cos(w * i * dt) - k * x - b * v) / m
    v += a * dt
    x += v * dt
    if i > 55000 and v > 0 and x > (peaks[-1] if peaks else -1):
        pass
    if i > 50000 and i % 10 == 0:
        peaks.append(x)
print(f"w0 = {w0:.1f} rad/s, drive w = {w} rad/s")
print(f"theory steady amplitude: {A_theory:.3f} m")
print(f"late-time window max |x|: {max(abs(np.array(peaks))):.3f} m")
# early beat: x ~ A(t) with beat at |w0-w|/2 in amplitude envelope
print(f"beat envelope frequency |w0-w|/2 = {abs(w0-w)/2:.1f} rad/s")

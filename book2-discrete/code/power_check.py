"""power_check.py -- numeric verification of power of a point.

Setup (coords): circle through A,B,C; P a cevian foot inside/outside.
Compute PA*PB along a secant through P, and PT^2 for a tangent, and
check both equal |OP|^2 - r^2.
"""
import math

# circle: unit circle, center O=(0,0), r=1
O = (0.0, 0.0)
r = 1.0

# P outside at (2,1); secant through P hitting circle at A,B:
# take direction d=(-2,-1)/|..| back toward origin.
P = (2.0, 1.0)
dx, dy = -P[0], -P[1]
L = math.hypot(dx, dy)
ux, uy = dx / L, dy / L
# solve |P + t u|^2 = 1 -> t^2 + 2t(P.u) + |P|^2 - 1 = 0
b = 2 * (P[0] * ux + P[1] * uy)
c = P[0] ** 2 + P[1] ** 2 - 1
disc = b * b - 4 * c
t1 = (-b - math.sqrt(disc)) / 2
t2 = (-b + math.sqrt(disc)) / 2
PA, PB = t1, t2   # distances along the secant (both positive)
power_sec = PA * PB
# tangent length: |PT|^2 = |OP|^2 - r^2
PT2 = P[0] ** 2 + P[1] ** 2 - r * r
print(f"secant: PA*PB = {power_sec:.6f}")
print(f"tangent: PT^2  = {PT2:.6f}")
print(f"agree: {abs(power_sec - PT2) < 1e-9}")
# interior case: Q=(0.3,0.2), chord through Q in direction u2
Q = (0.3, 0.2)
u2 = (math.cos(0.7), math.sin(0.7))
b2 = 2 * (Q[0] * u2[0] + Q[1] * u2[1])
c2 = Q[0] ** 2 + Q[1] ** 2 - 1
d2 = b2 * b2 - 4 * c2
s1 = (-b2 - math.sqrt(d2)) / 2
s2 = (-b2 + math.sqrt(d2)) / 2
QA, QB = -s1, s2  # s1<0 -> distance -s1
power_in = QA * QB
r_pow_in = r * r - (Q[0] ** 2 + Q[1] ** 2)
print(f"interior: QA*QB = {power_in:.6f} vs r^2-|OQ|^2 = {r_pow_in:.6f}")

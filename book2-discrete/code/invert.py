"""invert.py -- numeric inversion about a circle.

Inversion in circle center O radius r sends P -> P' on ray OP with
|OP|.|OP'| = r^2. Verify on a point set: a line not through O should
map to a circle through O.
"""
import math

O = (0.0, 0.0)
r = 2.0


def inv(P):
    d2 = P[0] ** 2 + P[1] ** 2
    k = r * r / d2
    return (P[0] * k, P[1] * k)


# line x=1 sampled; images should lie on a circle through O
pts = [(1.0, y / 2) for y in range(-6, 7)]
imgs = [inv(p) for p in pts]
# circle through O, inv(1,0)=(4,0)... fit: image circle has center
# (2,0), radius 2 (inversion of x=1 about r=2 circle).
errs = [abs(math.hypot(ix - 2.0, iy) - 2.0) for ix, iy in imgs]
print(f"line x=1 -> {len(imgs)} image points")
print(f"max distance from predicted circle (center (2,0), r=2): {max(errs):.2e}")
print(f"inv(inv(P))=P check: {inv(inv((3.0, 1.0)))} vs (3.0, 1.0)")
P=(3.0,0.0); Q=inv(P)
print(f"|OP|*|OP'| = {math.hypot(*P)*math.hypot(*Q):.3f} = r^2 = {r*r}")

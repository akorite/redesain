"""invariant_sim.py -- the difference-reduction process.

Start with a list of positive integers. Move: pick two numbers a,b and
replace them by |a-b|. Repeat until one number remains.
  INVARIANT:   gcd of all entries never changes -> the survivor IS the gcd.
  MONOVARIANT: the sum strictly decreases each move -> process terminates.
"""
from math import gcd
from functools import reduce


def main():
    a = [12, 18, 30, 42]
    print("start:", a)
    g = reduce(gcd, a)
    t = 0
    while len(a) > 1:
        t += 1
        a.sort(reverse=True)
        x, y = a[0], a[1]                    # take the two largest
        a = [x - y] + a[2:]
        a = [v for v in a if v != 0]
        cur_g = reduce(gcd, a) if a else g
        print(f"t={t}: {a}  sum={sum(a) or g}  gcd={cur_g} (invariant {g})")
    print(f"survivor = {a[0]} == gcd({[12,18,30,42]}) = {g}: {a[0]==g}")


if __name__ == "__main__":
    main()

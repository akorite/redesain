"""bezout.py -- the Euclidean algorithm, then read backwards.

Part 1: gcd(252,198) printed step by step, then back-substituted into a
Bezout identity. Part 2: all solutions of 12x + 18y = 30 -- one particular
solution plus the homogeneous family, verified on several t.
"""


def euclid(a, b):
    steps = []
    while b:
        q, r = divmod(a, b)
        steps.append((a, q, b, r))
        a, b = b, r
    return a, steps


def main():
    a0, b0 = 252, 198
    g, steps = euclid(a0, b0)
    print(f"Euclid({a0},{b0}):")
    for a, q, b, r in steps:
        print(f"  {a} = {q}*{b} + {r}")
    print(f"gcd = {g}")

    # back-substitute: walk the steps in reverse. Deepest step has
    # g = 1*a_last + 0*b_last; unwinding a = q*b + r swaps coefficients.
    A, B = 1, 0
    for a, q, b, r in reversed(steps):
        # g = A'*b + B'*r and r = a - q*b -> g = B'*a + (A' - q*B')*b
        A, B = B, A - q * B
    print(f"Bezout: {g} = {A}*{a0} + {B}*{b0}  (check {A*a0 + B*b0})")

    print("\nSolve 12x + 18y = 30:")
    g2 = 6
    print(f"  gcd(12,18) = {g2}, and {g2} | 30 -> solutions exist")
    # 6 = 18 - 12  ->  30 = 5*18 - 5*12 : particular solution (-5, 5)
    print("  particular: x0 = -5, y0 = 5")
    print("  general:    x = -5 + 3t,  y = 5 - 2t")
    for t in (-1, 0, 2):
        x, y = -5 + 3 * t, 5 - 2 * t
        print(f"  t={t}: x={x}, y={y}, check 12x+18y = {12*x + 18*y}")


if __name__ == "__main__":
    main()

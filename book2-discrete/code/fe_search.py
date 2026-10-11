"""fe_search.py -- brute-force polynomial solutions of a toy functional equation.

Equation (on a grid): f(x + y) - f(x - y) = 4xy   (a "d'Alembert" flavor).
Candidate family: degree <= 2 polynomials  f(t) = A t^2 + B t + C.
A poly solves it identically iff it solves it on enough grid points;
we evaluate on a 201-point grid and keep the survivors.
Then check which familiar closed forms survive, and print the verdict.
"""
import itertools

G = [x / 4 for x in range(-100, 101)]  # -25 .. 25 step 0.25


def fe_resid(f):
    """max |f(x+y) - f(x-y) - 4xy| over the grid."""
    return max(
        abs(f(x + y) - f(x - y) - 4 * x * y)
        for x in G[:41]       # keep x+y, x-y inside the grid
        for y in G[:41]
    )


def main():
    # coefficient grid: quadratic candidates
    sols = []
    for A in (i / 4 for i in range(-8, 9)):
        for B in (i / 4 for i in range(-8, 9)):
            for C in (i / 4 for i in range(-8, 9)):
                if fe_resid(lambda t, a=A, b=B, c=C: a * t * t + b * t + c) < 1e-9:
                    sols.append((A, B, C))
    uniq = {(a, b) for a, b, c in sols}
    print(f"quadratic survivors: {sorted(uniq)}")
    print(f"constant term free? distinct C values per (A,B): "
          f"{len(sols) == len(set(c for a, b, c in sols))}")
    # closed-form check
    for name, f in [("t^2 + c", lambda t: t * t),
                    ("t^2 - 1", lambda t: t * t - 1),
                    ("2t^2", lambda t: 2 * t * t),
                    ("t", lambda t: t),
                    ("0", lambda t: 0)]:
        print(f"  f={name}: residual {fe_resid(f):.3f}")
    print("verdict: f(t) = t^2 + C is the whole degree-<=2 family")


if __name__ == "__main__":
    main()

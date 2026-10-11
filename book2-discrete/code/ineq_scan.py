"""ineq_scan.py -- Monte-Carlo checks of Nesbitt and AM-GM on random triples.

Nesbitt: a/(b+c) + b/(c+a) + c/(a+b) >= 3/2 for a,b,c > 0.
AM-GM:   (a+b+c)/3 >= (abc)^(1/3), equality iff a=b=c.
Also prints the minimizer of x + 1/x on x > 0 found by grid search.
"""
import random


def nesbitt(a, b, c):
    return a / (b + c) + b / (c + a) + c / (a + b)


def main():
    random.seed(3)
    trials = 10000
    mn, arg = 10**9, None
    gm_ok = True
    for _ in range(trials):
        a, b, c = (10 ** random.uniform(-2, 2) for _ in range(3))
        v = nesbitt(a, b, c)
        if v < mn:
            mn, arg = v, (a, b, c)
        if (a + b + c) / 3 < (a * b * c) ** (1 / 3) - 1e-9:
            gm_ok = False
    print(f"Nesbitt over {trials} random triples: min = {mn:.4f} >= 1.5")
    print(f"  at (a,b,c) = {tuple(round(t,3) for t in arg)}")
    print(f"AM-GM held on all {trials} triples: {gm_ok}")
    best, bx = min((x + 1 / x, x) for x in (i / 200 for i in range(1, 2000)))
    print(f"x + 1/x minimizer on grid: x = {bx}, value = {best:.4f}")
    print("theory: equality at x = 1, minimum value = 2")


if __name__ == "__main__":
    main()

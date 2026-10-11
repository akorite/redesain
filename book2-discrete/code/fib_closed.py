"""fib_closed.py -- recurrence vs Binet's closed form, with round-off warning.

Binet: F_n = (phi^n - psi^n) / sqrt(5), phi=(1+sqrt5)/2, psi=(1-sqrt5)/2.
Exact in real arithmetic; floats are not reals -- watch where it drifts.
"""
from math import sqrt

PHI = (1 + sqrt(5)) / 2
PSI = (1 - sqrt(5)) / 2


def fib_recurrence(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_binet(n):
    return (PHI ** n - PSI ** n) / sqrt(5)


def main():
    print("n | recurrence | Binet (float) | round | ok?")
    first_bad = None
    for n in (10, 20, 40, 50, 60, 70, 71, 72):
        exact = fib_recurrence(n)
        approx = fib_binet(n)
        ok = round(approx) == exact
        if not ok and first_bad is None:
            first_bad = n
        print(f"{n:>3} | {exact} | {approx:.6e} | {round(approx)} | {ok}")
    print(f"first float failure at n = {first_bad} "
          "(double precision; exact answer needs ints)")


if __name__ == "__main__":
    main()

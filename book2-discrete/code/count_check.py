"""count_check.py -- brute-force enumeration vs closed forms.

Three checks on small instances:
  subsets of [n]:        2^n            vs enumeration
  lattice paths m x n:   C(m+n, m)      vs recursion-free walk count
  stars and bars x1+..+xk = n (>= 0):   C(n+k-1, k-1) vs enumeration
"""
from itertools import combinations, product
from math import comb


def main():
    print("subsets: n=4")
    n = 4
    enum = sum(1 for _ in product([0, 1], repeat=n))
    print(f"  enum={enum}  closed=2^{n}={2**n}")

    print("lattice paths: 3x2 grid")
    m, k = 3, 2
    enum = sum(1 for w in combinations(range(m + k), m))
    print(f"  enum={enum}  closed=C({m+k},{m})={comb(m+k, m)}")

    print("stars and bars: x1+x2+x3+x4 = 6, x >= 0")
    n, k = 6, 4
    enum = sum(1 for c in combinations(range(n + k - 1), k - 1))
    print(f"  enum={enum}  closed=C({n+k-1},{k-1})={comb(n+k-1, k-1)}")

    print("pigeonhole demo: 51 numbers from 1..100, two differ by 2x")
    worst = [2*i - 1 for i in range(1, 51)]
    print(f"  all-odd set {worst[:5]}...{worst[-3:]}: no pair doubles -> {len(worst)} evades")
    print(f"  adding any even e makes e/2 or 2e odd-divisor-equal")


if __name__ == "__main__":
    main()

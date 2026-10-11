"""gf_coin.py -- generating function for coin change, coefficients by hand.

The GF for coins {5, 10, 25} is  1 / ((1-x^5)(1-x^10)(1-x^25)).
Each factor is the geometric series 1 + x^c + x^2c + ...; multiplying
truncated series coefficient-by-coefficient IS the GF computation
(SymPy's `series` does the same algebra). Verified against DP/brute force.
"""
from itertools import product

N = 30


def gf_coeffs(coins, n):
    """Multiply the series prod_c (1 + x^c + x^2c + ...) truncated to x^n."""
    g = [1] + [0] * n
    for c in coins:
        ng = g[:]            # convolution with the coin's series
        for k in range(c, n + 1, c):
            for j in range(n - k + 1):
                ng[j + k] += g[j]
        g = ng
    return g


def brute(n):
    return sum(1 for a, b, c in product(range(n + 1), repeat=3)
               if 5 * a + 10 * b + 25 * c == n)


def main():
    g = gf_coeffs([5, 10, 25], N)
    print("GF product for coins {5,10,25}, terms through x^30:")
    print("  coefficients [x^0..x^30] nonzero:",
          {i: g[i] for i in range(N + 1) if g[i]})
    print(f"[x^30] by GF:  {g[N]}")
    print(f"[x^30] by brute force: {brute(N)}")


if __name__ == "__main__":
    main()

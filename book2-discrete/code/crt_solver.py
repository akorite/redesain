"""crt_solver.py -- CRT two ways: brute force vs constructive.

Solves x == r_i (mod m_i) for pairwise-coprime moduli by (a) scanning
0..M-1 and (b) the constructive proof (reduce to two congruences at a
time via Bezout), then prints the unique class mod the product.
"""


def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def crt_pair(r1, m1, r2, m2):
    # x = r1 + m1*t; need m1*t == r2 - r1 (mod m2)
    g, s, _ = egcd(m1, m2)
    assert (r2 - r1) % g == 0, "inconsistent"
    t = (s * (r2 - r1) // g) % (m2 // g)
    return (r1 + m1 * t) % (m1 * m2 // g), m1 * m2 // g


def main():
    mods = [(2, 3), (3, 5), (2, 7)]
    print("system: x == 2 (mod 3), x == 3 (mod 5), x == 2 (mod 7)")

    brute = [x for x in range(3 * 5 * 7)
             if all(x % m == r for r, m in mods)]
    print(f"brute force scan: {brute}")

    r, M = mods[0]
    for r2, m2 in mods[1:]:
        r, M = crt_pair(r, M, r2, m2)
        print(f"  folded: x == {r} (mod {M})")
    print(f"constructive: x == {r} (mod {M})")
    assert brute == [r]
    print(f"unique mod {M}: {r}; check {[r % m for _, m in mods]}")


if __name__ == "__main__":
    main()

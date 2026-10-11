"""check_prime_run.py -- Euler's polynomial f(x) = x^2 + x + 41.

Brute-force primality check for x = 0..50: where does the famous
prime streak break, and how often?
"""


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def least_factor(n):
    d = 2
    while n % d:
        d += 1
    return d


f = lambda x: x * x + x + 41

composites = [(x, f(x)) for x in range(51) if not is_prime(f(x))]
first_x = composites[0][0]

print("f(x) = x^2 + x + 41")
print(f"x = 0..{first_x - 1}: all prime ({first_x} consecutive values)")
for x, v in composites:
    d = least_factor(v)
    tag = "  <-- first composite" if x == first_x else ""
    print(f"x = {x:2d}: f({x}) = {v} = {d} * {v // d}{tag}")
print(f"{len(composites)} composites in x = 0..50")

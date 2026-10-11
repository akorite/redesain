"""powers_cycle.py -- powers of a mod m until the cycle repeats.

Prints a^k mod m for k = 1,2,... stopping when a value returns to a
previously seen residue (the cycle boundary), then reports the period.
Run: python3 powers_cycle.py [a m]   (default a=7, m=100)
"""
import sys


def powers_cycle(a, m):
    seen = {}
    cur = 1 % m
    k = 0
    while cur not in seen:
        seen[cur] = k
        cur = (cur * a) % m
        k += 1
    # cur now equals seen[cur]'s earlier value: cycle is seen[cur]..k-1
    start = seen[cur]
    return start, k - start, seen


def main():
    a = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    m = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    start, period, seen = powers_cycle(a, m)
    print(f"powers of {a} mod {m}:")
    items = sorted(seen.items(), key=lambda kv: kv[1])
    for v, k in items:
        print(f"  {a}^{k} == {v}")
    print(f"  {a}^{len(items)} == {(items[0][0]) if start == 0 else seen_inv(items, start)}  (repeat)")
    print(f"cycle starts at k={start}, period = {period}")
    # application: last two digits of a^2026
    e = 2026
    kk = start + (e - start) % period if e >= start else e
    print(f"so {a}^{e} mod {m} = {a}^{kk} mod {m} = {pow(a, e, m)}")


def seen_inv(items, k):
    for v, kk in items:
        if kk == k:
            return v


if __name__ == "__main__":
    main()

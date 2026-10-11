#!/usr/bin/env python3
# gen_inputs.py -- generates the input files used by Chapter 1's listings.
import random
import sys

def ints(path, n, lo=-1000, hi=1000, seed=1):
    rng = random.Random(seed)
    with open(path, "w") as f:
        f.write(f"{n}\n")
        f.write(" ".join(str(rng.randint(lo, hi)) for _ in range(n)) + "\n")

def missing(path, n, missing_value, seed=2):
    rng = random.Random(seed)
    vals = [v for v in range(1, n + 1) if v != missing_value]
    rng.shuffle(vals)
    with open(path, "w") as f:
        f.write(f"{n}\n")
        f.write(" ".join(map(str, vals)) + "\n")

if __name__ == "__main__":
    ints("ints1e6.txt", 1_000_000, 0, 10**9)          # for fastscan.cpp
    missing("missing_big.txt", 200_000, 200_000)      # for missing_*.cpp
    ints("mss_stress.txt", 20, -20, 20, seed=3)       # one stress case
    print("generated ints1e6.txt, missing_big.txt, mss_stress.txt")

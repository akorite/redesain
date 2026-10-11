#!/bin/sh
# test_ch01.sh -- Chapter 1 checks, run by `make test`.
# 1) fixed-case checks for this chapter's submissions
# 2) a 200-round stress test: mss_linear vs mss_brute on random arrays
set -e
cd "$(dirname "$0")"
CXX=${CXX:-clang++}
CXXFLAGS="-std=c++17 -O2 -Wall -Wextra"
mkdir -p .build

for p in weird missing_math missing_set missing_int mss_linear mss_brute repetitions; do
    $CXX $CXXFLAGS -o .build/$p $p.cpp
done

echo "== weird (n=3) =="
[ "$(echo 3 | .build/weird)" = "3 10 5 16 8 4 2 1" ] && echo PASS

echo "== missing number (n=4, missing 2) =="
printf "4\n1 3 4\n" > .build/miss4.txt
a=$(.build/missing_math < .build/miss4.txt)
b=$(.build/missing_set < .build/miss4.txt)
[ "$a" = "2" ] && [ "$b" = "2" ] && echo PASS

echo "== stress: mss_linear vs mss_brute, 200 rounds =="
python3 - <<'PY'
import random, subprocess, sys
rng = random.Random(12345)
for t in range(200):
    n = rng.randint(1, 30)
    arr = [rng.randint(-50, 50) for _ in range(n)]
    data = f"{n}\n{' '.join(map(str, arr))}\n".encode()
    a = subprocess.run([".build/mss_linear"], input=data,
                       capture_output=True).stdout.strip()
    b = subprocess.run([".build/mss_brute"], input=data,
                       capture_output=True).stdout.strip()
    if a != b:
        print(f"MISMATCH round {t}: linear={a} brute={b} arr={arr}")
        sys.exit(1)
print("200/200 rounds agree")
PY
[ "$(echo ATTCGGGA | .build/repetitions)" = "3" ] && echo "repetitions PASS"

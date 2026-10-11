#!/bin/bash
# test_ch03.sh -- fixed CSES samples + stress harness for chapter 3.
set -e
cd "$(dirname "$0")"
CXX=${CXX:-clang++}; F="-std=c++17 -O2 -Wall -Wextra"
mkdir -p .build
for p in sort_cmp compress_demo movie_festival stick_lengths apartments \
         ferris_wheel coins set_pattern; do
    $CXX $F -o .build/$p $p.cpp
done

echo "== fixed samples =="
diff <(./.build/sort_cmp) - <<'X'
bella 9
cato 9
anni 7
dele 4
X
echo "sort_cmp PASS"
diff <(./.build/compress_demo) - <<'X'
4000000000 -> 2
10 -> 0
10 -> 0
80 -> 1
4000000000 -> 2
distinct values: 3
X
echo "compress PASS"
expect() { # expect <name> <want-substring> <output>
  echo "$3" | grep -qF "$2" || { echo "FAIL $1: wanted '$2' in: $3" >&2; exit 1; }
  echo "$1 PASS"
}
expect movie 2 "$(printf "3\n3 5\n4 9\n5 8\n" | ./.build/movie_festival)"
expect stick 5 "$(printf "5\n2 3 1 5 2\n" | ./.build/stick_lengths)"
expect apts 2 "$(printf "4 3 5\n60 45 80 60\n30 60 75\n" | ./.build/apartments)"
expect ferris 3 "$(printf "4 10\n7 2 3 9\n" | ./.build/ferris_wheel)"
expect "coins counterex" "greedy=3 optimal=2" "$(./.build/coins 6 1 3 4)"
expect "coins counterex-order" "greedy=3 optimal=2" "$(./.build/coins 6 4 3 1)"
expect "coins US" "greedy=9 optimal=9" "$(./.build/coins 99 1 5 10 25)"
printf "5 3\n5 3 7 8 5\n4 8 3\n" | ./.build/set_pattern | diff - <(printf "3\n8\n-1\n") && echo "set PASS"
expect "end-greedy" 2 "$(printf "3\n0 10\n1 2\n3 4\n" | ./.build/movie_festival)"
expect "start-greedy fails" 1 \
  "$(printf "3\n0 10\n1 2\n3 4\n" | ./.build/movie_festival start)"
echo "earliest-start counterexample PASS"

echo "== stress: median vs brute argmin (300 rounds) =="
python3 - <<'PY'
import random, subprocess
for t in range(300):
    n = random.randint(1, 21); p = [random.randint(-50, 50) for _ in range(n)]
    inp = f"{n}\n{' '.join(map(str,p))}\n"
    got = int(subprocess.run(['./.build/stick_lengths'], input=inp,
                             capture_output=True, text=True).stdout)
    brute = min(sum(abs(x - m) for x in p) for m in range(min(p), max(p) + 1))
    assert got == brute, (p, got, brute)
print("median stress: 300/300 PASS")
PY

echo "== stress: end-greedy vs exhaustive brute (200 rounds, n<=10) =="
python3 - <<'PY'
import itertools, random, subprocess
def brute(m):
    best = 0
    for r in range(len(m) + 1):
        for sub in itertools.combinations(m, r):
            sub = sorted(sub)
            if all(sub[i][1] <= sub[i+1][0] for i in range(len(sub)-1)):
                best = max(best, len(sub))
    return best
for t in range(200):
    n = random.randint(1, 10)
    m = [(a, b) for a, b in
         ((random.randint(0, 15), 0) for _ in range(n))
         for a, b in [(a, random.randint(a+1, a+8))]]
    inp = f"{n}\n" + "\n".join(f"{a} {b}" for a, b in m) + "\n"
    got = int(subprocess.run(['./.build/movie_festival'], input=inp,
                             capture_output=True, text=True).stdout)
    assert got == brute(m), (m, got)
print("interval stress: 200/200 PASS")
PY
echo "test_ch03: ALL PASS"

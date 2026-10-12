#!/bin/bash
# test_ch10.sh -- caches: the simulator's exact counts are checked exactly
# (they are deterministic); the wall-clock harness is checked for shape only.
cd "$(dirname "$0")" || exit 1
set -e
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
CC=${CC:-gcc}
$CC -O2 -Wall -o "$T/sim" ch10_cache_sim.c
$CC -O2 -Wall -o "$T/trace" ch10_trace.c
$CC -O2 -Wall -o "$T/real" ch10_transpose_real.c

# 1. the hand-traced 10-access example of the chapter
"$T/trace" 2 2 8 0 8 16 24 0 32 8 40 16 0 | tee "$T/t1.txt"
grep -q "hits=2 misses=8 evictions=4" "$T/t1.txt"
# 2. the N=4 transpose of exercise 5: direct-mapped, naive then blocked
"$T/trace" 2 1 8 0 w32 2 w40 4 w48 6 w56 8 w34 10 w42 12 w50 14 w58 16 w36 18 w44 20 w52 22 w60 24 w38 26 w46 28 w54 30 w62 | tail -1 | grep -q "hits=6 misses=26"
# 3. the simulator's exact miss counts
"$T/sim" | tee "$T/sim.txt"
for want in \
  "E=1      misses=71552" "E=2      misses=69632" \
  "naive    misses=69632" "block4   misses=20480" "block8   misses=12512" \
  "block16  misses=10064" "block32  misses=69632" \
  "capacity=61440   conflict=0" \
  "capacity=0       conflict=61440" \
  "demand misses=67833" "block32  misses=8192" "naive    misses=24792" \
  "block8   misses=847872" "block16  L1 misses=4456448  L2 misses=524288"; do
  grep -q -F "$want" "$T/sim.txt" || { echo "MISSING: $want"; exit 1; }
done
# 4. the real transpose: every variant correct, blocked faster than naive
"$T/real" | tee "$T/real.txt"
! grep -q WRONG "$T/real.txt"
n=$(awk '/^naive/{print $4}' "$T/real.txt"); b=$(awk '/^block 8/{print $4}' "$T/real.txt")
awk -v n="$n" -v b="$b" 'BEGIN{printf "naive %.2f ms, block-8 %.2f ms, %.2fx\n",n,b,n/b; exit !(n>=1.3*b)}'
echo "ch10 PASS: simulator counts exact, 3-C split exact, real transpose correct and blocked faster"

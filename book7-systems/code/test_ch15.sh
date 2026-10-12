#!/bin/bash
# test_ch15.sh -- builds and runs ch15's code and checks the claimed outputs.
cd "$(dirname "$0")" || exit 1
T=$(mktemp -d) || exit 1
trap 'rm -rf "$T"' EXIT
fail() { echo "ch15 FAIL: $1"; exit 1; }

gcc -O2 -w -o "$T/bench"   ch15_bench.c          || fail "compile bench"
gcc -O2 -w -o "$T/dce0"    ch15_dce.c            || fail "compile dce0"
gcc -O2 -w -DSINK -o "$T/dce1" ch15_dce.c        || fail "compile dce1"
gcc -O2 -w -o "$T/cdf"     ch15_cdf.c -lm        || fail "compile cdf"
gcc -O2 -w -o "$T/compare" ch15_compare.c -lm    || fail "compile compare"

# 1. harness: p50 <= p99 <= max, and the foil line is printed
"$T/bench" > "$T/b.out" || fail "bench"
grep -q "^n=4M ints sum: p50=" "$T/b.out" || fail "bench format"
grep -q "^same, 3 cold samples:" "$T/b.out" || fail "bench foil line"
set -- $(sed -n 's/^n=4M ints sum: p50=\([0-9.]*\)ms p99=\([0-9.]*\)ms.*/\1 \2/p' "$T/b.out"); p50=$1; p99=$2
awk -v a="$p50" -v b="$p99" 'BEGIN{exit !(b>=a && a>0)}' || fail "bench p50/p99 ($p50, $p99)"

# 2. dead-code elimination: without the sink the kernel vanishes
"$T/dce0" > "$T/d0.out"; "$T/dce1" > "$T/d1.out"
t0=$(sed -n 's/.*best of 11 = \([0-9.]*\) ms.*/\1/p' "$T/d0.out")
t1=$(sed -n 's/.*best of 11 = \([0-9.]*\) ms.*/\1/p' "$T/d1.out")
awk -v a="$t0" 'BEGIN{exit !(a<0.01)}' || fail "kernel was not eliminated without sink ($t0 ms)"
awk -v a="$t1" 'BEGIN{exit !(a>0.1)}'  || fail "kernel suspiciously fast with sink ($t1 ms)"

# 3. distribution: percentiles ordered, histogram counts add up to 1000
"$T/cdf" > "$T/c.out" || fail "cdf"
set -- $(sed -n 's/^p50=\([0-9.]*\)  p90=\([0-9.]*\)  p99=\([0-9.]*\)  p99.9=\([0-9.]*\)  max=\([0-9.]*\).*/\1 \2 \3 \4 \5/p' "$T/c.out"); q50=$1; q90=$2; q99=$3; q999=$4; mx=$5
awk -v a="$q50" -v b="$q90" -v c="$q99" -v d="$q999" -v e="$mx" 'BEGIN{exit !(a<=b && b<=c && c<=d && d<=e && a>0)}' || fail "percentile order"
tot=$(awk '/^histogram/ {h=1; next} h && /: *[0-9]+$/ {s += $NF} END{print s}' "$T/c.out")
[ "$tot" = 1000 ] || fail "histogram sums to $tot, not 1000"

# 4. A/B comparison prints a verdict
"$T/compare" > "$T/cmp.out" || fail "compare"
grep -q "^verdict: " "$T/cmp.out" || fail "compare verdict"

# 5. Amdahl numbers quoted in the chapter
python3 ch15_amdahl.py > "$T/a.out" || fail "amdahl"
grep -q "serial  10%: p=2    1.82x  p=4    3.08x  p=8    4.71x" "$T/a.out" || fail "amdahl 10%"
grep -q "ceiling  20.0x" "$T/a.out" || fail "amdahl 5% ceiling"
grep -q "serial fraction <= 0.0476" "$T/a.out" || fail "amdahl inverse"

echo "ch15 PASS"

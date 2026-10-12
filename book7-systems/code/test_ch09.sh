#!/bin/bash
# test_ch09.sh -- memory hierarchy: builds and runs the chapter's four C
# benchmarks (shortened) and checks the SHAPE of the results, never exact
# nanoseconds (those differ per machine and per run).
cd "$(dirname "$0")" || exit 1
set -e
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
CC=${CC:-gcc}
$CC -O2 -Wall -o "$T/mm"  ch09_mem_mountain.c
$CC -O2 -Wall -o "$T/sb"  ch09_stride_bw.c
$CC -O2 -Wall -o "$T/dvi" ch09_dep_vs_indep.c
$CC -O2 -Wall -o "$T/vc"  ch09_volatile_cost.c

"$T/mm" 2000000 16777216 | tee "$T/mm.txt"
small=$(awk '$1==4096{print $2}' "$T/mm.txt")
big=$(awk '$1==16777216{print $2}' "$T/mm.txt")
awk -v a="$small" -v b="$big" 'BEGIN{printf "mountain: 4 KiB %.2f ns, 16 MiB %.2f ns, ratio %.0fx\n",a,b,b/a; exit !(b>=10*a)}'

"$T/sb" | tee "$T/sb.txt"
s1=$(awk '$1==1{print $2}' "$T/sb.txt"); s64=$(awk '$1==64{print $2}' "$T/sb.txt")
awk -v a="$s1" -v b="$s64" 'BEGIN{printf "stride: 1 -> %.2f ns/acc, 64 -> %.2f ns/acc\n",a,b; exit !(b>=3*a)}'

"$T/vc" | tee "$T/vc.txt"
awk '/plain/{p=$4} /volatile/{v=$4} END{exit !(v>1.3*p)}' "$T/vc.txt"

"$T/dvi" | tee "$T/dvi.txt"
awk '$1==134217728{printf "dep/indep at 128 MiB: %.1fx\n",$2/$3; exit !($2>=3*$3)}' "$T/dvi.txt"
echo "ch09 PASS: latency grows >=10x with footprint, stride cost rises >=3x, dependent chain >=3x slower than independent at 128 MiB"

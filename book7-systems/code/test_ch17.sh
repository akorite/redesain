#!/bin/bash
# test_ch17.sh -- build and run every ch17 program on x86_64 and check the claims.
# Timing checks use loose thresholds (shared container, noisy).
cd "$(dirname "$0")"
set -e
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
fail(){ echo "ch17 FAIL: $1"; exit 1; }

# 1. original single-thread ring and its capacity/wrap-around arithmetic
gcc -O2 ch17_ringbuf.c -o "$T/rb";  "$T/rb" | tee ch17_ringbuf.out
grep -q "1M push/pop pairs, 0 mismatches" ch17_ringbuf.out || fail "ringbuf"
gcc -O2 ch17_ringfull.c -o "$T/rf"; "$T/rf" | tee ch17_ringfull.out
grep -q "pushes accepted before full: 255  (head=255 tail=0)" ch17_ringfull.out || fail "ring capacity"
grep -q "after 10 more pushes: head=9 tail=10" ch17_ringfull.out || fail "ring wrap"
grep -q "drained 255 items, last value 1009" ch17_ringfull.out || fail "ring drain"

# 2. the folklore audit re-run (x86 numbers are NOT the Mac numbers: just check it runs
#    and that the compiler turned the 'branchy' min into a cmov)
gcc -O2 ch17_folklore.c -o "$T/fk" 2>/dev/null; "$T/fk" | tee ch17_folklore_x86.out
grep -q "binary n=16M" ch17_folklore_x86.out || fail "folklore output"
if [ "$(uname -m)" = "x86_64" ]; then
  gcc -O2 -S ch17_folklore.c -o - 2>/dev/null | grep -q "cmov" || fail "expected cmov for branchy min"
else
  echo "ch17 note: not x86_64, cmov mnemonic check skipped"
fi

# 3. branch experiment: real branch (jle in the branchy loop), random vs sorted
gcc -O2 -fno-tree-vectorize ch17_branch_x86.c -o "$T/br"
gcc -O2 -fno-tree-vectorize -c ch17_branch_x86.c -o "$T/br.o"
if [ "$(uname -m)" = "x86_64" ]; then
  objdump -d --no-show-raw-insn "$T/br.o" | awk '/<branchy>:/,/ret/' | grep -q "jle" || fail "branchy loop has no branch"
else
  echo "ch17 note: not x86_64, jle mnemonic check skipped"
fi
"$T/br" | tee ch17_branch_x86.out
awk '/^random/{r=$3/$6; if (r>3) ok=1} END{exit !ok}' ch17_branch_x86.out || fail "random: branchy not >3x slower"
awk '/^sorted/{r=$3/$6; if (r<3) ok=1} END{exit !ok}' ch17_branch_x86.out || fail "sorted: gap should be small"
[ "$(grep -o 'sums [0-9]* [0-9]*' ch17_branch_x86.out | awk '{print ($2==$3)}' | sort -u)" = "1" ] || fail "branch sums differ"

# 4. threaded SPSC ring, release/acquire: no value out of order
gcc -O2 -pthread ch17_spsc.c -o "$T/spsc"
"$T/spsc" | tee ch17_spsc.out
[ "$(grep -c ' 0 out of order' ch17_spsc.out)" = "2" ] || fail "spsc order"

# 5. tail latency: pool p99 must be far below malloc p99
gcc -O2 ch17_tail.c -o "$T/tail"; "$T/tail" | tee ch17_tail.out
awk '/^malloc/{m=$8} /^pool/{p=$8} END{exit !(m>3*p)}' ch17_tail.out || fail "malloc p99 not >3x pool p99"
echo "ch17 PASS: ring 0 mismatches + 255-slot capacity, branchy min is cmov on gcc, real-branch random/sorted gap, threaded SPSC in order, malloc tail >> pool tail"

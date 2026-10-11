#!/bin/bash
# test_ch03.sh -- assemble + run every ch03 RV32I program, verify real output.
set -e
cd "$(dirname "$0")"
python3 ch03_rv32asm.py ch03_sum.S > ch03_sum.hexout
python3 ch03_rv32sim.py ch03_sum.S    > ch03_sum.out     2> ch03_sum.count
python3 ch03_rv32sim.py ch03_sum_mem.S > ch03_sum_mem.out 2> ch03_sum_mem.count
python3 ch03_rv32sim.py ch03_arrsum.S > ch03_arrsum.out  2> ch03_arrsum.count
python3 ch03_rv32sim.py ch03_max.S    > ch03_max.out     2> ch03_max.count
grep -qx "55" ch03_sum.out
grep -qx "15" ch03_arrsum.out
grep -qx "42" ch03_max.out
grep -q "110 instructions" ch03_sum_mem.count
grep -q "57 instructions" ch03_sum.count
grep -q "00100293" ch03_sum.hexout
echo "ch03 PASS: 4 programs real-assembled, real-executed (55/15/42, 110v57 counts)"

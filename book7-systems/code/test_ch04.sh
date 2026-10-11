#!/bin/bash
# test_ch04.sh -- assemble+run fib, call-cost, inline; verify real output.
set -e
cd "$(dirname "$0")"
python3 ch03_rv32asm.py ch04_fib.S > /dev/null
python3 ch03_rv32sim.py ch04_fib.S       > ch04_fib.out    2> ch04_fib.count
python3 ch03_rv32sim.py ch04_callcost.S  > ch04_call.out  2> ch04_call.count
python3 ch03_rv32sim.py ch04_inline.S    > ch04_inline.out 2> ch04_inline.count
grep -qx "13" ch04_fib.out
grep -qx "A"  ch04_call.out
grep -qx "B"  ch04_inline.out
grep -q "565 instructions" ch04_fib.count
grep -q "410 instructions" ch04_call.count
grep -q "207 instructions" ch04_inline.count
grep -q "rv64i" ch04_switch_O2.s
echo "ch04 PASS: fib(7)=13 real frames; call tax 2instr; clang O0/O2 real"

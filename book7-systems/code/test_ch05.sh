#!/bin/bash
# test_ch05.sh -- rebuild + run the single-cycle core on its 13-word program.
set -e
cd "$(dirname "$0")"
iverilog -o ch05_sc_tb ch05_sc_tb.v ch05_rv32i_sc_top.v \
  ch05_rv32i_decode.v ch05_rv32i_regfile.v ch05_rv32i_alu.v
vvp ch05_sc_tb > ch05_sc.out 2>&1
grep -q "ch05 PASS" ch05_sc.out
grep -q "ok: a6" ch05_sc.out
grep -q "12 instrs retired in 12 cycles" ch05_sc.out
echo "ch05 PASS: single-cycle core ran 13-word program, 8 checks, CPI=1"

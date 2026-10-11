#!/bin/bash
# test_ch06.sh -- naive pipeline: dependent breaks, independent works.
set -e
cd "$(dirname "$0")"
iverilog -o ch06_pipe_tb ch06_pipe_tb.v ch06_rv32i_pipe_top.v \
  ch05_rv32i_decode.v ch05_rv32i_regfile.v ch05_rv32i_alu.v
vvp ch06_pipe_tb > ch06_pipe.out 2>&1
grep -q "a1=3 (want 8)" ch06_pipe.out
grep -q "a0..a4 = 1 2 3 4 5" ch06_pipe.out
echo "ch06 PASS: hazard SHOWN (a1=3), independent stream correct"

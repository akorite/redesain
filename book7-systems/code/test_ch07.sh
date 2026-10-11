#!/bin/bash
# test_ch07.sh -- forwarded core: dependent code now correct.
set -e
cd "$(dirname "$0")"
iverilog -o ch07_fwd_tb ch07_fwd_tb.v ch07_rv32i_fwd_top.v \
  ch05_rv32i_decode.v ch05_rv32i_regfile.v ch05_rv32i_alu.v
vvp ch07_fwd_tb > ch07_fwd.out 2>&1
grep -q "ch07 PASS" ch07_fwd.out
grep -q "a0=5 (5) a1=8 (8)" ch07_fwd.out
grep -q "1 stalls" ch07_fwd.out
echo "ch07 PASS: a1=8 forwarded, 1 load-use bubble, store forwarded"

#!/bin/sh
# ch09: rebuild + rerun adder4 and seg7 testbenches
set -e
cd "$(dirname "$0")"
iverilog -o /tmp/ch09_a4 ch09_full_adder.v ch09_adder4.v ch09_adder4_tb.v
vvp /tmp/ch09_a4 | grep -q "15 + 15 = (1,14)" || { echo "adder4 wrong"; exit 1; }
iverilog -o /tmp/ch09_s7 ch09_seg7.v ch09_seg7_tb.v
vvp /tmp/ch09_s7 | grep -q " 6 | 1011111" || { echo "seg7 wrong"; exit 1; }
echo "ch09 code OK"

#!/bin/sh
# ch12: rebuild + rerun all five classic-bug/self-check demos
set -e
cd "$(dirname "$0")"
iverilog -o /tmp/ch12_x ch12_xcounter.v ch12_xcounter_tb.v
vvp /tmp/ch12_x | grep -q "t=55 | no-rst q=xxxx | with-rst q=0100" || exit 1
iverilog -o /tmp/ch12_c ch12_caselatch.v ch12_caselatch_tb.v
vvp /tmp/ch12_c | grep -q "t=20 op=11 a= 7 b= 2 | latched= 5 safe= 0" || exit 1
iverilog -s race_bad_tb  -o /tmp/ch12_rb ch12_race.v ch12_race_tb.v
vvp /tmp/ch12_rb | grep -q "t=35 clk=1 d=0 q=1" || exit 1
iverilog -s race_good_tb -o /tmp/ch12_rg ch12_race.v ch12_race_tb.v
vvp /tmp/ch12_rg | grep -q "t=35 clk=1 d=1 q=1" || exit 1
iverilog -o /tmp/ch12_g ch12_shift.v ch12_golden_tb.v
vvp /tmp/ch12_g | grep -q "FAIL: 5 mismatches" || exit 1
iverilog -o /tmp/ch12_r ch12_report_tb.v
vvp /tmp/ch12_r | grep -q -- "--- tb done: 2 checks, 1 errors ---" || exit 1
echo "ch12 code OK"

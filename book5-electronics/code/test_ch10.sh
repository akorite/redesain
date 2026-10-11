#!/bin/sh
# ch10: rebuild + rerun dff demo, counter, traffic FSM, mm demo, seq101
set -e
cd "$(dirname "$0")"
iverilog -o /tmp/ch10_d ch10_dff.v ch10_dff_tb.v
vvp /tmp/ch10_d | grep -qE "t= +16 en=1 clk=1 d=1 | latch=1 ff=0" || exit 1
iverilog -o /tmp/ch10_c ch10_counter.v ch10_counter_tb.v
vvp /tmp/ch10_c | grep -q "t=155 en=1 | q=15 tc=1" || exit 1
iverilog -o /tmp/ch10_t ch10_traffic_fsm.v ch10_traffic_tb.v
vvp /tmp/ch10_t | grep -qE "t= +35 rst=0 state=2 | NS=10 EW=00" || exit 1
iverilog -o /tmp/ch10_m ch10_mm.v ch10_mm_tb.v
vvp /tmp/ch10_m | grep -qE "t= +15 x=1 | mealy=1 moore=0" || exit 1
iverilog -o /tmp/ch10_s ch10_seq101.v ch10_seq101_tb.v
vvp /tmp/ch10_s | grep -qE "t= +65 x=1 state=3 hit=1" || exit 1
echo "ch10 code OK"

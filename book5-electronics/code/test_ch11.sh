#!/bin/sh
# ch11: rebuild + rerun mux wrong-ways, counter self-check, traffic2, pipe, gen
set -e
cd "$(dirname "$0")"
iverilog -o /tmp/ch11_m ch11_mux4.v ch11_mux4_tb.v
vvp /tmp/ch11_m | grep -q "t=10 sel=1 a=0 b=1 | y1..4=1111 latch=0 stale=0" || exit 1
iverilog -o /tmp/ch11_c ch11_counter2.v ch11_counter2_tb.v
vvp /tmp/ch11_c | grep -q "PASS: all 3 checks" || exit 1
iverilog -o /tmp/ch11_cs -DSABOTAGE ch11_counter2.v ch11_counter2_tb.v
vvp /tmp/ch11_cs | grep -q "FAIL: 1 errors" || exit 1
iverilog -o /tmp/ch11_t ch11_traffic2.v ch11_traffic2_tb.v
vvp /tmp/ch11_t | grep -q "t=35 rst=0 | st=3 nx=0" || exit 1
iverilog -o /tmp/ch11_p ch11_pipe.v ch11_pipe_tb.v
vvp /tmp/ch11_p | grep -q "t=15 clk=1 d=1 | q_nb=0 q_block=1" || exit 1
iverilog -o /tmp/ch11_g ch11_gen.v ch11_gen_tb.v
vvp /tmp/ch11_g | grep -q "t=12 d=10110100 | q4=0100" || exit 1
echo "ch11 code OK"

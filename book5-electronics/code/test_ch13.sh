#!/bin/bash
# ch13: FPGA-flow demos must all still simulate and synthesize.
cd "$(dirname "$0")"
set -e
V=iverilog
$V -s blinky_tb -o /tmp/ch13_b ch13_blinky_tb.v
vvp /tmp/ch13_b | grep -q "cnt=1000 led=1"
$V -o /tmp/ch13_u ch13_uart_tx.v ch13_uart_tb.v
vvp /tmp/ch13_u | grep -q "PASS: UART frame decoded"
vvp /tmp/ch13_u | grep -q "decoded byte = 41"
$V -o /tmp/ch13_c ch13_counter_tb.v
vvp /tmp/ch13_c | grep -q "leds=000001 tc=1"
if command -v yosys >/dev/null; then
  yosys -Q -p "read_verilog ch13_blinky.v; synth_gowin -top blinky" | grep -q "Found and reported 0 problems"
fi
echo "ch13 code OK"

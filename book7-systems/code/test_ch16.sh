#!/bin/sh
# test_ch16.sh -- ch16 hardware self-check: assembler, core sims, UART.
set -e
cd "$(dirname "$0")"
echo "== assemble all three programs"
python3 ch16_asm8.py ch16_fib.asm  | tr ' ' '\n' > ch16_fib.hex
python3 ch16_asm8.py ch16_count.asm| tr ' ' '\n' > ch16_count.hex
python3 ch16_asm8.py ch16_mult.asm | tr ' ' '\n' > ch16_mult.hex
echo "== cpu8 Fibonacci run (expects 12 OUT bytes then HALT)"
iverilog -s cpu8_tb -o /tmp/c16fib ch16_cpu8.v ch15_regfile8.v ch14_alu8.v ch16_cpu8_tb.v
vvp /tmp/c16fib | tee /tmp/c16fib.log | grep -q "ALL CHECKS PASS"
echo "== cpu8 multiply run (expects OUT=42 then HALT)"
iverilog -s cpu8_mult_tb -DROMFILE='"ch16_mult.hex"' -o /tmp/c16mult ch16_cpu8.v ch15_regfile8.v ch14_alu8.v ch16_cpu8_mult_tb.v
vvp /tmp/c16mult | tee /tmp/c16mult.log | grep -q "printed 42"
echo "== uart_tx8 self-decoding bench"
iverilog -s uart_tb -o /tmp/c16ut ch16_uart_tx8.v ch16_uart_tb.v
vvp /tmp/c16ut | grep -q "PASS: UART"
echo "== lint the board top"
iverilog -tnull ch16_top_cpu9k.v ch16_cpu8.v ch15_regfile8.v ch14_alu8.v ch16_uart_tx8.v
echo "ch16 code OK"

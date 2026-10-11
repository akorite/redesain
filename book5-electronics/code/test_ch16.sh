#!/bin/bash
set -e; cd "$(dirname "$0")"; mkdir -p .build
iverilog -g2012 -o .build/cpu8_tb ch16_cpu8.v ch15_regfile8.v ch14_alu8.v ch16_cpu8_tb.v && vvp .build/cpu8_tb | tee .build/cpu8_tb.out
iverilog -g2012 -o .build/mult_tb ch16_cpu8.v ch15_regfile8.v ch14_alu8.v ch16_cpu8_mult_tb.v && vvp .build/mult_tb | tee .build/mult_tb.out
iverilog -g2012 -o .build/uart_tb ch16_uart_tx8.v ch16_uart_tb.v && vvp .build/uart_tb | tee .build/uart_tb.out
grep -qiE "FAIL| [1-9][0-9]* errors" .build/cpu8_tb.out .build/mult_tb.out .build/uart_tb.out && { echo FAIL; exit 1; }
echo "ch16 CPU testbenches PASS"

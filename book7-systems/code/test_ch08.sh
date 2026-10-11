#!/bin/bash
cd "$(dirname "$0")"
set -e
iverilog -o /tmp/ch08_soc_tb ch08_soc_tb.v ch08_rv32i_soc_top.v ch08_uart_tx.v ch05_rv32i_decode.v ch05_rv32i_regfile.v ch05_rv32i_alu.v
vvp /tmp/ch08_soc_tb | tee ch08_soc_tb.out
grep -q "ch08 PASS" ch08_soc_tb.out && echo "TEST_CH08 PASS"

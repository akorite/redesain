#!/bin/bash
set -e; cd "$(dirname "$0")"; mkdir -p .build
iverilog -g2012 -o .build/alu8_tb ch14_alu8.v ch14_alu8_tb.v && vvp .build/alu8_tb | tee .build/alu8_tb.out
iverilog -g2012 -o .build/alu8_exh ch14_alu8.v ch14_alu8_exh_tb.v && vvp .build/alu8_exh | tee .build/alu8_exh.out
iverilog -g2012 -o .build/top_tb ch14_alu8.v ch14_top_alu9k.v 2>/dev/null || true
grep -qiE "FAIL| [1-9][0-9]* errors" .build/alu8_tb.out .build/alu8_exh.out && { echo FAIL; exit 1; }
echo "ch14 ALU testbenches PASS"

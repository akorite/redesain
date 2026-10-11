#!/bin/bash
# ch15: register file, memories and the hand-driven datapath must all pass.
cd "$(dirname "$0")"
set -e
V=iverilog
$V -s regfile8_tb -o /tmp/ch15_r ch15_regfile8.v ch15_regfile8_tb.v
vvp /tmp/ch15_r | tee ch15_regfile8_tb.out | grep -q "PASS: regfile8 12 checks clean"
$V -s mem_tb -o /tmp/ch15_m ch15_rom.v ch15_ram.v ch15_mem_tb.v
vvp /tmp/ch15_m | tee ch15_mem_tb.out | grep -q "PASS: rom16 + ram16 8 checks clean"
$V -s datapath_tb -o /tmp/ch15_d ch14_alu8.v ch15_regfile8.v ch15_rom.v ch15_datapath.v ch15_datapath_tb.v
vvp /tmp/ch15_d | tee ch15_datapath_tb.out | grep -q "PASS: datapath executed 8 control-word steps clean"
if command -v yosys >/dev/null; then
  yosys -Q -p "read_verilog ch14_alu8.v ch15_regfile8.v ch15_rom.v ch15_ram.v ch15_datapath.v; synth_gowin -top datapath" | grep -q "Found and reported 0 problems"
fi
echo "ch15 code OK"

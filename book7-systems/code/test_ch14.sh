#!/bin/bash
# ch14: ALU vectors, exhaustive sweep, vector gen, and synth must all pass.
cd "$(dirname "$0")"
set -e
V=iverilog
python3 ch14_alu8_vec_gen.py > ch14_vec_gen.out
[ "$(wc -l < ch14_alu8_vectors.dat)" -eq 64 ]
$V -s alu8_tb -o /tmp/ch14_a ch14_alu8.v ch14_alu8_tb.v
vvp /tmp/ch14_a | tee ch14_alu8_tb.out | grep -q "PASS: all 64 vectors match"
$V -s alu8_exh_tb -o /tmp/ch14_e ch14_alu8.v ch14_alu8_exh_tb.v
vvp /tmp/ch14_e | tee ch14_alu8_exh_tb.out | grep -q "PASS: 131072 exhaustive vectors clean"
if command -v yosys >/dev/null; then
  yosys -Q -p "read_verilog ch14_alu8.v; synth_gowin -top alu8" | grep -q "Found and reported 0 problems"
  yosys -Q -p "read_verilog ch14_alu8.v ch14_top_alu9k.v; synth_gowin -top top_alu9k" | grep -q "Found and reported 0 problems"
fi
echo "ch14 code OK"

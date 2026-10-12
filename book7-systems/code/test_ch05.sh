#!/bin/bash
# test_ch05.sh -- the single-cycle core: fixed program, golden-model diff,
# immediate-generator cross-check, x0 mutation test, speed smoke test.
set -e
cd "$(dirname "$0")"
SRC="ch05_rv32i_decode.v ch05_rv32i_regfile.v ch05_rv32i_alu.v"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT

# 1. the 13-word program of the chapter (hand-checked state)
iverilog -o ch05_sc_tb ch05_sc_tb.v ch05_rv32i_sc_top.v $SRC
vvp ch05_sc_tb > ch05_sc.out 2>&1
grep -q "ch05 PASS" ch05_sc.out
grep -q "ok: a6" ch05_sc.out
grep -q "12 instrs retired in 12 cycles" ch05_sc.out

# 2. generic testbench vs the ch03 instruction-set simulator
iverilog -DSC -o ch05_run_sc ch05_run_tb.v ch05_rv32i_sc_top.v $SRC
for p in ch05_sum ch05_x0; do
  python3 ch05_golden.py $p.S $T/$p.hex > $T/$p.gold
  halt=$(sed -n 's/.*HALT=\([0-9]*\).*/\1/p' $T/$p.gold)
  I=$(sed -n 's/^I=\([0-9]*\).*/\1/p' $T/$p.gold)
  vvp ch05_run_sc +hex=$T/$p.hex +halt=$halt +cyc=100 | grep -v '\$finish' > $T/$p.hw
  diff <(grep -E '^[xm][0-9]+=' $T/$p.gold) <(grep -E '^[xm][0-9]+=' $T/$p.hw)
  grep -q "F=$I " $T/$p.hw        # CPI = 1: halt fetched after I cycles
  echo "  $p: state matches golden, F=I=$I"
done
cp $T/ch05_sum.hw ch05_sum.out
vvp ch05_run_sc +hex=ch05_prog.hex +halt=48 +cyc=30 +trace 2>/dev/null \
  | grep -v '\$finish' > ch05_trace.out

# 3. immediate generator: Verilog 'imm' wire == Python field decoder
python3 - <<'PY'
import re
from ch05_fields import decode
words = [int(l, 16) for l in open("ch05_prog.hex") if l.strip()]
n = 0
for l in open("ch05_trace.out"):
    m = re.match(r"T\s+\d+ pc=(\w+) insn=(\w+) imm=(\w+)", l)
    if not m: continue
    w = int(m.group(2), 16)
    fmt, name, rd, rs1, rs2, imm, wrong = decode(w)
    if imm is not None:
        assert (imm & 0xFFFFFFFF) == int(m.group(3), 16), (l, imm)
        n += 1
print("  immgen: %d immediates agree" % n)
PY
python3 ch05_fields.py ch05_prog.hex > ch05_fields.out
grep -q "sw .* 8 *12$" ch05_fields.out

# 4. mutation test: a regfile that lets x0 be written MUST be caught
sed -e "s/(ra1 == 5'd0) ? 32'd0 ://; s/(ra2 == 5'd0) ? 32'd0 ://" \
    -e "s/if (we \&\& wa != 5'd0)/if (we)/" ch05_rv32i_regfile.v > $T/rf_mut.v
iverilog -DSC -o $T/mut ch05_run_tb.v ch05_rv32i_sc_top.v ch05_rv32i_decode.v $T/rf_mut.v ch05_rv32i_alu.v
vvp $T/mut +hex=$T/ch05_x0.hex +halt=20 +cyc=30 | grep -v '\$finish' > ch05_x0_mutant.out
if diff -q <(grep -E '^[xm][0-9]+=' $T/ch05_x0.gold) <(grep -E '^[xm][0-9]+=' ch05_x0_mutant.out) >/dev/null; then
  echo "ch05 FAIL: x0 mutant was not detected"; exit 1; fi
cp $T/ch05_x0.hw ch05_x0.out

# 5. the 2000-cycle spin loop: finishes (it once hung on a combinational loop)
iverilog -o ch05_spin_tb ch05_spin_tb.v ch05_rv32i_sc_top.v $SRC
timeout 20 vvp ch05_spin_tb 2>/dev/null | grep -q "sim ran 2000 cycles"
vvp ch05_run_sc +hex=ch05_spin.hex +halt=9999 +cyc=2000 2>/dev/null | grep -q "x10=0000011d"

echo "ch05 PASS: 13-word program, golden diff (sum 1..10, x0), immgen cross-check, x0 mutant caught, CPI=1"

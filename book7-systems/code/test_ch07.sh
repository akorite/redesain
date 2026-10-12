#!/bin/bash
# test_ch07.sh -- forwarded core: golden diff, cycle formula, and three
# mutants (no stall, wrong forwarding priority, no squash) that must FAIL.
set -e
cd "$(dirname "$0")"
SRC="ch05_rv32i_decode.v ch05_rv32i_regfile.v ch05_rv32i_alu.v"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
iverilog -o ch07_fwd_tb ch07_fwd_tb.v ch07_rv32i_fwd_top.v $SRC
vvp ch07_fwd_tb > ch07_fwd.out 2>&1
grep -q "ch07 PASS" ch07_fwd.out
grep -q "a0=5 (5) a1=8 (8)" ch07_fwd.out
grep -q "1 stalls" ch07_fwd.out

iverilog -o ch07_run ch05_run_tb.v ch07_rv32i_fwd_top.v $SRC
st() { grep -E '^[xm][0-9]+=' "$1"; }
gold() { python3 ch05_golden.py $1.S $T/$1.hex > $T/$1.gold
         halt=$(sed -n 's/.*HALT=\([0-9]*\).*/\1/p' $T/$1.gold)
         I=$(sed -n 's/^I=\([0-9]*\).*/\1/p' $T/$1.gold); }
run() { vvp "$1" +hex=$T/$2.hex +halt=$halt +cyc=${3:-120} +nret=${4:-0} | grep -v '\$finish' > $T/$2.$5hw; }

# every program: final state == golden model
for p in ch06_dep ch06_indep ch05_sum ch07_prio ch07_br; do
  gold $p; run ./ch07_run $p
  diff <(st $T/$p.gold) <(st $T/$p.hw)
done
# cycle formula: F = I + stalls + 2*taken-branches
gold ch05_sum; run ./ch07_run ch05_sum
F=$(sed -n 's/.*F=\([0-9]*\) .*/\1/p' $T/ch05_sum.hw)
S=$(sed -n 's/.*stalls=\([0-9]*\).*/\1/p' $T/ch05_sum.hw)
K=$(sed -n 's/.*taken=\([0-9]*\).*/\1/p' $T/ch05_sum.hw)
[ "$F" -eq $((I + S + 2*K)) ] && [ "$S" -eq 1 ] && [ "$K" -eq 9 ] && [ "$F" -eq 56 ]
cp $T/ch05_sum.hw ch07_sum.out
gold ch07_br; run ./ch07_run ch07_br
grep -q "F=6 " $T/ch07_br.hw; cp $T/ch07_br.hw ch07_br.out
gold ch06_indep; run ./ch07_run ch06_indep 60 8
grep -q "F=8 .*lastret=12" $T/ch06_indep.hw
cp $T/ch06_indep.hw ch07_indep.out

# exercise programs: two bubbles; a false stall; the same without it; loop bound 6
gold ch07_stall2; run ./ch07_run ch07_stall2; diff <(st $T/ch07_stall2.gold) <(st $T/ch07_stall2.hw)
grep -q "stalls=2" $T/ch07_stall2.hw
gold ch07_false10; run ./ch07_run ch07_false10; diff <(st $T/ch07_false10.gold) <(st $T/ch07_false10.hw)
grep -q "stalls=1" $T/ch07_false10.hw          # independent, yet stalled
gold ch07_false11; run ./ch07_run ch07_false11; diff <(st $T/ch07_false11.gold) <(st $T/ch07_false11.hw)
grep -q "stalls=0" $T/ch07_false11.hw
gold ch07_gap; run ./ch07_run ch07_gap; diff <(st $T/ch07_gap.gold) <(st $T/ch07_gap.hw)
grep -q "stalls=0" $T/ch07_gap.hw
sed 's/li   t2, 11 /li   t2, 6  /' ch05_sum.S > $T/sum6.S
python3 ch05_golden.py $T/sum6.S $T/sum6.hex > $T/sum6.gold
I6=$(sed -n 's/^I=\([0-9]*\).*/\1/p' $T/sum6.gold)
vvp ch07_run +hex=$T/sum6.hex +halt=40 +cyc=100 | grep -v '\$finish' > $T/sum6.hw
diff <(st $T/sum6.gold) <(st $T/sum6.hw)
[ "$I6" -eq 22 ] && grep -q "F=31 stalls=1 taken=4" $T/sum6.hw
cp $T/ch07_false10.hw ch07_false10.out

# mutant 1: remove the load-use stall -> must give a WRONG a1
sed "s/^  assign stall = idex_memread \&\&/  assign stall = 1'b0 \&\& idex_memread \&\&/" ch07_rv32i_fwd_top.v > $T/m1.v
iverilog -o $T/m1 ch05_run_tb.v $T/m1.v $SRC
gold ch05_sum; run $T/m1 ch05_sum 120 0 m1.
! diff -q <(st $T/ch05_sum.gold) <(st $T/ch05_sum.m1.hw) >/dev/null
cp $T/ch05_sum.m1.hw ch07_nostall.out
# mutant 2: MEM/WB checked before EX/MEM -> stale writer wins
python3 - "$T" <<'PY'
import re, sys
s = open("ch07_rv32i_fwd_top.v").read()
for r in ("1", "2"):
    pat = re.compile(r"(wire \[31:0\] fwd%s = )\((exmem_regwrite[^)]*?)\)\s*\? exmem_wb :\s*\((memwb_regwrite[^)]*?)\)\s*\? wbdata : (idex_rd%s);" % ("A" if r=="1" else "B", r))
    s, n = pat.subn(r"\1(\3) ? wbdata : (\2) ? exmem_wb : \4;", s)
    assert n == 1, n
open(sys.argv[1] + "/m2.v", "w").write(s)
PY
iverilog -o $T/m2 ch05_run_tb.v $T/m2.v $SRC
gold ch07_prio; run $T/m2 ch07_prio 60 0 m2.
! diff -q <(st $T/ch07_prio.gold) <(st $T/ch07_prio.m2.hw) >/dev/null
cp $T/ch07_prio.m2.hw ch07_prio_mutant.out
# mutant 3: redirect the pc but do not squash the wrong-path slots
sed -e "s/if (rst || stall || flush) begin/if (rst || stall) begin/" \
    -e "s/ifid_insn <= flush ? 32'h00000013 : insn_f;.*/ifid_insn <= insn_f;/" ch07_rv32i_fwd_top.v > $T/m3.v
iverilog -o $T/m3 ch05_run_tb.v $T/m3.v $SRC
gold ch07_br; run $T/m3 ch07_br 60 0 m3.
! diff -q <(st $T/ch07_br.gold) <(st $T/ch07_br.m3.hw) >/dev/null
cp $T/ch07_br.m3.hw ch07_br_mutant.out
echo "ch07 PASS: 5 programs match golden; F = I + stalls + 2*taken (56 = 37+1+18); 3 mutants caught"

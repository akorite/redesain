#!/bin/bash
# test_ch06.sh -- naive pipeline: dependent code is WRONG, independent code
# is right, and a 5-stage pipe needs I+4 cycles for I independent writers.
set -e
cd "$(dirname "$0")"
SRC="ch05_rv32i_decode.v ch05_rv32i_regfile.v ch05_rv32i_alu.v"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
iverilog -o ch06_pipe_tb ch06_pipe_tb.v ch06_rv32i_pipe_top.v $SRC
vvp ch06_pipe_tb > ch06_pipe.out 2>&1
grep -q "a1=3 (want 8)" ch06_pipe.out
grep -q "a0..a4 = 1 2 3 4 5" ch06_pipe.out

iverilog -DPIPE -o ch06_run ch05_run_tb.v ch06_rv32i_pipe_top.v $SRC
run() {  # run <prog> <nret>
  python3 ch05_golden.py $1.S $T/$1.hex > $T/$1.gold
  halt=$(sed -n 's/.*HALT=\([0-9]*\).*/\1/p' $T/$1.gold)
  vvp ch06_run +hex=$T/$1.hex +halt=$halt +cyc=60 +nret=$2 | grep -v '\$finish' > $T/$1.hw
}
# independent: matches the golden model; last of 8 writers retires at edge 12
run ch06_indep 8
diff <(grep -E '^[xm][0-9]+=' $T/ch06_indep.gold) <(grep -E '^[xm][0-9]+=' $T/ch06_indep.hw)
grep -q "lastret=12" $T/ch06_indep.hw
cp $T/ch06_indep.hw ch06_indep.out
# dependent: MUST differ from golden (a1=3, a2=0, a3 and mem[0] stay 0)
run ch06_dep 4
if diff -q <(grep -E '^[xm][0-9]+=' $T/ch06_dep.gold) <(grep -E '^[xm][0-9]+=' $T/ch06_dep.hw) >/dev/null; then
  echo "ch06 FAIL: dependent code unexpectedly correct"; exit 1; fi
grep -q "^x11=00000003" $T/ch06_dep.hw
! grep -q "^x12=" $T/ch06_dep.hw
cp $T/ch06_dep.hw ch06_dep.out; cp $T/ch06_dep.gold ch06_dep.gold
# padding fixes it: two pads per dependent hand-off
run ch06_dep_nops 4
diff <(grep -E '^[xm][0-9]+=' $T/ch06_dep_nops.gold) <(grep -E '^[xm][0-9]+=' $T/ch06_dep_nops.hw)
# two loads then a use: a2 stays 0
run ch06_two 3
! grep -q "^x12=" $T/ch06_two.hw
grep -q "^x10=00000005" $T/ch06_two.hw
echo "ch06 PASS: hazard SHOWN (a1=3, a2=0), independent stream correct, 8 writers retire by edge 12"

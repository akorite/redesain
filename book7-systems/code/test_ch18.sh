#!/bin/bash
# test_ch18.sh -- run the chapter's VM and compiler and check every claimed output.
cd "$(dirname "$0")"
set -e
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
fail(){ echo "ch18 FAIL: $1"; exit 1; }

# 1. the original VM: 50, then 3 2 1 0, 28 dispatches
gcc -O2 ch18_vm.c -o "$T/vm"; "$T/vm" | tee ch18_vm.out
[ "$(tr '\n' ' ' < ch18_vm.out)" = "50 3 2 1 0 instructions executed: 28 " ] || fail "ch18_vm output"

# 2. the bytecode loader gives the same answer; the fixed countdown has no stray 0
gcc -O2 -Wall ch18_vmrun.c -o "$T/vmrun"
timeout 10 "$T/vmrun" < ch18_count.bc | tee ch18_count.out
[ "$(tr '\n' ' ' < ch18_count.out)" = "50 3 2 1 0 instructions executed: 28 " ] || fail "count.bc"
timeout 10 "$T/vmrun" < ch18_count_fixed.bc | tee ch18_count_fixed.out
[ "$(tr '\n' ' ' < ch18_count_fixed.out)" = "3 2 1 instructions executed: 20 " ] || fail "fixed countdown"
echo "1 6 1 7 4 1 8 2 0" | "$T/vmrun" -t | tee ch18_trace.out
grep -q "5  ip=7   ADD       stack before: 42 8" ch18_trace.out || fail "trace"
# bounds checks
echo "1 1 1 0 5 0" | "$T/vmrun" | grep -q "divide by zero" || fail "div0 check"
echo "6 6 6" | "$T/vmrun" | grep -q "stack underflow" || fail "underflow check"
python3 -c "print('1 1 '*300 + '0')" | "$T/vmrun" | grep -q "stack overflow" || fail "overflow check"

# 3. the compiler: precedence, folding, VM run, RV32 code
[ "$(python3 ch18_expr.py --target ast '2+3*4')" = "$(printf '(2 + (3 * 4))\nvalue: 14')" ] || fail "precedence"
[ "$(python3 ch18_expr.py --naive --target ast '2+3*4' | tail -1)" = "value: 20" ] || fail "naive should give 20"
python3 ch18_expr.py --target vmlist '(6+7)*8' | tee ch18_expr_vmlist.out
python3 ch18_expr.py --target rv32 '(6+7)*8' | tee ch18_expr_rv32.out
python3 ch18_expr.py --fold --target rv32 '(6+7)*8' | tee ch18_expr_rv32_fold.out
grep -q "li   t0, 104" ch18_expr_rv32_fold.out || fail "fold"
for e in '(6+7)*8' '6*7+8' '10-3-2' '2+3*4' '100/7/2' '((1+2)*(3+4))-5*(6-2)' '7-10'; do
  want=$(python3 -c "
import sys; sys.path.insert(0,'.')
import ch18_expr as c; print(c.evaluate(c.Parser(c.tokenize('$e')).parse()))")
  got=$(python3 ch18_expr.py --target vm "$e" | "$T/vmrun" | head -1)
  [ "$want" = "$got" ] || fail "VM result for $e: want $want got $got"
done
# C semantics cross-check for the same expressions
cat > "$T/c.c" <<'C'
#include <stdio.h>
int main(void){printf("%d %d %d %d %d %d %d\n",(6+7)*8,6*7+8,10-3-2,2+3*4,100/7/2,((1+2)*(3+4))-5*(6-2),7-10);return 0;}
C
gcc "$T/c.c" -o "$T/c"
mine=$(for e in '(6+7)*8' '6*7+8' '10-3-2' '2+3*4' '100/7/2' '((1+2)*(3+4))-5*(6-2)' '7-10'; do python3 ch18_expr.py --target vm "$e" | "$T/vmrun" | head -1; done | tr '\n' ' ')
[ "$mine" = "$("$T/c") " ] || fail "differs from gcc: $mine"
# + and - programs run on the Book's own RV32I simulator (ch03)
python3 ch18_expr.py --target rv32 '(9-4)+(7-5)' > "$T/e.S"
a0=$(python3 -c "
import sys; sys.path.insert(0,'.')
from ch03_rv32asm import assemble
from ch03_rv32sim import CPU
c=CPU([w for _,w,_ in assemble(open('$T/e.S').read().splitlines())]).run(); print(c.x[10], c.steps)")
[ "$a0" = "7 8" ] || fail "rv32 sim result '$a0'"
# * program assembles as RV32IM (clang) and contains a mul
XCLANG=clang
command -v /opt/homebrew/opt/llvm/bin/clang >/dev/null && XCLANG=/opt/homebrew/opt/llvm/bin/clang
if ! echo 'nop' | "$XCLANG" --target=riscv32 -march=rv32im -mabi=ilp32 -c -x assembler - -o "$T/probe.o" 2>/dev/null; then
  echo "ch18 note: clang lacks riscv32 backend, rv32 object check skipped"
else
python3 ch18_expr.py --target rv32 '(6+7)*8' | "$XCLANG" --target=riscv32 -march=rv32im -mabi=ilp32 -c -x assembler - -o "$T/m.o"
OBJDUMP=$(command -v llvm-objdump || command -v /opt/homebrew/opt/llvm/bin/llvm-objdump || echo objdump)
"$OBJDUMP" -d "$T/m.o" | tee ch18_expr_rv32_objdump.out | grep -q "mul" || fail "no mul"
grep -qE "b3 82 62 02|026282b3" ch18_expr_rv32_objdump.out || fail "mul encoding"
fi

# 4. cost of interpretation (timing: loose bounds)
gcc -O2 ch18_vm_bench.c -o "$T/vb"; "$T/vb" | tee ch18_vm_bench.out
awk '/VM \/ native/{gsub("x","",$5); gsub("x","",$10); if ($5+0>3 && $10+0>2) ok=1} END{exit !ok}' ch18_vm_bench.out || fail "VM not >3x native(register)"
echo "ch18 PASS: VM 50/3 2 1 0/28 dispatches, fixed countdown 3 2 1/20, bounds checks, compiler matches gcc on 7 expressions, RV32 runs on ch03 sim and assembles as RV32IM, VM several times slower than native"

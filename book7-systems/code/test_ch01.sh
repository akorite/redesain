#!/bin/bash
# test_ch01.sh -- rebuild every ch01 artifact and verify real outputs.
set -e
cd "$(dirname "$0")"
CLANG="clang -target x86_64-linux-gnu"
LD=/opt/homebrew/bin/ld.lld
$CLANG -O0 -c ch01_sum.c -o ch01_sum.o
$CLANG -O2 -c ch01_sum.c -o ch01_sum_O2.o
$CLANG -O0 -c ch01_broken.c -o ch01_broken.o
$CLANG -c ch01_asm.S -o ch01_asm.o
$CLANG -c ch01_start.S -o ch01_start.o
$CLANG -S -O0 ch01_sum.c -o ch01_sum.s
$LD -o ch01_sum.elf ch01_start.o ch01_sum.o
objdump -h ch01_sum.o | grep -E "text|data" > ch01_sizes.out
objdump -h ch01_sum_O2.o | grep -E "text|data" >> ch01_sizes.out
objdump -d ch01_sum.o | sed -n '/<main>:/,/retq/p' | head -18 > ch01_main_disasm.out
objdump -r ch01_broken.o | head -14 > ch01_reloc.out
if $LD -o ch01_broken.elf ch01_broken.o 2> ch01_link_err.out; then
  echo "FAIL: link should have failed" >&2; exit 1
fi
grep -q "undefined symbol: missing" ch01_link_err.out || { echo "FAIL: no missing-symbol error"; exit 1; }
file ch01_sum.elf | grep -q "ELF 64-bit" || { echo "FAIL: not ELF"; exit 1; }
grep -q "callq" ch01_main_disasm.out || { echo "FAIL: disasm truncated"; exit 1; }
grep -q "R_X86_64_PLT32.*missing" ch01_reloc.out || { echo "FAIL: reloc table wrong"; exit 1; }
echo "ch01 PASS: ELF objects, linked executable, missing-symbol error all real"

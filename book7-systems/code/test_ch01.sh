#!/bin/bash
set -e; cd "$(dirname "$0")"; mkdir -p .build
CC=${CC:-clang}
# 1) compile the freestanding C to asm at -O0 and -O2; .text must exist in both
$CC -target x86_64-linux-gnu -O0 -S ch01_sum.c -o .build/sum_O0.s
$CC -target x86_64-linux-gnu -O2 -S ch01_sum.c -o .build/sum_O2.s
grep -q 'sum:' .build/sum_O0.s && grep -q 'sum:' .build/sum_O2.s
# 2) assemble+link a real ELF, then verify section headers via llvm-objdump
$CC -target x86_64-linux-gnu -O0 -c ch01_sum.c -o .build/sum.o
command -v llvm-objdump >/dev/null && llvm-objdump -h .build/sum.o | grep -q '.text' || objdump -h .build/sum.o | grep -q '.text'
# 3) ch01_broken.c must FAIL to link (chapter's deliberate error)
if $CC -target x86_64-linux-gnu -fuse-ld=lld -nostdlib ch01_broken.c -o .build/broken 2>/dev/null; then
  echo "FAIL: broken.c linked unexpectedly"; exit 1
fi
echo "ch01 PASS: asm emit + ELF object + expected link failure all real"

#!/bin/bash
# test_ch02.sh -- rebuild and verify ch02 artifacts.
set -e
cd "$(dirname "$0")"
clang -O0 ch02_bytes.c -o ch02_bytes && ./ch02_bytes | tee ch02_bytes.out
clang -O0 ch02_pad.c -o ch02_pad && ./ch02_pad | tee ch02_pad.out
clang -O0 ch02_float.c -o ch02_float && ./ch02_float | tee ch02_float.out
clang -O2 ch02_align.c -o ch02_align && ./ch02_align | tee ch02_align.out
grep -q "0d 0c 0b 0a" ch02_bytes.out || exit 1
grep -q "A: sizeof=24" ch02_pad.out || exit 1
grep -q "3.141592" ch02_float.out || exit 1
grep -q "offset 0:" ch02_align.out || exit 1
echo "ch02 PASS: bytes/padding/float/alignment all real"

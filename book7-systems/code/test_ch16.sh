#!/bin/bash
# test_ch16.sh -- build and run every ch16 program on x86_64 and check the claims.
# Timing checks use deliberately loose thresholds (shared container, noisy).
cd "$(dirname "$0")"
set -e
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
fail(){ echo "ch16 FAIL: $1"; exit 1; }

# 1. SAXPY: scalar baseline (vectoriser off) vs SSE2 vs AVX2 intrinsics
if [ "$(uname -m)" = "x86_64" ]; then
gcc -O3 -fno-tree-vectorize -mavx2 ch16_saxpy_x86.c -o "$T/sx_novec"
gcc -O3 -mavx2 ch16_saxpy_x86.c -o "$T/sx_vec"
"$T/sx_novec" 25 | tee ch16_saxpy_x86_novec.out
"$T/sx_vec"   25 | tee ch16_saxpy_x86_vec.out
grep -q "correctness (n=1003, ragged tail): ok" ch16_saxpy_x86_novec.out || fail "saxpy kernels disagree"
# AVX2 must beat the honest scalar baseline by >1.5x at n=2^16 (in-cache); got ~4-6x
awk '$1=="2^16"{gsub("x","",$6); if ($6+0>1.5) ok=1} END{exit !ok}' ch16_saxpy_x86_novec.out || fail "avx2 speedup at 2^16 below 1.5x"
# at n=2^25 (memory-bound) the gap must collapse below 2x
awk '$1=="2^25"{gsub("x","",$6); if ($6+0<2.0) ok=1} END{exit !ok}' ch16_saxpy_x86_novec.out || fail "2^25 not bandwidth-bound?"
else
  echo "ch16 note: not x86_64, AVX2 saxpy checks skipped"
fi

# 2. the loop-tail bug: fixed version exact, naive version caught by AddressSanitizer
if [ "$(uname -m)" = "x86_64" ]; then
gcc -g -fsanitize=address ch16_tail.c -o "$T/tail"
"$T/tail" fixed | tee ch16_tail_fixed.out
[ "$(cat ch16_tail_fixed.out)" = "1 3 5 7 9 11 13 15 17 19 " ] || fail "tail fixed output"
if "$T/tail" naive > ch16_tail_naive.out 2>&1; then fail "naive tail loop not flagged"; fi
grep -q "heap-buffer-overflow" ch16_tail_naive.out || fail "ASan message missing"
else
  echo "ch16 note: not x86_64, emmintrin tail checks skipped"
fi

# 3. AoS vs SoA
gcc -O3 ch16_soa_x86.c -o "$T/soa"
"$T/soa" | tee ch16_soa_x86.out
awk '/ratio AoS\/SoA/{gsub("x","",$4); if ($4+0>1.5) ok=1} END{exit !ok}' ch16_soa_x86.out || fail "SoA ratio < 1.5"

# 4. saturating add: identical output, intrinsic version faster
if [ "$(uname -m)" = "x86_64" ]; then
gcc -O3 ch16_satadd.c -o "$T/sat"
"$T/sat" | tee ch16_satadd.out
grep -q "outputs identical: yes" ch16_satadd.out || fail "satadd mismatch"
awk '/speedup/{for(i=1;i<=NF;i++) if($i=="speedup"){v=$(i+1); gsub("x","",v); if (v+0>1.2) ok=1}} END{exit !ok}' ch16_satadd.out || fail "satadd speedup"
else
  echo "ch16 note: not x86_64, SSE2 satadd checks skipped"
fi
echo "ch16 PASS: saxpy x86 (SSE2/AVX2 vs scalar, correct on ragged n), tail bug caught by ASan, SoA > AoS, satadd identical + faster"

#!/bin/sh
# Test for code/crt_solver.py: brute and constructive agree at 23 mod 105.
out=$(python3 "$(dirname "$0")/crt_solver.py")
echo "$out" | grep -q "brute force scan: \[23\]" || { echo "FAIL: brute"; exit 1; }
echo "$out" | grep -q "x == 8 (mod 15)" || { echo "FAIL: fold1"; exit 1; }
echo "$out" | grep -q "x == 23 (mod 105)" || { echo "FAIL: final"; exit 1; }
echo "test_07_crt: PASS"

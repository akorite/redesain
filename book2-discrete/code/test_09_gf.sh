#!/bin/sh
out=$(python3 "$(dirname "$0")/gf_coin.py")
echo "$out" | grep -qF "[x^30] by GF:  5" || { echo "FAIL: gf"; exit 1; }
echo "$out" | grep -qF "[x^30] by brute force: 5" || { echo "FAIL: brute"; exit 1; }
echo "test_09_gf: PASS"

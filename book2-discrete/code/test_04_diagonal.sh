#!/bin/sh
# Test for code/diagonal_demo.py: 8 marked rows, constructed number 0.45555555...
out=$(python3 "$(dirname "$0")/diagonal_demo.py")
echo "$out" | grep -q "constructed: 0.45555555" || { echo "FAIL: value"; exit 1; }
[ "$(echo "$out" | grep -c '\[')" = "8" ] || { echo "FAIL: marks"; exit 1; }
echo "test_04_diagonal: PASS"

#!/bin/sh
out=$(python3 "$(dirname "$0")/count_check.py")
echo "$out" | grep -q "enum=16  closed=2^4=16" || { echo "FAIL: subsets"; exit 1; }
echo "$out" | grep -q "enum=10  closed=C(5,3)=10" || { echo "FAIL: paths"; exit 1; }
echo "$out" | grep -q "enum=84  closed=C(9,3)=84" || { echo "FAIL: stars"; exit 1; }
echo "test_08_count: PASS"

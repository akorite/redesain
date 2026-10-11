#!/bin/sh
out=$(python3 "$(dirname "$0")/fixed_points.py")
echo "$out" | grep -q "estimated E\[fixed points\] = 1.0048" || { echo "FAIL"; exit 1; }
echo "$out" | grep -q "exact value               = 1 " || { echo "FAIL"; exit 1; }
echo "test_12_fixed: PASS"

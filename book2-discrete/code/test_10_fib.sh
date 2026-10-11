#!/bin/sh
out=$(python3 "$(dirname "$0")/fib_closed.py")
echo "$out" | grep -q "first float failure at n = 71" || { echo "FAIL: binet break"; exit 1; }
echo "$out" | grep -q " 20 | 6765 |" || { echo "FAIL: F20"; exit 1; }
echo "test_10_fib: PASS"

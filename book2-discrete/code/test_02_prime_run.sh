#!/bin/sh
# Test for code/check_prime_run.py: verifies the streak and the first composite.
out=$(python3 "$(dirname "$0")/check_prime_run.py")
echo "$out" | grep -q "x = 0..39: all prime (40 consecutive values)" || { echo "FAIL: streak"; exit 1; }
echo "$out" | grep -q "x = 40: f(40) = 1681 = 41 \* 41  <-- first composite" || { echo "FAIL: first composite"; exit 1; }
echo "$out" | grep -q "4 composites in x = 0..50" || { echo "FAIL: count"; exit 1; }
echo "test_02_prime_run: PASS"

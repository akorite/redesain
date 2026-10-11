#!/bin/sh
# Test for code/powers_cycle.py: 7 mod 100 -> period 4, answer 49;
# 3 mod 7 -> period 6, answer 4.
out=$(python3 "$(dirname "$0")/powers_cycle.py")
echo "$out" | grep -q "period = 4" || { echo "FAIL: period"; exit 1; }
echo "$out" | grep -q "7\^2026 mod 100 = 7\^2 mod 100 = 49" \
    || { echo "FAIL: 7^2026"; exit 1; }
python3 "$(dirname "$0")/powers_cycle.py" 3 7 | grep -q "period = 6" \
    || { echo "FAIL: 3 mod 7"; exit 1; }
echo "test_06_powers: PASS"

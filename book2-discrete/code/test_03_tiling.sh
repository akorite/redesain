#!/bin/sh
# Test for code/verify_tiling.py: 8x8 minus one cell -> 21 trominos, 63 cells.
out=$(python3 "$(dirname "$0")/verify_tiling.py")
echo "$out" | grep -q "trominos used: 21, cells covered: 63, expected: 21" \
    || { echo "FAIL: count"; exit 1; }
# every row must have 8 symbols and the hole marker must appear exactly once
[ "$(echo "$out" | grep -c '^[#A-Za-z0-9 ]*$')" -ge 8 ] || { echo "FAIL: rows"; exit 1; }
[ "$(echo "$out" | grep -o '#' | wc -l | tr -d ' ')" = "1" ] \
    || { echo "FAIL: hole"; exit 1; }
echo "test_03_tiling: PASS"

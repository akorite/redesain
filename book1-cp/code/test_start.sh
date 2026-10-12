#!/bin/bash
# Checks the two programs quoted in "Start here" against the output printed in the book.
set -e
cd "$(dirname "$0")/start"
g++ -std=c++17 -O0 -o /tmp/first_program first_program.cpp
out=$(printf '5\n30 10 50 20 40\n' | /tmp/first_program)
exp=$'sum = 150\nsmallest = 10, largest = 50'
[ "$out" = "$exp" ] || { echo "FAIL first_program"; exit 1; }
g++ -std=c++17 -O0 -o /tmp/overflow overflow.cpp
[ "$(/tmp/overflow)" = "-294967296 4000000000" ] || { echo "FAIL overflow"; exit 1; }
echo "test_start: ok"
# The binary-search first-attempt programs (Chapter 4).
cd ../first_attempts
g++ -std=c++17 -O0 -o /tmp/bs_naive bs_naive.cpp && /tmp/bs_naive | tail -1 | grep -q "stuck: never terminates" || { echo "FAIL bs_naive"; exit 1; }
g++ -std=c++17 -O0 -o /tmp/bs_fixed bs_fixed.cpp && [ "$(/tmp/bs_fixed | tail -1)" = "first index with a[i] >= 6: 3 (value 7)" ] || { echo "FAIL bs_fixed"; exit 1; }
echo "test_start (first attempts): ok"

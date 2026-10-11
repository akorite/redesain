#!/bin/sh
# Test for code/bezout.py: gcd=18, Bezout 4*252 - 5*198, family checks 30.
out=$(python3 "$(dirname "$0")/bezout.py")
echo "$out" | grep -q "^gcd = 18" || { echo "FAIL: gcd"; exit 1; }
echo "$out" | grep -q "Bezout: 18 = 4\*252 + -5\*198  (check 18)" \
    || { echo "FAIL: bezout"; exit 1; }
[ "$(echo "$out" | grep -c 'check 12x+18y = 30')" = "3" ] \
    || { echo "FAIL: family"; exit 1; }
echo "test_05_bezout: PASS"

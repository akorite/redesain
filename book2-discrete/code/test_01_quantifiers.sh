#!/bin/sh
# Chapter 1: verify_quantifiers.py must run and disagree on the two claims in world 1.
out="$(python3 "$(dirname "$0")/verify_quantifiers.py")" || exit 1
printf '%s\n' "$out"
echo "$out" | grep -q "every contestant solved some problem : True" || exit 1
echo "$out" | grep -q "some problem was solved by everyone  : False" || exit 1
echo "test_01_quantifiers: PASS"

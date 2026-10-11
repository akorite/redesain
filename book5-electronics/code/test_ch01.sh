#!/bin/sh
# test_ch01.sh -- Chapter 1 checks: the chapter's scripts run and produce
# the outputs the book prints. Run by `make test`.
cd "$(dirname "$0")" || exit 1

sh check_tools.sh >/dev/null 2>&1 || { echo "FAIL: check_tools.sh exit"; exit 1; }
sh check_tools.sh | grep -q "found\|MISSING" \
  || { echo "FAIL: check_tools.sh produced no status lines"; exit 1; }

out=$(python3 prefix.py) || { echo "FAIL: prefix.py exit"; exit 1; }
echo "$out" | grep -q "0.0047  ->  4.7 m" || { echo "FAIL: 4.7 m"; exit 1; }
echo "$out" | grep -q "1e-07  ->  100 n"  || { echo "FAIL: 100 n"; exit 1; }
echo "$out" | grep -q "0.02  ->  20 m"    || { echo "FAIL: 20 m"; exit 1; }
echo "$out" | grep -q "3.3  ->  3.3"      || { echo "FAIL: 3.3 bare"; exit 1; }

echo "ch01 tests: PASS"

#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
python3 harness_test.py | grep -q "ALL PASS"
python3 run_sma.py | grep -q "trades 15"
python3 run_sma.py | grep -q "SMA20/60: ret +7.9%"
python3 lookahead_bug.py | grep -q "ret +1343%"
python3 lookahead_bug.py | grep -q "ret -52.1%"
echo "ALL ch08 CHECKS PASS"

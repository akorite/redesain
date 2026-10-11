#!/usr/bin/env bash
set -e; cd "$(dirname "$0")"
python3 sharpe_se.py | grep -q "T=2520 days  se(SR)~0.024"
python3 sharpe_se.py | grep -q "empirical se over 2000 sims (T=252): 1.012"
python3 metrics_demo.py | grep -q "sharpe +1.49"
python3 tail_demo.py | grep -q "skew -4.30"
echo "ALL ch12 CHECKS PASS"

#!/usr/bin/env bash
set -e; cd "$(dirname "$0")"
python3 many_tests.py | grep -q "best in-sample sharpe: +1.80"
python3 many_tests.py | grep -q "E\[max sharpe\] under H0 ~ +2.40"
python3 fit_grid.py | grep -q "SMA(46,56) sharpe +1.04"
python3 fit_grid.py | grep -q "OOS sharpe: -0.19"
python3 deflated.py | grep -q "Bonferroni t-bar at N=100: 3.29"
echo "ALL ch09 CHECKS PASS"

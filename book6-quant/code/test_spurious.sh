#!/bin/bash
# Reruns the spurious-regression demo and compares with the output printed in Chapter 2.
cd "$(dirname "$0")"
exp=$'levels : median R^2 = 0.165, share with R^2 > 0.3 = 0.346\nchanges: median R^2 = 0.0010, share with R^2 > 0.3 = 0.000'
[ "$(python3 spurious_regression.py)" = "$exp" ] && echo "test_spurious: ok" || { echo "FAIL spurious"; exit 1; }

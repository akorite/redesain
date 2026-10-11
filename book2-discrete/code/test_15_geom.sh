#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 power_check.py | grep -F "secant: PA*PB = 4.000000"
python3 power_check.py | grep -F "agree: True"
python3 power_check.py | grep -F "interior: QA*QB = 0.870000"
python3 invert.py | grep -F "4.44e-16"
python3 invert.py | grep -F "r^2 = 4.0"
echo PASS

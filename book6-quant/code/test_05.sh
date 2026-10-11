#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
python3 scoring.py | grep -q "q=0.6 report 0.6: E\[Brier\]=0.2400"
python3 calibration.py | grep -q "ECE=0.0747"
python3 calibration.py | grep -q "calibrated twin ECE=0.0230"
python3 arb_check.py | grep -q "100 binary markets checked, YES+NO deviating >3c from 1: 0"
python3 arb_check.py | grep -q "markets priced <5c on the lead outcome: 21"
python3 resolve_sim.py | grep -q "buy YES@0.62 true 0.70: EV +0.080"
echo "ALL ch05 CHECKS PASS"

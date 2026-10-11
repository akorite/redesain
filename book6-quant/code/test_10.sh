#!/usr/bin/env bash
set -e; cd "$(dirname "$0")"
python3 impact_model.py | grep -q "10.0% of ADV)  impact   63.2bp"
python3 twap_vwap.py | grep -q "IS VWAP:  -72.72bp"
python3 is_shortfall.py | grep -q "instant IS: +63.2bp"
python3 is_shortfall.py | grep -q "+48.5bp"
echo "ALL ch10 CHECKS PASS"

#!/usr/bin/env bash
set -e; cd "$(dirname "$0")"
python3 wf_demo.py | grep -q "IS +1.51  OOS -0.52"
python3 wf_demo.py | grep -q "IS -0.88  OOS +0.52"
python3 purged_kfold.py | grep -q "116 overlapping labels"
python3 purged_kfold.py | grep -q "corr 0.983"
echo "ALL ch11 CHECKS PASS"

#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 ineq_scan.py | grep -F "min = 1.5003 >= 1.5"
python3 ineq_scan.py | grep -F "AM-GM held on all 10000 triples: True"
python3 ineq_scan.py | grep -F "minimum value = 2"
echo PASS

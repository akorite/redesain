#!/usr/bin/env bash
set -e; cd "$(dirname "$0")"
python3 report_check.py | grep -q "9/9 fields present"
python3 repro_demo.py | grep -q "seed 7: ann ret -31.1%"
python3 redteam_demo.py | grep -q "4 pass / 1 flag"
echo "ALL ch15 CHECKS PASS"

#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
python3 data_clean.py | grep -q "raw 1006 prints -> dedup 990  (dupes 16)"
python3 resample_demo.py | grep -q "bar semantics verified: o=first, h=max, l=min, c=last"
python3 resample_demo.py | grep -q "n=635"
python3 gaps_detect.py | grep -q "outage window: 1791739020 .. 1791739140 (3 bars)"
python3 pin_data.py | grep -q "sha256 3450c146b18639b3"
echo "ALL ch07 CHECKS PASS"

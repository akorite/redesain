#!/bin/sh
# test_ch18.sh -- ch18 artifacts: sensor filter sim, Gerber gen, DRC check.
set -e
cd "$(dirname "$0")"
echo "== sensor filter sim (expect fc ~= 1.59k)"
ngspice -b ch18_sensor_filter.cir | grep -q "fc  *=.*1.59"
echo "== generate gerbers + drill"
python3 ch18_gerber_gen.py | grep -q "wrote"
echo "== DRC-style check (expect 0 violations)"
python3 ch18_drc_check.py | grep -q "0 violations"
echo "ch18 code OK"

#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
python3 amm_swap.py | grep -q "in  500: out  16633.3  eff price  33.27"
python3 il_calc.py | grep -q "r=2.00: IL= -5.72%"
python3 lp_sim.py | grep -q "mean +2.48%  no-fees -1.93%"
python3 cl_range.py | grep -q "range +/-20%: capital multiplier ~5.4x"
echo "ALL ch06 CHECKS PASS"

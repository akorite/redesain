#!/usr/bin/env bash
set -e; cd "$(dirname "$0")"
python3 kelly_sims.py | grep -q "f\* = 0.10"
python3 kelly_sims.py | grep -q "final   61089.0"
python3 kelly_est.py | grep -q "fhat=+3.75"
python3 ruin_sim.py | grep -q "bankroll 20 units: ruin 1.5%"
echo "ALL ch13 CHECKS PASS"

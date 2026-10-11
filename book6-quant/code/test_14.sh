#!/usr/bin/env bash
set -e; cd "$(dirname "$0")"
python3 risk_metrics.py | grep -q "hist VaR -2.94%  ES -4.12%"
python3 risk_metrics.py | grep -q "normal expect 1.9 days"
python3 ewma_vol.py | grep -q "EWMA vol now 28.8%"
python3 stress_demo.py | grep -q "worst day: -9.90%"
echo "ALL ch14 CHECKS PASS"

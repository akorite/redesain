#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 fe_search.py | grep -F "quadratic survivors: [(1.0, 0.0)]"
python3 fe_search.py | grep -F "verdict: f(t) = t^2 + C is the whole degree-<=2 family"
echo PASS

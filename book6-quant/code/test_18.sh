#!/usr/bin/env bash
# ch18 regression: every printed output in the chapter must reproduce.
set -e
cd "$(dirname "$0")"
echo "[1] cycle2_carry.py"
python3 cycle2_carry.py | grep -q "mean carry +0.12bp/h  ann +10.3%"
python3 cycle2_carry.py | grep -q "equity over window 1.0059"
echo "   ok: carry"
echo "[2] cycle2_se.py"
python3 cycle2_se.py | grep -q "t-stat +3.85"
python3 cycle2_se.py | grep -q "se 0.030bp/h"
echo "   ok: se"
echo "[3] cycle2_sizing.py"
python3 cycle2_sizing.py | grep -q "3x notional: buffer 33%"
python3 cycle2_sizing.py | grep -q "+10.3%/yr; at 3x"
echo "   ok: sizing"
echo "[4] memo2_render.py"
python3 memo2_render.py | grep -q "+0.12bp/h (+10.3%/yr), t=+3.8"
python3 memo2_render.py | grep -q "CONDITIONAL"
echo "   ok: memo"
echo "[5] figdata18.py regenerates"
python3 figdata18.py >/dev/null
test -s ../figures/data/ch18-premium.dat && test -s ../figures/data/ch18-carryeq.dat
echo "   ok: fig data committed-path"
echo "ALL ch18 CHECKS PASS"

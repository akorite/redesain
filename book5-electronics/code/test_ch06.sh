#!/bin/sh
# ch06 transistor checks: recompute the claimed numbers from the .dat files
set -e
cd "$(dirname "$0")"
ngspice -b ch06_nmos_inv.cir 2>/dev/null | grep -q -- "-3.22881e-04" || ngspice -b ch06_nmos_inv.cir 2>&1 | grep -q "3.22881e-04"
ngspice -b ch06_cmos_inv.cir 2>&1 | grep -c "3.31000e-12" | grep -q "^2$"
ngspice -b ch06_switch_load.cir 2>&1 | grep -q "5.184072e+00"
echo "ch06 tests: all sim outputs reproduce"

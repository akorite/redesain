#!/bin/sh
# test_ch02.sh -- Chapter 2 checks: netlists run, outputs contain expected values.
cd "$(dirname "$0")" || exit 1
command -v ngspice >/dev/null 2>&1 || { echo "ngspice not installed; SKIP"; exit 0; }

ngspice -b ch02_led.cir | grep -q "1.47745e-02" || { echo "FAIL: led .op current"; exit 1; }
ngspice -b ch02_sweep.cir >/dev/null 2>&1
tail -1 ch02_sweep.dat | grep -q "1.47744954e-02" || { echo "FAIL: sweep endpoint"; exit 1; }
echo "ch02 tests: PASS"

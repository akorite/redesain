#!/bin/sh
out=$(python3 "$(dirname "$0")/euler_check.py")
echo "$out" | grep -q "Konigsberg multigraph: no Eulerian trail" || { echo "FAIL"; exit 1; }
echo "$out" | grep -q "5-cycle: Eulerian circuit" || { echo "FAIL"; exit 1; }
echo "$out" | grep -q "path of 4: Eulerian trail" || { echo "FAIL"; exit 1; }
echo "test_11_euler: PASS"

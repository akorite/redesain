#!/bin/bash
# Checks the two primer programs against the output printed in "Start here".
set -e
cd "$(dirname "$0")/start"
[ "$(python3 python_primer.py)" = $'count   = 4\naverage = 116.25\nlargest = 140\nsquares = [14400, 9025]' ] || { echo FAIL python_primer; exit 1; }
[ "$(python3 numpy_primer.py)" = $'shape of X: (3, 2)\nX @ w     : [12. 34. 56.]\ncolumn means: [3. 4.]' ] || { echo FAIL numpy_primer; exit 1; }
echo "test_start: ok"

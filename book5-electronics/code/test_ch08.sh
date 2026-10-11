#!/bin/sh
# ch08: rerun the Verilog truth printer + the two checker verifications
set -e
cd "$(dirname "$0")"
IV=$(command -v iverilog || echo /opt/homebrew/bin/iverilog)
VVP=$(command -v vvp || echo /opt/homebrew/bin/vvp)

"$IV" -o /tmp/ch08_gates_tb ch08_gates_tb.v
out=$("$VVP" /tmp/ch08_gates_tb)
echo "$out" | grep -q "1 1 |  1   1   0    0    0     1" || { echo "gates_tb output wrong"; exit 1; }

python3 ch08_truth_check.py "I&D | I&~B" "I&(D|~B)" | grep -q "EQUIVALENT on all 8" || { echo "alarm check failed"; exit 1; }
python3 ch08_truth_check.py "A&B | A&~B | ~A&B" "A|B" | grep -q "EQUIVALENT on all 4" || { echo "simplify check failed"; exit 1; }
echo "ch08 code OK"

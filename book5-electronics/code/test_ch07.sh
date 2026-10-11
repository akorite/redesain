#!/bin/sh
# ch07: rerun the three netlists, check the key numbers
set -e
cd "$(dirname "$0")"
NG=$(command -v ngspice || echo /opt/homebrew/bin/ngspice)

out=$("$NG" -b ch07_buffer.cir 2>&1)
echo "$out" | grep -q "2.272727e-01" || { echo "buffer: unbuffered divider wrong"; exit 1; }
echo "$out" | grep -q "2.4997" || { echo "buffer: buffered value wrong"; exit 1; }

out=$("$NG" -b ch07_inv_amp.cir 2>&1)
echo "$out" | grep -q "vclean              =  7.9" || { echo "inv_amp: clean gain wrong"; exit 1; }
echo "$out" | grep -q "vmax                =  1.04" || { echo "inv_amp: saturation wrong"; exit 1; }

out=$("$NG" -b ch07_comparator_osc.cir 2>&1)
echo "$out" | grep -q "t4                  =  9.36" || { echo "osc: T4 missing"; exit 1; }
echo "$out" | grep -q "t8                  =  1.81" || { echo "osc: T8 missing"; exit 1; }
echo "ch07 simulations OK"

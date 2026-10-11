#!/bin/sh
# test_ch03.sh -- Chapter 3 checks: the three simulations run and produce
# the node voltages / load-line the book prints. Run by `make test`.
set -e
cd "$(dirname "$0")"
echo "test_ch03: divider .op"
ngspice -b ch03_divider.cir | grep -q "V(2).*3.333333e+00" \
  && echo "  divider v(2)=3.33V OK"
echo "test_ch03: twoloop .op"
ngspice -b ch03_twoloop.cir | grep -q "V(3).*8.8329" \
  && echo "  twoloop v(3)=8.83V OK"
echo "test_ch03: thevenin load-line agreement"
ngspice -b ch03_thevenin.cir >/dev/null
ngspice -b ch03_thevenin_model.cir >/dev/null
python3 - <<'PY'
a=[l.split() for l in open('ch03_divider_loadline.dat') if l.split()]
b=[l.split() for l in open('ch03_thevenin_loadline.dat') if l.split()]
m=max(abs(float(x[1])-float(y[1])) for x,y in zip(a,b))
assert m < 1e-4, m
print("  load-line max diff %.1e OK" % m)
PY
echo "test_ch03: PASS"

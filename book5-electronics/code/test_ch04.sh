#!/bin/sh
# test_ch04.sh -- Chapter 4 checks: the three .tran simulations run and
# produce the numbers the book prints. Run by `make test`.
set -e
cd "$(dirname "$0")"
echo "test_ch04: rc step tau"
ngspice -b ch04_rc_step.cir >/dev/null
python3 - <<'PY'
d=[l.split() for l in open('ch04_rc_step.dat') if l.split()]
v=[float(r[1]) for r in d]
import bisect
assert abs(v[bisect.bisect_left([float(r[0]) for r in d],1e-3)]-3.162)<0.02
assert abs(v[-1]-4.966)<0.05
print("  v(tau)=3.162V, v(5tau)=4.97V OK")
PY
echo "test_ch04: decoupling dips"
ngspice -b ch04_decouple.cir >/dev/null
ngspice -b ch04_decouple_nocap.cir >/dev/null
python3 - <<'PY'
cap=min(float(l.split()[1]) for l in open('ch04_decouple_cap.dat') if l.split())
noc=min(float(l.split()[1]) for l in open('ch04_decouple_nocap.dat') if l.split())
assert abs((5-noc)-0.5)<0.01 and abs((5-cap)-0.091)<0.02
print("  dips 0.500V vs 0.091V OK")
PY
echo "test_ch04: flyback peak"
ngspice -b ch04_relay_flyback.cir >/dev/null
python3 - <<'PY'
pk=max(float(l.split()[1]) for l in open('ch04_flyback.dat') if l.split())
assert pk>1500, pk
print("  peak %.0fV (>1.5kV) OK" % pk)
PY
echo "test_ch04: PASS"

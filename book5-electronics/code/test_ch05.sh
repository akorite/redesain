#!/bin/sh
# test_ch05.sh -- Chapter 5 checks: rectifier ripple, flyback clamp, zener range.
set -e
cd "$(dirname "$0")"
echo "test_ch05: rectifier ripple"
ngspice -b ch05_rectifier.cir >/dev/null
python3 - <<'PY'
d=[l.split() for l in open('ch05_rectifier.dat') if l.split()]
t=[float(r[0]) for r in d]; v=[float(r[3]) for r in d]
seg=[v[i] for i in range(len(t)) if t[i]>0.06]
rip=max(seg)-min(seg)
assert 1.4<rip<1.6, rip
assert 9.0<max(seg)<9.3
print("  ripple %.2fV p-p, peak %.2fV OK"%(rip,max(seg)))
PY
echo "test_ch05: flyback clamp"
ngspice -b ch05_flyback_diode.cir >/dev/null
python3 - <<'PY'
d=[l.split() for l in open('ch05_flyback_diode.dat') if l.split()]
pk=max(float(r[1]) for r in d)
assert 12.5<pk<13.5, pk
print("  clamped at %.2fV OK"%pk)
PY
echo "test_ch05: zener range"
ngspice -b ch05_zener.cir >/dev/null
python3 - <<'PY'
d=[l.split() for l in open('ch05_zener.dat') if l.split()]
v0=float(d[0][3]); v30=float(d[-1][3])
assert 3.4<v0<3.5 and 3.2<v30<3.3, (v0,v30)
print("  vout %.3fV -> %.3fV OK"%(v0,v30))
PY
echo "test_ch05: PASS"

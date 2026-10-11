#!/usr/bin/env python3
# ch17_compare.py -- the three-points comparison table for ch17:
# ideal / measured / measured+contact-resistance, printed verbatim.
import subprocess, re, sys

def op(cir):
    r = subprocess.run(['ngspice','-b',cir], capture_output=True, text=True)
    m = re.search(r'V\(2\)\s+([-\d.e+]+)', r.stdout)
    m3 = re.search(r'V\(3\)\s+([-\d.e+]+)', r.stdout)
    return (float(m.group(1)) if m else None,
            float(m3.group(1)) if m3 else None)

# ideal divider: 5V, 1k, 2k -> 5*2/3 = 3.333
ideal = 5*2000/3000
# measured divider without contact: 987/1982
meas = 5.02*1982/(987+1982)
print('divider mid-point, three ways')
print('  ideal (5V, 1k||2k):              %.3f V' % ideal)
print('  measured Rs (5.02V, 987||1982):  %.3f V' % meas)
v2, v3 = op('ch17_divider_measured.cir')
print('  ngspice w/ 2ohm contact:  %.3f V (node2)' % v2)
print('                          %.3f V (node3)' % v3)
print('  drift vs ideal:           %+.1f %%' % (100*(v2-ideal)/ideal))

# RC fade: ideal tau vs measured tau
tau_i = 1000*1e-6
tau_m = 985*1.08e-6
print('\nrc fade time constant')
print('  ideal tau (1k*1uF):      %.3f ms' % (tau_i*1e3))
print('  measured tau (985*1.08u): %.3f ms' % (tau_m*1e3))
print('  shift:                   %+.1f %%' % (100*(tau_m-tau_i)/tau_i))

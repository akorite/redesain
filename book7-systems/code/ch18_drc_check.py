#!/usr/bin/env python3
# ch18_drc_check.py -- the board's rules enforced over the actual
# pad/track geometry in ch18_gerber_gen.py's coordinates. Prints a
# DRC-style report; exits nonzero on violations (run the broken
# variant to see the report change).
import math, sys

RULES = {'min_track_mm': 0.200, 'min_clear_mm': 0.150,
         'min_hole_edge_mm': 0.250}
PADS = {'J1.1':(4.0,4.0,0.8),'J1.2':(4.0,6.54,0.8),
        'J1.3':(4.0,9.08,0.8),'J1.4':(4.0,11.62,0.8),
        'U1.in':(16.0,4.0,1.15),'U1.out':(22.0,4.0,1.15),
        'U2.1':(30.0,12.0,0.8),'U2.2':(30.0,9.0,0.8),
        'R1.1':(24.0,9.0,0.9),'R1.2':(26.0,9.0,0.9)}
HOLES = [(4,4),(4,6.54),(4,9.08),(4,11.62),(30,9),(30,12),
         (2,2),(38,28)]
BOARD = (0,0,40,30)

viol = 0
# 1. pad-to-pad clearance
names = list(PADS)
for i in range(len(names)):
    for j in range(i+1, len(names)):
        x1,y1,r1 = PADS[names[i]]; x2,y2,r2 = PADS[names[j]]
        d = math.hypot(x1-x2, y1-y2) - r1 - r2
        if d < RULES['min_clear_mm']:
            viol += 1; print('CLEAR %s <-> %s: %.3fmm < %.3fmm'
                             % (names[i],names[j],d,RULES['min_clear_mm']))
# 2. holes inside board with edge margin
for (x,y) in HOLES:
    ok = (BOARD[0]+RULES['min_hole_edge_mm'] <= x <= BOARD[2]-RULES['min_hole_edge_mm']
          and BOARD[1]+RULES['min_hole_edge_mm'] <= y <= BOARD[3]-RULES['min_hole_edge_mm'])
    if not ok:
        viol += 1; print('EDGE hole at (%.1f,%.1f) violates %.2fmm keepout'
                         % (x,y,RULES['min_hole_edge_mm']))
# 3. mounting-hole clearance to nearest pad
for (x,y) in [(2,2),(38,28)]:
    d = min(math.hypot(x-px,y-py)-r for px,py,r in PADS.values())
    print('mount(%g,%g) pad-clearance %.2fmm' % (x,y,d))
print('%d violations' % viol)
sys.exit(1 if viol else 0)

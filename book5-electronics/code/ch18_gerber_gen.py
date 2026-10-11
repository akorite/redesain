#!/usr/bin/env python3
# ch18_gerber_gen.py -- emit a REAL (minimal but valid) Gerber X2
# pair + Excellon drill for the ch18 sensor board: 40x30mm outline,
# through-hole header + LDO/sensor pads, F_Cu tracks, B_Cu pour,
# Edge_Cuts. Everything the chapter quotes is generated here.
OUT = 'ch18_sensor'
def head(name, f):
    f.write('%TF.FileFunction,' + name + '*%\n')
    f.write('%FSLAX34Y34*%\n%MOMM*%\n%LPD*%\n')
    f.write('%ADD10C,0.250*%\n%ADD11R,1.800X1.800*%\n'
            '%ADD12C,1.600*%\n%ADD13O,1.300X2.300*%\n')

def end(f): f.write('M02*\n'); f.close()

def line(f, x1, y1, x2, y2):
    f.write('X%.4fY%.4fD01*\n' % (x1, y1))
    f.write('X%.4fY%.4fD02*\n' % (x2, y2))

def flash(f, ap, x, y):
    f.write('D%02d*\n' % ap)
    f.write('X%.4fY%.4fD03*\n' % (x, y))

# ---------------- F_Cu: pads + tracks ----------------
f = open(OUT + '-F_Cu.gbr', 'w'); head('Copper,L1,Top', f)
PADS = {  # name: (x,y,aperture)
  'J1.1': (4.0, 4.0, 12), 'J1.2': (4.0, 6.54, 12),
  'J1.3': (4.0, 9.08, 12), 'J1.4': (4.0, 11.62, 12),
  'U1.in': (16.0, 4.0, 13), 'U1.out': (22.0, 4.0, 13),
  'U2.1': (30.0, 12.0, 12), 'U2.2': (30.0, 9.0, 12),
  'R1.1': (24.0, 9.0, 11), 'R1.2': (26.0, 9.0, 11),
}
for (x, y, ap) in PADS.values(): flash(f, ap, x, y)
f.write('D10*\n')
# tracks: J1.1(+5V)->U1.in ; U1.out->R1.1 area ; U2.2->R1.1 ; R1.2->J1.4
for seg in [((4.0,4.0),(16.0,4.0)), ((22.0,4.0),(24.0,9.0)),
            ((30.0,9.0),(24.0,9.0)), ((26.0,9.0),(4.0,11.62)),
            ((22.0,4.0),(4.0,9.08)), ((30.0,12.0),(4.0,9.08))]:
    (x1,y1),(x2,y2) = seg; line(f,x1,y1,x2,y2)
end(f)

# ---------------- B_Cu: ground pour (region) ----------------
f = open(OUT + '-B_Cu.gbr', 'w'); head('Copper,L2,Bot', f)
f.write('%TA.Region*%\nG36*\n')
for (x,y) in [(1,1),(39,1),(39,29),(1,29),(1,1)]:
    f.write('X%.4fY%.4fD0%d*\n' % (x,y,1 if (x,y)!=(1,1) else 2))
f.write('G37*\n%TD*%\n'); end(f)

# ---------------- Edge_Cuts ----------------
f = open(OUT + '-Edge_Cuts.gbr', 'w'); head('Profile', f)
f.write('D10*\n')
for seg in [((0,0),(40,0)),((40,0),(40,30)),((40,30),(0,30)),((0,30),(0,0))]:
    (x1,y1),(x2,y2)=seg; line(f,x1,y1,x2,y2)
end(f)

# ---------------- drill ----------------
f = open(OUT + '.drl', 'w')
f.write('M48\n; DRILL file, sensor board\nMETRIC,TZ\n')
f.write('T1C0.900\nT2C3.200\n%%,T1\n')   # T1=0.9mm comp holes, T2=3.2mm mount
for (x,y) in [(4,4),(4,6.54),(4,9.08),(4,11.62),(30,9),(30,12)]:
    f.write('X%.3fY%.3f\n' % (x,y))
f.write('T2\nX2.000Y2.000\nX38.000Y28.000\nM30\n'); f.close()

print('wrote %s-F_Cu.gbr, %s-B_Cu.gbr, %s-Edge_Cuts.gbr, %s.drl'
      % (OUT,OUT,OUT,OUT))

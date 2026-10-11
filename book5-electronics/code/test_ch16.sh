#!/bin/bash
set -e; cd "$(dirname "$0")"; CXX=${CXX:-clang++}; F="-std=c++17 -O2 -Wall -Wextra"; mkdir -p .build
for p in point_location line_seg_int point_in_poly poly_area poly_lattice convex_hull min_dist; do $CXX $F -o .build/$p $p.cpp; done
expect() { echo "$3" | grep -qF -- "$2" || { echo "FAIL $1: wanted '$2' in: $3" >&2; exit 1; }; echo "$1 PASS"; }
expect loc "$(printf "LEFT\nRIGHT\nTOUCH")" "$(printf "3\n1 1 5 3 2 3\n1 1 5 3 4 1\n1 1 5 3 3 2\n" | ./.build/point_location)"
expect seg "$(printf "NO\nYES\nYES\nYES\nYES")" "$(printf "5\n1 1 5 3 1 2 4 3\n1 1 5 3 1 1 4 3\n1 1 5 3 2 3 4 1\n1 1 5 3 2 4 4 1\n1 1 5 3 3 2 7 4\n" | ./.build/line_seg_int)"
expect polyarea "16" "$(printf "4\n1 1\n4 2\n3 5\n1 4\n" | ./.build/poly_area)"
expect inpoly "$(printf "INSIDE\nOUTSIDE\nBOUNDARY")" "$(printf "4 3\n1 1\n4 2\n3 5\n1 4\n2 3\n3 1\n1 3\n" | ./.build/point_in_poly)"
expect lattice "6 8" "$(printf "4\n1 1\n5 3\n3 5\n1 4\n" | ./.build/poly_lattice)"
expect mindist "2" "$(printf "4\n2 1\n4 4\n1 2\n6 3\n" | ./.build/min_dist)"
expect hull "4" "$(printf "6\n2 1\n2 5\n3 3\n4 3\n4 4\n6 3\n" | ./.build/convex_hull | head -1)"
python3 - <<'PY'
import random, subprocess, math
R=random.Random(7)
def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def onseg(p,a,b): return min(a[0],b[0])<=p[0]<=max(a[0],b[0]) and min(a[1],b[1])<=p[1]<=max(a[1],b[1])
def sgn(x): return (x>0)-(x<0)
def segint(a,b,c,d):
    o1,o2,o3,o4=cross(a,b,c),cross(a,b,d),cross(c,d,a),cross(c,d,b)
    if o1==0 and onseg(c,a,b): return True
    if o2==0 and onseg(d,a,b): return True
    if o3==0 and onseg(a,c,d): return True
    if o4==0 and onseg(b,c,d): return True
    if o1==0 or o2==0 or o3==0 or o4==0: return False
    return sgn(o1)!=sgn(o2) and sgn(o3)!=sgn(o4)
# orient + seg_int mirrors
for _ in range(150):
    a,b,c,d=[(R.randint(-8,8),R.randint(-8,8)) for _ in range(4)]
    o=cross(a,b,c)
    want="LEFT" if o>0 else "RIGHT" if o<0 else "TOUCH"
    inp=f"1\n{a[0]} {a[1]} {b[0]} {b[1]} {c[0]} {c[1]}\n"
    got=subprocess.run(['./.build/point_location'],input=inp,capture_output=True,text=True).stdout.strip()
    assert got==want,(inp,got,want)
    inp2=f"1\n{a[0]} {a[1]} {b[0]} {b[1]} {c[0]} {c[1]} {d[0]} {d[1]}\n"
    got2=subprocess.run(['./.build/line_seg_int'],input=inp2,capture_output=True,text=True).stdout.strip()
    assert got2==("YES" if segint(a,b,c,d) else "NO"),(inp2,got2)
print("orient+segint stress: 150/150 PASS")
# polygon mirrors: area2, pick, in_poly, hull on random convex-ish polygons
def mkpoly(n):
    cx,cy=R.randint(-5,5),R.randint(-5,5)
    pts=set()
    while len(pts)<n: pts.add((R.randint(-6,6),R.randint(-6,6)))
    pts=list(pts)
    import math as m
    pts.sort(key=lambda p:m.atan2(p[1]-cy,p[0]-cx))
    return pts
def area2(p): return abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[(i+1)%len(p)][0]*p[i][1] for i in range(len(p))))
def bpts(p):
    from math import gcd
    return sum(gcd(abs(p[(i+1)%len(p)][0]-p[i][0]),abs(p[(i+1)%len(p)][1]-p[i][1])) for i in range(len(p)))
def inpoly(q,p):
    n=len(p); ins=False
    for i in range(n):
        a,b=p[i],p[(i+1)%n]
        if cross(a,b,q)==0 and onseg(q,a,b): return 1
        if (a[1]>q[1])!=(b[1]>q[1]) and (cross(q,a,b)>0)==(a[1]>q[1]): ins=not ins
    return 0 if ins else 2
for _ in range(100):
    n=R.randint(3,7); p=mkpoly(n)
    inp=f"{n}\n"+"".join(f"{x} {y}\n" for x,y in p)
    got=subprocess.run(['./.build/poly_area'],input=inp,capture_output=True,text=True).stdout.strip()
    assert got==str(area2(p)),(inp,got,area2(p))
    B=bpts(p); I=(area2(p)-B+2)//2
    got2=subprocess.run(['./.build/poly_lattice'],input=inp,capture_output=True,text=True).stdout.strip()
    assert got2==f"{I} {B}",(inp,got2,I,B)
    q=(R.randint(-8,8),R.randint(-8,8))
    inp3=f"{n} 1\n"+"".join(f"{x} {y}\n" for x,y in p)+f"{q[0]} {q[1]}\n"
    got3=subprocess.run(['./.build/point_in_poly'],input=inp3,capture_output=True,text=True).stdout.strip()
    want3=["INSIDE","BOUNDARY","OUTSIDE"][inpoly(q,p)]
    assert got3==want3,(inp3,got3,want3)
print("area+pick+inpoly stress: 100/100 PASS")
# min_dist vs brute
for _ in range(100):
    n=R.randint(2,12)
    pts=list({(R.randint(-20,20),R.randint(-20,20)) for _ in range(n)})
    n=len(pts)
    inp=f"{n}\n"+"".join(f"{x} {y}\n" for x,y in pts)
    want=min((a[0]-b[0])**2+(a[1]-b[1])**2 for i,a in enumerate(pts) for b in pts[i+1:])
    got=subprocess.run(['./.build/min_dist'],input=inp,capture_output=True,text=True).stdout.strip()
    assert got==str(want),(inp,got,want)
print("min_dist stress: 100/100 PASS")
# hull: emitted vertices form the hull (convex, contains all, boundary keeps collinear)
for _ in range(100):
    n=R.randint(3,15)
    pts=list({(R.randint(-9,9),R.randint(-9,9)) for _ in range(n)})
    inp=f"{len(pts)}\n"+"".join(f"{x} {y}\n" for x,y in pts)
    out=subprocess.run(['./.build/convex_hull'],input=inp,capture_output=True,text=True).stdout.split()
    k=int(out[0]); h=[(int(out[i]),int(out[i+1])) for i in range(1,2*k+1,2)]
    assert len(h)==k
    if k>2:
        # all emitted turns same sign or zero (convex incl. boundary collinear)
        s=set()
        for i in range(k):
            s.add(sgn(cross(h[i],h[(i+1)%k],h[(i+2)%k])))
        assert s<={0,1} or s<={-1,0},(inp,h)
        # every point inside-or-boundary of the emitted polygon
        for q in pts:
            assert inpoly(q,h)!=2,(inp,q,h)
print("hull stress: 100/100 PASS")
PY
echo "test_ch16: ALL PASS"

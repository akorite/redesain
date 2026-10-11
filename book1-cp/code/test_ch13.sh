#!/bin/bash
set -e; cd "$(dirname "$0")"; CXX=${CXX:-clang++}; F="-std=c++17 -O2 -Wall -Wextra"; mkdir -p .build
for p in dynamic_rsq dynamic_rmq range_update_queries hotel_queries list_removals; do $CXX $F -o .build/$p $p.cpp; done
expect() { echo "$3" | grep -qF "$2" || { echo "FAIL $1: wanted '$2' in: $3" >&2; exit 1; }; echo "$1 PASS"; }
expect rsq "14" "$(printf "8 4\n3 2 4 5 1 1 5 3\n2 1 4\n2 5 6\n1 3 1\n2 1 4\n" | ./.build/dynamic_rsq | head -1)"
expect rmq "2" "$(printf "8 3\n3 2 4 5 1 1 5 3\n2 1 4\n2 5 6\n1 2 3\n" | ./.build/dynamic_rmq | head -1)"
expect ruq "5" "$(printf "8 2\n3 2 4 5 1 1 5 3\n1 2 4 1\n2 3\n" | ./.build/range_update_queries)"
expect hotel "3 8 1 0 0" "$(printf "8 5\n3 2 4 1 3 3 2 4\n4 4 2 4 5\n" | ./.build/hotel_queries)"
expect rem "1 2 2 6 4" "$(printf "5\n2 6 1 4 2\n3 1 3 1 1\n" | ./.build/list_removals)"
python3 - <<'PY'
import random,subprocess
# segtree sum/min vs brute
for fn,kind in [('dynamic_rsq','sum'),('dynamic_rmq','min')]:
    for _ in range(80):
        n=random.randint(2,9);q=random.randint(1,8)
        a=[random.randint(0,20) for _ in range(n)];ops=[]
        for _ in range(q):
            if random.random()<.4:
                ops.append((1,random.randint(1,n),random.randint(0,20)))
            else:
                l=random.randint(1,n);r=random.randint(l,n);ops.append((2,l,r))
        inp=f"{n} {q}\n"+' '.join(map(str,a))+"\n"+"".join(f"{t} {x} {y}\n" for t,x,y in ops)
        b=a[:];want=[]
        for t,x,y in ops:
            if t==1:b[x-1]=y
            else:want.append(sum(b[x-1:y]) if kind=='sum' else min(b[x-1:y]))
        got=subprocess.run(['./.build/'+fn],input=inp,capture_output=True,text=True).stdout.split()
        assert list(map(int,got))==want,(inp,got,want)
    print(f"{kind} stress: 80/80 PASS")
# fenwick diff range-update/point-query vs brute
for _ in range(80):
    n=random.randint(2,9);q=random.randint(1,8)
    a=[random.randint(0,20) for _ in range(n)];ops=[]
    for _ in range(q):
        if random.random()<.4:
            l=random.randint(1,n);r=random.randint(l,n)
            d=random.randint(1,10)
            ops.append(("1 %d %d %d" % (l,r,d),('u',l,r,d)))
        else:
            k=random.randint(1,n)
            ops.append(("2 %d" % k,('q',k)))
    random.shuffle(ops)
    inp=f"{n} {q}\n"+' '.join(map(str,a))+"\n"+"".join(o+"\n" for o,_ in ops)
    b=a[:];want=[]
    for _,e in ops:
        if e[0]=='u':
            for i in range(e[1]-1,e[2]):b[i]+=e[3]
        else:want.append(b[e[1]-1])
    got=subprocess.run(['./.build/range_update_queries'],input=inp,capture_output=True,text=True).stdout.split()
    assert list(map(int,got))==want,(inp,got,want)
print("ruq stress: 80/80 PASS")
# hotel vs brute first-fit
for _ in range(80):
    n=random.randint(1,8);m=random.randint(1,6)
    a=[random.randint(1,9) for _ in range(n)]
    req=[random.randint(1,10) for _ in range(m)]
    inp=f"{n} {m}\n"+' '.join(map(str,a))+"\n"+' '.join(map(str,req))+"\n"
    b=a[:];want=[]
    for r in req:
        p=next((i for i,v in enumerate(b) if v>=r),None)
        want.append(0 if p is None else p+1)
        if p is not None:b[p]-=r
    got=subprocess.run(['./.build/hotel_queries'],input=inp,capture_output=True,text=True).stdout.split()
    assert list(map(int,got))==want,(inp,got,want)
print("hotel stress: 80/80 PASS")
# list removals vs brute
for _ in range(80):
    n=random.randint(1,9)
    a=[random.randint(0,99) for _ in range(n)]
    live=a[:];ks=[]
    for _ in range(n):
        k=random.randint(1,len(live));ks.append(k);live.pop(k-1)
    inp=f"{n}\n"+' '.join(map(str,a))+"\n"+' '.join(map(str,ks))+"\n"
    live=a[:];want=[]
    for k in ks:want.append(live.pop(k-1))
    got=subprocess.run(['./.build/list_removals'],input=inp,capture_output=True,text=True).stdout.split()
    assert list(map(int,got))==want,(inp,got,want)
print("removals stress: 80/80 PASS")
PY
echo "test_ch13: ALL PASS"

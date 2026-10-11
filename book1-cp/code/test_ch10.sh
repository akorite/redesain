#!/bin/bash
set -e; cd "$(dirname "$0")"; CXX=${CXX:-clang++}; F="-std=c++17 -O2 -Wall -Wextra"; mkdir -p .build
for p in subordinates tree_diameter company_queries tree_distances2 distance_queries; do $CXX $F -o .build/$p $p.cpp; done
expect() { echo "$3" | grep -qF "$2" || { echo "FAIL $1: wanted '$2' in: $3" >&2; exit 1; }; echo "$1 PASS"; }
expect subor "4 0 2 0 0" "$(printf "5\n1 1 3 3\n" | ./.build/subordinates)"
expect diam "3" "$(printf "5\n1 2\n1 3\n3 4\n3 5\n" | ./.build/tree_diameter)"
expect comp "$(printf "3\n1\n-1")" "$(printf "5 3\n1 1 3 3\n4 1\n4 2\n3 3\n" | ./.build/company_queries)"
expect dist2 "2 3 2 3 3" "$(printf "5\n1 2\n1 3\n3 4\n3 5\n" | ./.build/tree_distances2)"
expect distq "$(printf "2\n3\n0")" "$(printf "5 3\n1 2\n1 3\n3 4\n3 5\n4 5\n4 2\n1 1\n" | ./.build/distance_queries)"
python3 - <<'PY'
import random,subprocess
for _ in range(150):
    n=random.randint(2,10)
    es=[(random.randint(1,i),i+1) for i in range(1,n)]
    inp=f"{n}\n"+"".join(f"{a} {b}\n" for a,b in es)
    g={i:[] for i in range(1,n+1)}
    for a,b in es: g[a].append(b);g[b].append(a)
    par={1:0};dep={1:0};st=[1];ordr=[]
    while st:
        v=st.pop();ordr.append(v)
        for u in g[v]:
            if u!=par.get(v):par[u]=v;dep[u]=dep[v]+1;st.append(u)
    dd=0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            a,b=i,j;seen=set()
            while dep[a]>dep[b]:a=par[a]
            while dep[b]>dep[a]:b=par[b]
            while a!=b:a,b=par[a],par[b]
            dd=max(dd,dep[i]+dep[j]-2*dep[a])
    got=subprocess.run(['./.build/tree_diameter'],input=inp,capture_output=True,text=True).stdout.strip()
    assert int(got)==dd,(inp,got,dd)
print("diameter stress: 150/150 PASS")
for _ in range(150):
    n=random.randint(2,10); q=6
    es=[(random.randint(1,i),i+1) for i in range(1,n)]
    g={i:[] for i in range(1,n+1)}
    for a,b in es:g[a].append(b);g[b].append(a)
    par={1:0};dep={1:0};st=[1]
    while st:
        v=st.pop()
        for u in g[v]:
            if u!=par.get(v):par[u]=v;dep[u]=dep[v]+1;st.append(u)
    qs=[(random.randint(1,n),random.randint(1,n)) for _ in range(q)]
    inp=f"{n} {q}\n"+"".join(f"{a} {b}\n" for a,b in es)+"".join(f"{a} {b}\n" for a,b in qs)
    want=[]
    for a,b in qs:
        x,y=a,b
        while dep[x]>dep[y]:x=par[x]
        while dep[y]>dep[x]:y=par[y]
        while x!=y:x,y=par[x],par[y]
        want.append(str(dep[a]+dep[b]-2*dep[x]))
    got=subprocess.run(['./.build/distance_queries'],input=inp,capture_output=True,text=True).stdout.split()
    assert got==want,(inp,got,want)
print("distq stress: 150/150 PASS")
for _ in range(150):
    n=random.randint(2,9)
    es=[(random.randint(1,i),i+1) for i in range(1,n)]
    g={i:[] for i in range(1,n+1)}
    for a,b in es:g[a].append(b);g[b].append(a)
    inp=f"{n}\n"+"".join(f"{a} {b}\n" for a,b in es)
    # brute: for each v, BFS max dist
    import collections
    want=[]
    for s in range(1,n+1):
        d={s:0};qq=collections.deque([s])
        while qq:
            v=qq.popleft()
            for u in g[v]:
                if u not in d:d[u]=d[v]+1;qq.append(u)
        want.append(str(max(d.values())))
    got=subprocess.run(['./.build/tree_distances2'],input=inp,capture_output=True,text=True).stdout.split()
    assert got==want,(inp,got,want)
print("reroot stress: 150/150 PASS")
PY
echo "test_ch10: ALL PASS"

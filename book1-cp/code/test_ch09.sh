#!/bin/bash
set -e; cd "$(dirname "$0")"; CXX=${CXX:-clang++}; F="-std=c++17 -O2 -Wall -Wextra"; mkdir -p .build
for p in road_construction building_roads road_reparation closing_farm; do $CXX $F -o .build/$p $p.cpp; done
expect() { echo "$3" | grep -qF "$2" || { echo "FAIL $1: wanted '$2' in: $3" >&2; exit 1; }; echo "$1 PASS"; }
expect constr "$(printf "4 2\n3 3\n2 3")" "$(printf "5 3\n1 2\n1 3\n4 5\n" | ./.build/road_construction)"
expect roads "$(printf "1\n1 3")" "$(printf "4 2\n1 2\n3 4\n" | ./.build/building_roads)"
expect rep "14" "$(printf "5 6\n1 2 3\n2 3 5\n2 4 2\n3 4 8\n5 1 7\n5 4 4\n" | ./.build/road_reparation)"
expect repimp "IMPOSSIBLE" "$(printf "4 1\n1 2 3\n" | ./.build/road_reparation)"
expect farm "$(printf "YES\nYES\nYES\nYES")" "$(printf "4\n1 2\n1 3\n1 4\n4\n3\n1\n2\n" | ./.build/closing_farm)"
expect farm2 "NO" "$(printf "4\n1 2\n3 4\n2\n1\n3\n4\n" | ./.build/closing_farm | head -1)"
python3 - <<'FARMPY'
import random,subprocess,collections
for _ in range(200):
    n=random.randint(2,8)
    es=[(random.randint(1,i),i+1) for i in range(1,n)]
    g={i:[] for i in range(1,n+1)}
    for a,b in es:g[a].append(b);g[b].append(a)
    order=list(range(1,n+1));random.shuffle(order)
    inp=f"{n}\n"+"".join(f"{a} {b}\n" for a,b in es)+"".join(f"{x}\n" for x in order)
    got=subprocess.run(['./.build/closing_farm'],input=inp,capture_output=True,text=True).stdout.split()
    gone=set();want=[]
    for v in order:
        gone.add(v)
        rem=[u for u in range(1,n+1) if u not in gone]
        if len(rem)<=1:want.append("YES");continue
        seen={rem[0]};q=collections.deque([rem[0]])
        while q:
            x=q.popleft()
            for u in g[x]:
                if u not in gone and u not in seen:seen.add(u);q.append(u)
        want.append("YES" if len(seen)==len(rem) else "NO")
    assert got==want,(inp,got,want)
print("farm stress: 200/200 PASS")
FARMPY
python3 - <<'PY'
import random,subprocess
for _ in range(150):
    n=random.randint(2,10); m=random.randint(0,15)
    es=[(random.randint(1,n),random.randint(1,n),random.randint(1,20)) for _ in range(m)]
    inp=f"{n} {m}\n"+"".join(f"{a} {b} {w}\n" for a,b,w in es)
    par=list(range(n+1)); sz=[1]*(n+1)
    def f(v):
        while par[v]!=v: par[v]=par[par[v]]; v=par[v]
        return v
    tot=0;cnt=0
    for a,b,w in sorted(es,key=lambda e:e[2]):
        ra,rb=f(a),f(b)
        if ra!=rb:
            if sz[ra]<sz[rb]:ra,rb=rb,ra
            par[rb]=ra;sz[ra]+=sz[rb];tot+=w;cnt+=1
    got=subprocess.run(['./.build/road_reparation'],input=inp,capture_output=True,text=True).stdout.strip()
    want="IMPOSSIBLE" if cnt<n-1 else str(tot)
    assert got==want,(inp,got,want)
print("kruskal stress: 150/150 PASS")
PY
echo "test_ch09: ALL PASS"

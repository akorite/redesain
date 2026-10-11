#!/bin/bash
set -e; cd "$(dirname "$0")"
CXX=${CXX:-clang++}; F="-std=c++17 -O2 -Wall -Wextra"; mkdir -p .build
for p in shortest_routes1 cycle_finding routes2 flight_discount cowroad; do $CXX $F -o .build/$p $p.cpp; done
expect() { echo "$3" | grep -qF "$2" || { echo "FAIL $1: wanted '$2' in: $3" >&2; exit 1; }; echo "$1 PASS"; }
expect routes1 "0 5 2" "$(printf "3 4\n1 2 6\n1 3 2\n3 2 3\n1 3 4\n" | ./.build/shortest_routes1)"
expect routes2 "$(printf "5\n5\n8\n-1\n3")" "$(printf "4 3 5\n1 2 5\n1 3 9\n2 3 3\n1 2\n2 1\n1 3\n1 4\n3 2\n" | ./.build/routes2)"
expect cyc "YES" "$(printf "4 5\n1 2 1\n2 4 1\n3 1 1\n4 1 -3\n4 3 -2\n" | ./.build/cycle_finding)"
expect nocyc "NO" "$(printf "3 2\n1 2 1\n2 3 1\n" | ./.build/cycle_finding)"
expect disc "2" "$(printf "3 4\n1 2 3\n2 3 1\n1 3 7\n2 1 5\n" | ./.build/flight_discount)"
python3 - <<'PY'
import random, subprocess, heapq
for _ in range(200):
    n=random.randint(2,9); m=random.randint(0,14)
    es=[(random.randint(1,n),random.randint(1,n),random.randint(1,20)) for _ in range(m)]
    inp=f"{n} {m}\n"+"".join(f"{a} {b} {w}\n" for a,b,w in es)
    got=list(map(int,subprocess.run(['./.build/shortest_routes1'],input=inp,capture_output=True,text=True).stdout.split()))
    INF=4*10**18; d=[INF]*(n+1); d[1]=0; pq=[(0,1)]
    g={i:[] for i in range(1,n+1)}
    for a,b,w in es: g[a].append((b,w))
    while pq:
        du,u=heapq.heappop(pq)
        if du!=d[u]:continue
        for v,w in g[u]:
            if du+w<d[v]:d[v]=du+w;heapq.heappush(pq,(d[v],v))
    assert got==d[1:],(inp,got,d[1:])
print("dijkstra stress: 200/200 PASS")
for _ in range(200):
    n=random.randint(2,6); m=random.randint(0,10)
    es=[(random.randint(1,n),random.randint(1,n),random.randint(-5,9)) for _ in range(m)]
    inp=f"{n} {m}\n"+"".join(f"{a} {b} {w}\n" for a,b,w in es)
    out=subprocess.run(['./.build/cycle_finding'],input=inp,capture_output=True,text=True).stdout.split()
    INF=10**18; dist=[0]*(n+1); x=-1
    for _i in range(n):
        x=-1
        for a,b,w in es:
            if dist[a]+w<dist[b]:dist[b]=dist[a]+w;x=b
    want="NO" if x<0 else "YES"
    assert out[0]==want,(inp,out,want)
    if want=="YES":
        cyc=list(map(int,out[1:]))
        s=0; wmap={}
        for a,b,w in es:
            if (a,b) not in wmap or w<wmap[(a,b)]: wmap[(a,b)]=w
        for i in range(len(cyc)-1):
            assert (cyc[i],cyc[i+1]) in wmap,(cyc,es)
            s+=wmap[(cyc[i],cyc[i+1])]
        assert s<0,(cyc,es,s)
print("bellmanford stress: 200/200 PASS (sign + cycle validity)")
for _ in range(200):
    n=random.randint(2,7); m=random.randint(0,12); q=5
    es=[(random.randint(1,n),random.randint(1,n),random.randint(1,9)) for _ in range(m)]
    inp=f"{n} {m} {q}\n"+"".join(f"{a} {b} {w}\n" for a,b,w in es)
    INF=10**18; D=[[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):D[i][i]=0
    for a,b,w in es:D[a][b]=D[b][a]=min(D[a][b],w)
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if D[i][k]+D[k][j]<D[i][j]:D[i][j]=D[i][k]+D[k][j]
    qs=[(random.randint(1,n),random.randint(1,n)) for _ in range(q)]
    inp+="".join(f"{a} {b}\n" for a,b in qs)
    got=subprocess.run(['./.build/routes2'],input=inp,capture_output=True,text=True).stdout.split()
    want=[('-1' if D[a][b]>=INF else str(D[a][b])) for a,b in qs]
    assert got==want,(inp,got,want)
print("floyd stress: 200/200 PASS")
for _ in range(150):
    n=random.randint(2,7); m=random.randint(0,10)
    es=[(random.randint(1,n),random.randint(1,n),random.randint(1,20)) for _ in range(m)]
    inp=f"{n} {m}\n"+"".join(f"{a} {b} {w}\n" for a,b,w in es)
    INF=10**18; d=[[INF,INF] for _ in range(n+1)]; d[1][0]=0; pq=[(0,1,0)]
    g={i:[] for i in range(1,n+1)}
    for a,b,w in es:g[a].append((b,w))
    while pq:
        du,u,c=heapq.heappop(pq)
        if du!=d[u][c]:continue
        for v,w in g[u]:
            if du+w<d[v][c]:d[v][c]=du+w;heapq.heappush(pq,(d[v][c],v,c))
            if c==0 and du+w//2<d[v][1]:d[v][1]=du+w//2;heapq.heappush(pq,(d[v][1],v,1))
    got=subprocess.run(['./.build/flight_discount'],input=inp,capture_output=True,text=True).stdout.strip()
    assert int(got)==(d[n][1] if d[n][1]<INF else -1) or (d[n][1]>=INF and int(got)>=INF//2),(inp,got,d[n])
print("discount stress: 150/150 PASS")
PY
echo "test_ch08: ALL PASS"

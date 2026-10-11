#!/bin/bash
set -e; cd "$(dirname "$0")"
CXX=${CXX:-clang++}; F="-std=c++17 -O2 -Wall -Wextra"; mkdir -p .build
for p in shortest_routes1 cycle_finding routes2 flight_discount cowroad high_score; do $CXX $F -o .build/$p $p.cpp; done
expect() { echo "$3" | grep -qF -- "$2" || { echo "FAIL $1: wanted '$2' in: $3" >&2; exit 1; }; echo "$1 PASS"; }
expect routes1 "0 5 2" "$(printf "3 4\n1 2 6\n1 3 2\n3 2 3\n1 3 4\n" | ./.build/shortest_routes1)"
expect routes2 "$(printf "5\n5\n8\n-1\n3")" "$(printf "4 3 5\n1 2 5\n1 3 9\n2 3 3\n1 2\n2 1\n1 3\n1 4\n3 2\n" | ./.build/routes2)"
expect cyc "YES" "$(printf "4 5\n1 2 1\n2 4 1\n3 1 1\n4 1 -3\n4 3 -2\n" | ./.build/cycle_finding)"
expect nocyc "NO" "$(printf "3 2\n1 2 1\n2 3 1\n" | ./.build/cycle_finding)"
expect cyccyc "4 1 2 4" "$(printf "4 5\n1 2 1\n2 4 1\n3 1 1\n4 1 -3\n4 3 -2\n" | ./.build/cycle_finding | tail -1)"
expect cowroad "31" "$(printf "4 2\n30 92 36 10\n38 85 60 16\n41 13 5 68\n20 97 13 80\n" | ./.build/cowroad)"
expect disc "2" "$(printf "3 4\n1 2 3\n2 3 1\n1 3 7\n2 1 5\n" | ./.build/flight_discount)"
expect high "5" "$(printf "4 5\n1 2 3\n2 4 -1\n1 3 -2\n3 4 7\n1 4 4\n" | ./.build/high_score)"
expect high-unb "-1" "$(printf "4 5\n1 2 1\n2 3 1\n3 2 1\n3 4 1\n1 4 1\n" | ./.build/high_score)"
expect high-blocked "2" "$(printf "4 4\n1 4 2\n1 2 0\n2 3 1\n3 2 1\n" | ./.build/high_score)"
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
echo "== stress: cycle_finding emits a real negative cycle (150) =="
python3 - <<'PY'
import random, subprocess
R=random.Random(4)
for _ in range(150):
    n=R.randint(2,8); m=R.randint(0,14)
    E=[(R.randint(1,n),R.randint(1,n),R.randint(-9,9)) for _ in range(m)]
    inp=f"{n} {m}\n"+"".join(f"{a} {b} {w}\n" for a,b,w in E)
    out=subprocess.run(['./.build/cycle_finding'],input=inp,capture_output=True,text=True).stdout.split()
    # brute negative-cycle detect via repeated relaxation
    INF=10**18; d=[INF]*(n+1)
    for v in range(1,n+1):
        d2=d[:]; d2[v]=0
        for _i in range(n):
            for a,b,w in E:
                if d2[a]+w<d2[b]: d2[b]=d2[a]+w
        if d2!=d: d=d2
    has_cycle=False
    d=[0]*(n+1)                       # seed all vertices
    for _i in range(n):
        for a,b,w in E:
            if d[a]+w<d[b]: d[b]=d[a]+w
    if any(d[a]+w<d[b] for a,b,w in E): has_cycle=True
    if not has_cycle:
        assert out==['NO'],(inp,out)
    else:
        assert out[0]=='YES' and len(out)>=3,(inp,out)
        cyc=list(map(int,out[1:])); assert cyc[0]==cyc[-1],(inp,out)
        w={}
        for a,b,wt in E: w.setdefault((a,b),[]).append(wt)
        tot=0; ok=True
        for u,v in zip(cyc,cyc[1:]):
            cand=w.get((u,v),[])
            if not cand: ok=False; break
            tot+=min(cand)
        assert ok and tot<0,(inp,out,tot)
print("cycle stress: 150/150 PASS")
PY

echo "== stress: cowroad vs python mirror (120) =="
python3 - <<'PY'
import random, subprocess, heapq
R=random.Random(8)
for _ in range(120):
    n=R.randint(3,7); T=R.randint(0,5)
    a=[[R.randint(1,99) for _ in range(n)] for _ in range(n)]
    inp=f"{n} {T}\n"+'\n'.join(' '.join(map(str,r)) for r in a)+'\n'
    got=int(subprocess.run(['./.build/cowroad'],input=inp,capture_output=True,text=True).stdout)
    INF=10**18; dist=[[[INF]*3 for _ in range(n)] for _ in range(n)]
    dist[0][0][0]=0; pq=[(0,0,0,0)]
    while pq:
        d,r,c,k=heapq.heappop(pq)
        if d!=dist[r][c][k]: continue
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr,nc=r+dr,c+dc
            if 0<=nr<n and 0<=nc<n:
                nk=(k+1)%3; w=T+(a[nr][nc] if k==2 else 0)
                if d+w<dist[nr][nc][nk]:
                    dist[nr][nc][nk]=d+w; heapq.heappush(pq,(d+w,nr,nc,nk))
    assert got==min(dist[n-1][n-1]),(inp,got)
print("cowroad stress: 120/120 PASS")
PY
echo "== stress: high_score vs python mirror (150) =="
python3 - <<'PY'
import random, subprocess
from collections import deque
R=random.Random(11)
def mirror(n,E):
    INF=10**18; d=[INF]*(n+1); d[1]=0; touched=[]
    adj=[[] for _ in range(n+1)]
    for a,b,w in E: adj[a].append(b)
    for i in range(n):
        touched=[]
        for a,b,w in E:
            if d[a]<INF and d[a]-w<d[b]: d[b]=d[a]-w; touched.append(b)
    bad=[0]*(n+1); q=deque(touched)
    for v in touched: bad[v]=1
    while q:
        u=q.popleft()
        for v in adj[u]:
            if not bad[v]: bad[v]=1; q.append(v)
    return -1 if bad[n] else -d[n]
for _ in range(150):
    n=R.randint(2,8); m=R.randint(0,14)
    E=[(R.randint(1,n),R.randint(1,n),R.randint(-9,15)) for _ in range(m)]
    # keep cases where n is reachable from 1 (as CSES inputs guarantee)
    adj0=[[] for _ in range(n+1)]
    for a,b,_ in E: adj0[a].append(b)
    seen=[0]*(n+1); q=deque([1]); seen[1]=1
    while q:
        u=q.popleft()
        for v in adj0[u]:
            if not seen[v]: seen[v]=1; q.append(v)
    if not seen[n]: continue
    inp=f"{n} {m}\n"+"".join(f"{a} {b} {w}\n" for a,b,w in E)
    got=subprocess.run(['./.build/high_score'],input=inp,capture_output=True,text=True).stdout.strip()
    want=mirror(n,E)
    if want!=-1: assert got==str(want),(inp,got,want)
    else: assert got=='-1',(inp,got)
print("high_score stress: 150/150 PASS")
PY
echo "test_ch08: ALL PASS"

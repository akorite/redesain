#!/bin/bash
set -e
cd "$(dirname "$0")"
CXX=${CXX:-clang++}; F="-std=c++17 -O2 -Wall -Wextra"
mkdir -p .build
for p in counting_rooms labyrinth building_teams course_schedule planets_cycles; do
    $CXX $F -o .build/$p $p.cpp
done
expect() { echo "$3" | grep -qF "$2" || { echo "FAIL $1: wanted '$2' in: $3" >&2; exit 1; }; echo "$1 PASS"; }

echo "== fixed checks =="
expect rooms "3" "$(printf "5 8\n########\n#..#...#\n####.#.#\n#..#...#\n########\n" | ./.build/counting_rooms)"
expect labyrinth "YES" "$(printf "5 8\n########\n#.A#...#\n#.##.#B#\n#......#\n########\n" | ./.build/labyrinth | head -1)"
expect labyrinth-len "9" "$(printf "5 8\n########\n#.A#...#\n#.##.#B#\n#......#\n########\n" | ./.build/labyrinth | sed -n 2p)"
expect labyrinth-path "LDDRRRRRU" "$(printf "5 8\n########\n#.A#...#\n#.##.#B#\n#......#\n########\n" | ./.build/labyrinth | tail -1)"
expect teams "1 2 2 1 2" "$(printf "5 3\n1 2\n1 3\n4 5\n" | ./.build/building_teams)"
expect teams-imp "IMPOSSIBLE" "$(printf "3 3\n1 2\n2 3\n1 3\n" | ./.build/building_teams)"
expect course "3 4 1 5 2" "$(printf "5 3\n1 2\n3 1\n4 5\n" | ./.build/course_schedule)"
expect course-imp "IMPOSSIBLE" "$(printf "3 3\n1 2\n2 3\n3 1\n" | ./.build/course_schedule)"
expect planets "3 3 1 3 4" "$(printf "5\n2 4 3 1 4\n" | ./.build/planets_cycles)"

echo "== stress: rooms vs brute (150) =="
python3 - <<'PY'
import random, subprocess
for _ in range(150):
    n,m = random.randint(1,8), random.randint(1,8)
    g = [''.join(random.choice('.#') for _ in range(m)) for _ in range(n)]
    inp = f"{n} {m}\n"+'\n'.join(g)+"\n"
    got = int(subprocess.run(['./.build/counting_rooms'],input=inp,capture_output=True,text=True).stdout)
    seen=[[0]*m for _ in range(n)]; cnt=0
    for r in range(n):
        for c in range(m):
            if g[r][c]=='.' and not seen[r][c]:
                cnt+=1; stk=[(r,c)]; seen[r][c]=1
                while stk:
                    x,y=stk.pop()
                    for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<n and 0<=ny<m and g[nx][ny]=='.' and not seen[nx][ny]:
                            seen[nx][ny]=1; stk.append((nx,ny))
    assert got==cnt,(g,got,cnt)
print("rooms stress: 150/150 PASS")
PY

echo "== stress: planets vs brute (200) =="
python3 - <<'PY'
import random, subprocess
for _ in range(200):
    n = random.randint(1,10)
    t = [random.randint(1,n) for _ in range(n)]
    inp = f"{n}\n{' '.join(map(str,t))}\n"
    got = list(map(int,subprocess.run(['./.build/planets_cycles'],input=inp,capture_output=True,text=True).stdout.split()))
    want=[]
    for s in range(1,n+1):
        seen={s}; v=s; k=0
        while t[v-1] not in seen:
            seen.add(t[v-1]); v=t[v-1]; k+=1
        want.append(k+1)
    assert got==want,(t,got,want)
print("planets stress: 200/200 PASS")
PY

echo "== stress: labyrinth path valid + shortest (150) =="
python3 - <<'PY'
import random, subprocess
from collections import deque
D={'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}
R=random.Random(7)
for _ in range(150):
    while True:
        n,m=R.randint(3,8),R.randint(3,8)
        if (n-2)*(m-2)<2: continue
        g=[['#']*m]+[['#']+list('.'*(m-2))+['#'] for _ in range(n-2)]+[['#']*m]
        for i in range(1,n-1):
            for j in range(1,m-1):
                if R.random()<0.3: g[i][j]='#'
        free=[(i,j) for i in range(1,n-1) for j in range(1,m-1) if g[i][j]=='.']
        if len(free)>=2: break
    a,b=R.sample(free,2)
    g[a[0]][a[1]]='A'; g[b[0]][b[1]]='B'
    inp=f"{n} {m}\n"+'\n'.join(''.join(r) for r in g)+'\n'
    out=subprocess.run(['./.build/labyrinth'],input=inp,capture_output=True,text=True).stdout.split()
    dist=[[-1]*m for _ in range(n)]; dist[a[0]][a[1]]=0; q=deque([a])
    while q:
        x,y=q.popleft()
        for dx,dy in D.values():
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and dist[nx][ny]<0 and g[nx][ny]!='#':
                dist[nx][ny]=dist[x][y]+1; q.append((nx,ny))
    if dist[b[0]][b[1]]<0:
        assert out[0]=='NO',(inp,out)
    else:
        assert out[0]=='YES' and int(out[1])==dist[b[0]][b[1]] and len(out[2])==dist[b[0]][b[1]],(inp,out)
        x,y=a
        for mv in out[2]:
            dx,dy=D[mv]; x,y=x+dx,y+dy
            assert g[x][y]!='#',(inp,out)
        assert (x,y)==b,(inp,out)
print("labyrinth stress: 150/150 PASS")
PY

echo "== stress: course_schedule emits valid topo order (200) =="
python3 - <<'PY'
import random, subprocess
from collections import deque
R=random.Random(9)
for _ in range(200):
    n=R.randint(2,9); E=[]
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if R.random()<0.2: E.append((i,j))
    cyclic=False
    if R.random()<0.15 and E:                      # sometimes inject one back-edge
        a,b=R.choice(E); E.append((b,a)); cyclic=True
    inp=f"{n} {len(E)}\n"+''.join(f"{a} {b}\n" for a,b in E)
    out=subprocess.run(['./.build/course_schedule'],input=inp,capture_output=True,text=True).stdout.split()
    indeg=[0]*(n+1); adj=[[] for _ in range(n+1)]
    for a,b in E: adj[a].append(b); indeg[b]+=1
    q=deque(v for v in range(1,n+1) if indeg[v]==0); cnt=0
    while q:
        u=q.popleft(); cnt+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0: q.append(v)
    if cnt<n:
        assert out==['IMPOSSIBLE'],(inp,out)
    else:
        assert out!=['IMPOSSIBLE'] and len(out)==n,(inp,out)
        pos={int(v):k for k,v in enumerate(out)}
        assert sorted(pos)==list(range(1,n+1)),(inp,out)
        for a,b in E: assert pos[a]<pos[b],(inp,out,E)
print("course stress: 200/200 PASS")
PY
echo "test_ch07: ALL PASS"

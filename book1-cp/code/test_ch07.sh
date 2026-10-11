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
expect teams "1 2 2 1 2" "$(printf "5 3\n1 2\n1 3\n4 5\n" | ./.build/building_teams)"
expect teams-imp "IMPOSSIBLE" "$(printf "3 3\n1 2\n2 3\n1 3\n" | ./.build/building_teams)"
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
echo "test_ch07: ALL PASS"

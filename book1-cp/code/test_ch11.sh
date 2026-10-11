#!/bin/bash
set -e; cd "$(dirname "$0")"; CXX=${CXX:-clang++}; F="-std=c++17 -O2 -Wall -Wextra"; mkdir -p .build
for p in minimizing_coins coin_combos book_shop increasing_subseq grid_paths; do $CXX $F -o .build/$p $p.cpp; done
expect() { echo "$3" | grep -qF "$2" || { echo "FAIL $1: wanted '$2' in: $3" >&2; exit 1; }; echo "$1 PASS"; }
expect coins "3" "$(printf "3 11\n1 5 7\n" | ./.build/minimizing_coins)"
expect combos "8 3" "$(printf "3 9\n2 3 5\n" | ./.build/coin_combos)"
expect shop "13" "$(printf "4 10\n4 8 5 3\n5 12 8 1\n" | ./.build/book_shop)"
expect shoptake "1 3" "$(printf "4 10\n4 8 5 3\n5 12 8 1\n" | ./.build/book_shop | tail -1)"
expect lis "4" "$(printf "8\n7 3 5 3 6 2 9 8\n" | ./.build/increasing_subseq)"
expect grid "3" "$(printf "4\n....\n.*..\n...*\n*...\n" | ./.build/grid_paths)"
python3 - <<'PY'
import random,subprocess
for _ in range(150):
    n=random.randint(1,6);X=random.randint(1,30)
    c=[random.randint(1,8) for _ in range(n)]
    inp=f"{n} {X}\n{' '.join(map(str,c))}\n"
    dp=[10**9]*(X+1);dp[0]=0
    for s in range(1,X+1):
        for v in c:
            if s>=v:dp[s]=min(dp[s],dp[s-v]+1)
    got=subprocess.run(['./.build/minimizing_coins'],input=inp,capture_output=True,text=True).stdout.strip()
    want=str(dp[X] if dp[X]<10**9 else -1)
    assert got==want,(inp,got,want)
print("coins stress: 150/150 PASS")
import bisect
for _ in range(150):
    n=random.randint(1,15)
    a=[random.randint(1,20) for _ in range(n)]
    L=[]
    for x in a:
        i=bisect.bisect_left(L,x)
        if i==len(L):L.append(x)
        else:L[i]=x
    inp=f"{n}\n{' '.join(map(str,a))}\n"
    got=subprocess.run(['./.build/increasing_subseq'],input=inp,capture_output=True,text=True).stdout.strip()
    assert int(got)==len(L),(inp,got,len(L))
print("lis stress: 150/150 PASS")
for _ in range(150):
    n=random.randint(1,6);X=random.randint(1,25)
    w=[random.randint(1,10) for _ in range(n)]
    v=[random.randint(1,15) for _ in range(n)]
    inp=f"{n} {X}\n{' '.join(map(str,w))}\n{' '.join(map(str,v))}\n"
    dp=[[0]*(X+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for x in range(X,-1,-1):
            dp[i][x]=dp[i-1][x]
            if x>=w[i-1]:dp[i][x]=max(dp[i][x],dp[i-1][x-w[i-1]]+v[i-1])
    got=subprocess.run(['./.build/book_shop'],input=inp,capture_output=True,text=True).stdout.strip().split('\n')
    assert int(got[0])==dp[n][X],(inp,got,dp[n][X])
    take=[int(t) for t in got[1].split()] if len(got)>1 and got[1].strip() else []
    assert sum(w[i-1] for i in take)<=X,(inp,got)          # take fits
    assert sum(v[i-1] for i in take)==dp[n][X],(inp,got)  # take achieves max
    assert len(set(take))==len(take) and all(1<=i<=n for i in take),(inp,got)
print("knapsack stress: 150/150 PASS (value + take-table validity)")
for _ in range(120):
    n=random.randint(1,7)
    g=[['.' if random.random()<0.75 else '*' for _ in range(n)] for _ in range(n)]
    inp=f"{n}\n"+'\n'.join(''.join(r) for r in g)+'\n'
    dp=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if g[i][j]=='*':continue
            dp[i][j]=(1 if i==j==0 else 0)+((dp[i-1][j] if i>0 else 0)+(dp[i][j-1] if j>0 else 0))
            dp[i][j]%=10**9+7
    got=subprocess.run(['./.build/grid_paths'],input=inp,capture_output=True,text=True).stdout.strip()
    assert int(got)==dp[n-1][n-1],(inp,got,dp[n-1][n-1])
print("grid stress: 120/120 PASS")
PY
echo "test_ch11: ALL PASS"

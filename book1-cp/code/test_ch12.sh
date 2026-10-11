#!/bin/bash
set -e; cd "$(dirname "$0")"; CXX=${CXX:-clang++}; F="-std=c++17 -O2 -Wall -Wextra"; mkdir -p .build
for p in elevator_rides counting_numbers removal_game edit_distance money_sums tree_matching; do $CXX $F -o .build/$p $p.cpp; done
expect() { echo "$3" | grep -qF "$2" || { echo "FAIL $1: wanted '$2' in: $3" >&2; exit 1; }; echo "$1 PASS"; }
expect elev "2" "$(printf "4 10\n4 8 6 1\n" | ./.build/elevator_rides)"
expect num "171" "$(printf "123 321\n" | ./.build/counting_numbers)"
expect rem "8" "$(printf "4\n4 5 1 3\n" | ./.build/removal_game)"
expect edit "2" "$(printf "LOVE\nMOVIE\n" | ./.build/edit_distance)"
expect money "6" "$(printf "3\n2 3 5\n" | ./.build/money_sums | head -1)"
expect match "2" "$(printf "5\n1 2\n1 3\n3 4\n3 5\n" | ./.build/tree_matching)"
python3 - <<'PY'
import random,subprocess
for _ in range(150):
    n=random.randint(1,7);X=random.randint(1,15)
    w=[random.randint(1,10) for _ in range(n)]
    inp=f"{n} {X}\n{' '.join(map(str,w))}\n"
    N=1<<n;dp=[(99,0)]*N;dp[0]=(1,0)
    for m in range(1,N):
        best=(99,0)
        for i in range(n):
            if m>>i&1:
                r,cap=dp[m^(1<<i)]
                c=(r,cap+w[i]) if cap+w[i]<=X else (r+1,w[i])
                best=min(best,c)
        dp[m]=best
    got=subprocess.run(['./.build/elevator_rides'],input=inp,capture_output=True,text=True).stdout.strip()
    assert int(got)==dp[N-1][0],(inp,got,dp[N-1])
print("elevator stress: 150/150 PASS")
for _ in range(120):
    a=random.randint(0,10**5); b=a+random.randint(0,4000)
    inp=f"{a} {b}\n"
    def ok(x):
        s=str(x)
        return all(s[i]!=s[i+1] for i in range(len(s)-1))
    want=sum(ok(i) for i in range(a,b+1))
    got=subprocess.run(['./.build/counting_numbers'],input=inp,capture_output=True,text=True).stdout.strip()
    assert int(got)==want,(inp,got,want)
print("numbers stress (adjacent-digit brute): 120/120 PASS")
for _ in range(120):
    n=random.randint(1,9)
    a=[random.randint(1,20) for _ in range(n)]
    inp=f"{n}\n{' '.join(map(str,a))}\n"
    dp=[[0]*n for _ in range(n)]
    for i in range(n):dp[i][i]=a[i]
    for l in range(2,n+1):
        for i in range(n-l+1):
            j=i+l-1
            dp[i][j]=max(a[i]-dp[i+1][j],a[j]-dp[i][j-1])
    want=(sum(a)+dp[0][n-1])//2
    got=subprocess.run(['./.build/removal_game'],input=inp,capture_output=True,text=True).stdout.strip()
    assert int(got)==want,(inp,got,want)
print("removal stress: 120/120 PASS")
for _ in range(100):
    def rs(): return ''.join(random.choice('ab') for _ in range(random.randint(1,8)))
    s,t=rs(),rs()
    n,m=len(s),len(t)
    D=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):D[i][0]=i
    for j in range(m+1):D[0][j]=j
    for i in range(1,n+1):
        for j in range(1,m+1):
            D[i][j]=min(D[i-1][j]+1,D[i][j-1]+1,D[i-1][j-1]+(s[i-1]!=t[j-1]))
    inp=f"{s}\n{t}\n"
    got=subprocess.run(['./.build/edit_distance'],input=inp,capture_output=True,text=True).stdout.strip()
    assert int(got)==D[n][m],(inp,got,D[n][m])
print("edit stress: 100/100 PASS")
for _ in range(120):
    n=random.randint(1,8)
    c=[random.randint(1,15) for _ in range(n)]
    reach={0}
    for w in c:reach|={s+w for s in reach if s+w<=200}
    inp=f"{n}\n{' '.join(map(str,c))}\n"
    out=subprocess.run(['./.build/money_sums'],input=inp,capture_output=True,text=True).stdout.split()
    want=sorted(x for x in reach if x>0)
    assert list(map(int,out[1:]))==want,(inp,out,want)
print("money stress: 120/120 PASS")
PY
echo "test_ch12: ALL PASS"

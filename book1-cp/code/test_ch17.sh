#!/bin/bash
set -e; cd "$(dirname "$0")"; CXX=${CXX:-clang++}; F="-std=c++17 -O2 -Wall -Wextra"; mkdir -p .build
for p in dice_probability throwing_dice candy_lottery inversion_prob moving_robots coupon_collector; do $CXX $F -o .build/$p $p.cpp; done
expect() { echo "$3" | grep -qF -- "$2" || { echo "FAIL $1: wanted '$2' in: $3" >&2; exit 1; }; echo "$1 PASS"; }
expect dice "0.194444" "$(printf "2 9 10\n" | ./.build/dice_probability)"
expect throw "125" "$(printf "8\n" | ./.build/throwing_dice)"
expect throw100 "201345653" "$(printf "100\n" | ./.build/throwing_dice)"
expect robots "23.120740" "$(printf "10\n" | ./.build/moving_robots)"
expect candy "2.444444" "$(printf "2 3\n" | ./.build/candy_lottery)"
expect inv "1.057143" "$(printf "3\n5 2 7\n" | ./.build/inversion_prob)"
expect coupon "exact   14.700000" "$(printf "6\n" | ./.build/coupon_collector)"
python3 - <<'PY'
import random, subprocess, itertools
R=random.Random(3)
def close(a,b,t=1e-5): return abs(a-b)<t
# dice: enumerate for n<=4, DP mirror for bigger
for _ in range(80):
    n=R.randint(1,5); hi=6*n; a=R.randint(1,hi); b=R.randint(a,hi)
    if n<=4:
        tot=sum(1 for t in itertools.product(range(1,7),repeat=n) if a<=sum(t)<=b)/6**n
    else:
        dp=[1.0]+[0.0]*hi
        for i in range(n):
            nd=[0.0]*(hi+1)
            for s in range(6*i+1):
                for f in range(1,7): nd[s+f]+=dp[s]/6
            dp=nd
        tot=sum(dp[a:b+1])
    inp=f"{n} {a} {b}\n"
    got=float(subprocess.run(['./.build/dice_probability'],input=inp,capture_output=True,text=True).stdout)
    assert close(got,tot),(inp,got,tot)
print("dice stress: 80/80 PASS")
for _ in range(80):
    n=R.randint(1,40)
    M=10**9+7; dp=[0]*(n+7); dp[0]=1
    for i in range(1,n+1):
        dp[i]=sum(dp[max(0,i-6):i])%M
    inp=f"{n}\n"
    got=subprocess.run(['./.build/throwing_dice'],input=inp,capture_output=True,text=True).stdout.strip()
    assert got==str(dp[n]),(inp,got,dp[n])
print("throwing stress: 80/80 PASS")
for _ in range(80):
    n=R.randint(1,6); k=R.randint(1,8)
    want=sum(1-((v-1)/k)**n for v in range(1,k+1))
    if n<=3 and k<=5:  # brute cross-check
        tot=sum(max(t) for t in itertools.product(range(1,k+1),repeat=n))/k**n
        assert close(want,tot)
    inp=f"{n} {k}\n"
    got=float(subprocess.run(['./.build/candy_lottery'],input=inp,capture_output=True,text=True).stdout)
    assert close(got,want),(inp,got,want)
print("candy stress: 80/80 PASS")
for _ in range(80):
    n=R.randint(2,8); r=[R.randint(1,20) for _ in range(n)]
    want=0.0
    for a in range(n):
        for b in range(a+1,n):
            cnt=sum(min(va-1,r[b]) for va in range(1,r[a]+1))
            want+=cnt/(r[a]*r[b])
    inp=f"{n}\n"+' '.join(map(str,r))+'\n'
    got=float(subprocess.run(['./.build/inversion_prob'],input=inp,capture_output=True,text=True).stdout)
    assert close(got,want),(inp,got,want)
print("inversion stress: 80/80 PASS")
# robots: python mirror (same math) + degenerate k=0 sanity (expect 0 empties)
inp="0\n"
got=subprocess.run(['./.build/moving_robots'],input=inp,capture_output=True,text=True).stdout.strip()
assert got=="0.000000",(inp,got)
for k in [1,3,7]:
    adj=[[] for _ in range(64)]
    for r in range(8):
        for c in range(8):
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                nr,nc=r+dr,c+dc
                if 0<=nr<8 and 0<=nc<8: adj[r*8+c].append(nr*8+nc)
    ne=[1.0]*64
    for t in range(64):
        cur=[0.0]*64; cur[t]=1.0
        for _s in range(k):
            nxt=[0.0]*64
            for s in range(64):
                for v in adj[s]: nxt[v]+=cur[s]/len(adj[s])
            cur=nxt
        for s in range(64): ne[s]*=(1-cur[s])
    want=sum(ne)
    inp=f"{k}\n"
    got=float(subprocess.run(['./.build/moving_robots'],input=inp,capture_output=True,text=True).stdout)
    assert close(got,want,1e-6),(inp,got,want)
print("robots stress: k=0 sanity + 3 mirrors PASS")
PY
echo "test_ch17: ALL PASS"

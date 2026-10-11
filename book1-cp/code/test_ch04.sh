#!/bin/bash
# test_ch04.sh -- fixed CSES/USACO checks + stress harness for chapter 4.
set -e
cd "$(dirname "$0")"
CXX=${CXX:-clang++}; F="-std=c++17 -O2 -Wall -Wextra"
mkdir -p .build
for p in bsearch_template factory_machines array_division \
         social_distancing mult_table real_bsearch; do
    $CXX $F -o .build/$p $p.cpp
done

echo "== fixed checks =="
printf "3 7\n3 2 5\n" | ./.build/factory_machines | tail -1 | grep -qx 8 && echo "factory PASS"
printf "5 3\n2 4 7 3 5\n" | ./.build/array_division | tail -1 | grep -qx 8 && echo "arrdiv PASS"
echo 3 | ./.build/mult_table | grep -qx 3 && echo "mult PASS"
printf "5 3\n1 2 5 8 9\n" | ./.build/social_distancing | tail -1 | grep -qx 4 && echo "social PASS"
./.build/bsearch_template | diff - <(printf "first >= 7 at index 2 (a[2]=7)\nfirst >  7 at index 4 (a[4]=11)\nlower_bound agrees: 2\n") && echo "template PASS"
./.build/real_bsearch | tail -1 | grep -q "1.4142135623730" && echo "real PASS"

echo "== stress: factory vs linear scan (300 rounds) =="
python3 - <<'PY'
import random, subprocess
for _ in range(300):
    n = random.randint(1,6); t = random.randint(1,60)
    a = [random.randint(1,9) for _ in range(n)]
    inp = f"{n} {t}\n{' '.join(map(str,a))}\n"
    got = int(subprocess.run(['./.build/factory_machines'], input=inp,
              capture_output=True, text=True).stdout.strip().split('\n')[-1])
    T = 1
    while sum(T//x for x in a) < t: T += 1
    assert got == T, (a, t, got, T)
print("factory stress: 300/300 PASS")
PY

echo "== stress: array division vs DP brute (200 rounds, n<=12) =="
python3 - <<'PY'
import random, subprocess
def brute(a, k):
    n = len(a); INF = 10**18
    dp = [[INF]*(n+1) for _ in range(k+1)]
    dp[0][0] = 0; pre = [0]
    for x in a: pre.append(pre[-1]+x)
    for g in range(1,k+1):
        for i in range(g, n+1):
            for j in range(i):
                dp[g][i] = min(dp[g][i], max(dp[g-1][j], pre[i]-pre[j]))
    return dp[k][n]
for _ in range(200):
    n = random.randint(1,12); k = random.randint(1,n)
    a = [random.randint(1,20) for _ in range(n)]
    inp = f"{n} {k}\n{' '.join(map(str,a))}\n"
    got = int(subprocess.run(['./.build/array_division'], input=inp,
              capture_output=True, text=True).stdout.strip().split('\n')[-1])
    assert got == brute(a,k), (a,k,got,brute(a,k))
print("arrdiv stress: 200/200 PASS")
PY

echo "== stress: social distancing vs subset brute (200 rounds, n<=9) =="
python3 - <<'PY'
import itertools, random, subprocess
def brute(p, k):
    best = 0
    for sub in itertools.combinations(p, k):
        gaps = [sub[i+1]-sub[i] for i in range(k-1)]
        best = max(best, min(gaps) if gaps else 10**9)
    return best
for _ in range(200):
    n = random.randint(3,9); k = random.randint(2,n)
    p = sorted(random.sample(range(1,30), n))
    inp = f"{n} {k}\n{' '.join(map(str,p))}\n"
    got = int(subprocess.run(['./.build/social_distancing'], input=inp,
              capture_output=True, text=True).stdout.strip().split('\n')[-1])
    assert got == brute(p,k), (p,k,got,brute(p,k))
print("social stress: 200/200 PASS")
PY

echo "== stress: mult table vs direct enumeration (n<=40) =="
python3 - <<'PY'
import random, subprocess
for n in [3,5,7,9,15,33,39]:
    got = int(subprocess.run(['./.build/mult_table'], input=f"{n}\n",
              capture_output=True, text=True).stdout)
    flat = sorted(i*j for i in range(1,n+1) for j in range(1,n+1))
    assert got == flat[(n*n-1)//2] == flat[len(flat)//2], (n, got)
print("mult stress: 7/7 PASS")
PY
echo "test_ch04: ALL PASS"

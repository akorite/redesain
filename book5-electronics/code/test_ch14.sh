#!/bin/bash
set -e; cd "$(dirname "$0")"; CXX=${CXX:-clang++}; F="-std=c++17 -O2 -Wall -Wextra"; mkdir -p .build
for p in counting_divisors exponentiation2 binomial_coefficients distributing_apples christmas_party fibonacci; do $CXX $F -o .build/$p $p.cpp; done
expect() { echo "$3" | grep -qF "$2" || { echo "FAIL $1: wanted '$2' in: $3" >&2; exit 1; }; echo "$1 PASS"; }
expect div "5" "$(printf "3\n16\n17\n18\n" | ./.build/counting_divisors | head -1)"
expect exp2 "2187" "$(printf "1\n3 7 1\n" | ./.build/exponentiation2)"
expect ncr "846527861" "$(printf "1\n40 20\n" | ./.build/binomial_coefficients)"
expect apples "15" "$(printf "4 3\n" | ./.build/distributing_apples)"
expect christmas "9" "$(printf "4\n" | ./.build/christmas_party)"
expect fib "55" "$(printf "10\n" | ./.build/fibonacci)"
python3 - <<'PY'
import random,subprocess,math
M=10**9+7
# divisors vs python factorization
for _ in range(150):
    x=random.randint(1,10**6)
    inp=f"1\n{x}\n"
    want=1;t=x;d=2
    tt=t
    while d*d<=tt:
        e=0
        while tt%d==0:tt//=d;e+=1
        want*=e+1;d+=1
    if tt>1:want*=2
    got=subprocess.run(['./.build/counting_divisors'],input=inp,capture_output=True,text=True).stdout.strip()
    assert int(got)==want,(inp,got,want)
print("divisors stress: 150/150 PASS")
# exp2 vs python pow
for _ in range(150):
    a,b,c=[random.randint(0,10**8) for _ in range(3)]
    inp=f"1\n{a} {b} {c}\n"
    want=pow(a,pow(b,c,M-1),M)
    got=subprocess.run(['./.build/exponentiation2'],input=inp,capture_output=True,text=True).stdout.strip()
    assert int(got)==want,(inp,got,want)
print("exp2 stress: 150/150 PASS")
# ncr + apples vs math.comb
for _ in range(120):
    a=random.randint(0,10**4);b=random.randint(0,a)
    inp=f"1\n{a} {b}\n"
    want=math.comb(a,b)%M
    got=subprocess.run(['./.build/binomial_coefficients'],input=inp,capture_output=True,text=True).stdout.strip()
    assert int(got)==want,(inp,got,want)
print("ncr stress: 120/120 PASS")
for _ in range(100):
    n=random.randint(1,50);m=random.randint(1,20)
    inp=f"{n} {m}\n"
    want=math.comb(n+m-1,m-1)%M
    got=subprocess.run(['./.build/distributing_apples'],input=inp,capture_output=True,text=True).stdout.strip()
    assert int(got)==want,(inp,got,want)
print("apples stress: 100/100 PASS")
# derangements vs python recurrence + brute check for small n
from itertools import permutations
for _ in range(120):
    n=random.randint(0,12)
    inp=f"{n}\n"
    d=[1,0]+[0]*(n)
    for i in range(2,n+1):d[i]=(i-1)*(d[i-1]+d[i-2])%M
    want=d[max(1,n)] if n>0 else 1
    if n<=7:
        want=sum(1 for p in permutations(range(n)) if all(p[i]!=i for i in range(n)))%M
    got=subprocess.run(['./.build/christmas_party'],input=inp,capture_output=True,text=True).stdout.strip()
    assert int(got)==want,(inp,got,want)
print("christmas stress: 120/120 PASS")
# fib vs python fast doubling
def fib(n):
    if n==0:return (0,1)
    a,b=fib(n//2)
    c=(a*(2*b-a))%M;dd=(a*a+b*b)%M
    return (c,dd) if n%2==0 else (dd,(c+dd)%M)
for _ in range(120):
    n=random.randint(0,10**15)
    inp=f"{n}\n"
    got=subprocess.run(['./.build/fibonacci'],input=inp,capture_output=True,text=True).stdout.strip()
    assert int(got)==fib(n)[0],(inp,got,fib(n)[0])
print("fib stress: 120/120 PASS")
PY
echo "test_ch14: ALL PASS"

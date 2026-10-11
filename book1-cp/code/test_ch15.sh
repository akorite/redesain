#!/bin/bash
set -e; cd "$(dirname "$0")"; CXX=${CXX:-clang++}; F="-std=c++17 -O2 -Wall -Wextra"; mkdir -p .build
for p in string_matching borders periods word_combinations minimal_rotation hash_demo; do $CXX $F -o .build/$p $p.cpp; done
expect() { echo "$3" | grep -qF "$2" || { echo "FAIL $1: wanted '$2' in: $3" >&2; exit 1; }; echo "$1 PASS"; }
expect match   "2 2"    "$(printf 'saippuakauppias\npp\n' | ./.build/string_matching)"
expect borders "2 5"    "$(printf 'abcababcab\n' | ./.build/borders)"
expect periods "3 6 7"  "$(printf 'abcabca\n' | ./.build/periods)"
expect words   "2"      "$(printf 'ababc\n4\nab\nabab\nc\ncb\n' | ./.build/word_combinations)"
expect rot     "abac"   "$(printf 'acab\n' | ./.build/minimal_rotation)"
expect demo    "both hash to 24" "$(./.build/hash_demo)"
python3 - <<'PY'
import random,subprocess
R=random.Random(15)
def run(p,inp): return subprocess.run(['./.build/'+p],input=inp,capture_output=True,text=True).stdout.strip()
def borders_py(s):
    n=len(s); return ' '.join(str(k) for k in range(1,n) if s[:k]==s[n-k:])
def periods_py(s):
    n=len(s); return ' '.join(str(k) for k in range(1,n+1) if all(s[i]==s[i+k] for i in range(n-k)))
def matches_py(s,p):
    c=0;i=s.find(p)
    while i>=0: c+=1;i=s.find(p,i+1)
    return c
def words_py(s,W):
    M=10**9+7;n=len(s);dp=[0]*(n+1);dp[n]=1
    for i in range(n-1,-1,-1):
        for w in W:
            if s.startswith(w,i): dp[i]=(dp[i]+dp[i+len(w)])%M
    return dp[0]
def rot_py(s):
    return min(s[i:]+s[:i] for i in range(len(s)))
for _ in range(200):
    n,m=R.randint(1,60),R.randint(1,4)
    s=''.join(R.choice('abc') for _ in range(n)); p=''.join(R.choice('abc') for _ in range(m))
    got=run('string_matching',f'{s}\n{p}\n').split()
    w=matches_py(s,p)
    assert got==[str(w),str(w)], (s,p,got,w)
    s2=''.join(R.choice('ab') for _ in range(R.randint(1,40)))
    got=run('borders',s2+'\n'); w=borders_py(s2)
    assert got==w or (got=='' and w==''), (s2,got,w)
    s3=''.join(R.choice('ab') for _ in range(R.randint(1,40)))
    assert run('periods',s3+'\n')==periods_py(s3), s3
    n=R.randint(1,30); s4=''.join(R.choice('ab') for _ in range(n))
    W=list({''.join(R.choice('ab') for _ in range(R.randint(1,4))) for _ in range(R.randint(1,4))})
    got=run('word_combinations',f'{s4}\n{len(W)}\n'+'\n'.join(W)+'\n')
    assert got==str(words_py(s4,W)), (s4,W,got)
    s5=''.join(R.choice('abc') for _ in range(R.randint(1,60)))
    assert run('minimal_rotation',s5+'\n')==rot_py(s5), s5
print('ALL STRESS PASS (200 rounds x 5 checks)')
PY

#!/bin/bash
# test_ch02.sh -- fixed-case checks + stress harness for chapter 2 code.
set -e
cd "$(dirname "$0")"
CXX=${CXX:-clang++}; FLAGS="-std=c++17 -O2 -Wall -Wextra"
mkdir -p .build
for f in subsets_rec subsets_mask apple_division apple_bench creating_strings perms_demo queens milk_pails size_ladder gray_code; do
    $CXX $FLAGS -o .build/$f $f.cpp
done
B=.build
fail=0
check() { # name expected actual
    if [ "$2" == "$3" ]; then echo "PASS  $1"; else echo "FAIL  $1: want '$2' got '$3'"; fail=1; fi
}

# -- fixed cases ---------------------------------------------------------
check "subsets_rec n=3 count" "8" "$($B/subsets_rec | wc -l | tr -d ' ')"
check "subsets_mask n=3 count" "8" "$($B/subsets_mask | wc -l | tr -d ' ')"
check "rec==mask sets" "same" "$(diff <($B/subsets_rec | sort) <($B/subsets_mask | sort) >/dev/null && echo same || echo diff)"
check "apple sample" "1" "$(echo '5
3 2 7 4 1' | $B/apple_division)"
check "apple equal halves" "0" "$(echo '4
1 1 1 1' | $B/apple_division)"
check "apple n=1" "7" "$(echo '1
7' | $B/apple_division)"
check "creating aabac count" "20" "$(echo aabac | $B/creating_strings | head -1)"
check "creating abc count" "6" "$(echo abc | $B/creating_strings | head -1)"
check "creating aaa count" "1" "$(echo aaa | $B/creating_strings | head -1)"
check "creating sorted" "yes" "$(echo aabac | $B/creating_strings | tail -n +2 | sort -c 2>/dev/null && echo yes)"
check "milk pails sample" "76" "$(echo '17 25 77' | $B/milk_pails)"
check "milk pails exact" "100" "$(echo '10 10 100' | $B/milk_pails)"
check "queens empty board" "92" "$($B/queens | head -1 | grep -o 'leaves=[0-9]*' | cut -d= -f2)"
check "queens cses board" "65" "$(printf '........\n........\n..*.....\n........\n........\n.....**.\n...*....\n........\n' | $B/queens stdin | head -1 | grep -o 'leaves=[0-9]*' | cut -d= -f2)"

# -- pruning really prunes -----------------------------------------------
full=$($B/queens | head -1 | grep -o 'nodes=[0-9]*' | cut -d= -f2)
colonly=$($B/queens | tail -1 | grep -o 'nodes=[0-9]*' | cut -d= -f2)
check "diag prune cuts nodes ($colonly > $full)" "yes" "$([ $colonly -gt $full ] && echo yes)"

# -- stress: recursive bitmask solver vs lib-style fixed0 ----------------
python3 - <<'PY'
import itertools, random, subprocess
random.seed(7)
ok = 0
for t in range(200):
    n = random.randint(1, 12)
    w = [random.randint(1, 50) for _ in range(n)]
    want = min(abs(sum(w) - 2 * sum(w[i] for i in range(1, n) if (m >> (i-1)) & 1) + 0) if n > 1 else sum(w)
               for m in range(1 << max(0, n-1))) if n > 1 else w[0]
    got = int(subprocess.run(['.build/apple_division'], input=f'{n}\n{" ".join(map(str,w))}\n',
                             capture_output=True, text=True).stdout)
    assert got == want, (n, w, want, got)
    ok += 1
print(f'stress: {ok}/200 random cases agree with independent enumeration')
PY
echo "----"
[ $fail -eq 0 ] && echo "ALL CHECKS PASSED" || echo "SOME CHECKS FAILED"
exit $fail
check gray_code "00
01
11
10" "$(echo 2 | $B/gray_code)"

#!/usr/bin/env bash
# stress.sh -- Chapter 18 stress harness: gen -> fast vs brute -> verdict.
# Usage: bash stress.sh FAST BINARY  (default: mss_buggy), rounds default 500.
set -u
cd "$(dirname "$0")"
CXX=${CXX:-clang++}
FAST=${1:-mss_buggy}
ROUNDS=${2:-500}
mkdir -p .build
$CXX -std=c++17 -O2 -o .build/gen_mss gen_mss.cpp
$CXX -std=c++17 -O2 -o .build/brute  mss_brute.cpp
$CXX -std=c++17 -O2 -o .build/fast   "$FAST.cpp" || exit 1

for ((s = 1; s <= ROUNDS; s++)); do
    ./.build/gen_mss "$s" > .build/in.txt
    want=$(./.build/brute < .build/in.txt)
    got=$(./.build/fast < .build/in.txt)
    if [ "$want" != "$got" ]; then
        echo "MISMATCH seed=$s  brute=$want  fast=$got"
        echo "input:"; cat .build/in.txt
        exit 1
    fi
done
echo "stress: $ROUNDS/$ROUNDS rounds identical ($FAST vs mss_brute)"

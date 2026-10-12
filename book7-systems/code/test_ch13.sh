#!/bin/bash
# test_ch13.sh -- builds and runs ch13's code and checks the claimed outputs.
cd "$(dirname "$0")" || exit 1
T=$(mktemp -d) || exit 1
trap 'rm -rf "$T"' EXIT
fail() { echo "ch13 FAIL: $1"; exit 1; }

for p in race lockscale partition prodcons; do
  gcc -O2 -w -pthread -o "$T/$p" "ch13_$p.c" || fail "compile $p"
done
if gcc -O2 -w -pthread -o "$T/deadlock" "ch13_deadlock.c" 2>/dev/null; then HAVE_DEADLOCK=1; else HAVE_DEADLOCK=0; fi

# 1. the unprotected counter must lose updates (three tries; any single lucky run is allowed)
lost=0
for i in 1 2 3; do
  l=$("$T/race" | sed -n 's/.*lost \([0-9]*\)).*/\1/p')
  [ -n "$l" ] || fail "race output"
  [ "$l" -gt 0 ] && lost=1
done
[ "$lost" = 1 ] || fail "race never lost an update in 3 runs"

# 2. lockscale prints 4 rows, T = 1 2 4 8, and the three columns
"$T/lockscale" > "$T/ls.out" || fail "lockscale"
[ "$(grep -cE '^ *(1|2|4|8) ' "$T/ls.out")" = 4 ] || fail "lockscale rows"

# 3. condition variable: while-loop version never wakes on an empty queue
"$T/prodcons" while > "$T/pc.out" || fail "prodcons while"
grep -q "produced=200000 consumed=200000 empty-queue wakeups=0" "$T/pc.out" || fail "while version"
# the if-version is the bug; it only shows under load, so try a few times
seen=0
for i in 1 2 3 4 5; do
  w=$("$T/prodcons" if | sed -n 's/.*wakeups=\([0-9]*\)/\1/p')
  [ -n "$w" ] && [ "$w" -gt 0 ] && seen=1 && break
done
[ "$seen" = 1 ] || echo "ch13 note: if-version showed no bad wakeup in 5 tries (timing dependent)"

# 4. deadlock: opposite order -> both stuck; global order -> none
if [ "$HAVE_DEADLOCK" = 1 ]; then
  "$T/deadlock" bad  | grep -q "opposite order: 2 thread(s) stuck" || fail "deadlock bad"
  "$T/deadlock" good | grep -q "global order: 0 thread(s) stuck"   || fail "deadlock good"
else
  echo "ch13 note: pthread_barrier/timedlock absent (macOS), deadlock check skipped"
fi

# 5. false sharing: needs >= 2 cores; adjacent counters must be clearly slower at 4 threads
if [ "$(nproc)" -ge 4 ]; then
  "$T/partition" > "$T/part.out" || fail "partition"
  awk '$1==4 {exit !($2 > 1.2*$3)}' "$T/part.out" || fail "no false-sharing slowdown at 4 threads: $(grep '^ *4' "$T/part.out")"
else
  echo "ch13 note: fewer than 4 cores, false-sharing check skipped"
fi

echo "ch13 PASS"

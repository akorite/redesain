#!/bin/bash
# test_ch12.sh -- builds and runs ch12's code and checks the claimed outputs.
cd "$(dirname "$0")" || exit 1
T=$(mktemp -d) || exit 1
trap 'rm -rf "$T"' EXIT
fail() { echo "ch12 FAIL: $1"; exit 1; }

for p in fork_demo zombie pipeline cow ctx_switch; do
  gcc -O2 -w -o "$T/$p" "ch12_$p.c" || fail "compile $p"
done

"$T/fork_demo" > "$T/fork.out" || fail "fork_demo exit"
grep -q "hello from exec'd child" "$T/fork.out" || fail "fork_demo exec output"
grep -q "status=0" "$T/fork.out" || fail "fork_demo status"

if [ -d /proc ]; then
  "$T/zombie" > "$T/z.out" || fail "zombie exit"
  grep -q "before waitpid: child state = Z" "$T/z.out" || fail "zombie state not Z"
  grep -q "exit status = 7" "$T/z.out" || fail "zombie status"
  grep -q "after  waitpid: child state = -" "$T/z.out" || fail "zombie not reaped"
else
  echo "ch12 note: /proc absent (macOS), zombie check skipped"
fi

"$T/pipeline" > "$T/p.out" || fail "pipeline exit"
[ "$(head -1 "$T/p.out" | tr -d ' ')" = "14" ] || fail "pipeline wc -c != 14"
grep -q "reaped 3 children" "$T/p.out" || fail "pipeline child count"

gcc -O2 -w -DLEAK -o "$T/pipe_leak" ch12_pipeline.c || fail "compile pipe_leak"
timeout 2 "$T/pipe_leak" > /dev/null 2>&1; [ $? = 124 ] || fail "leaky pipeline should hang (exit 124)"

"$T/cow" > "$T/c.out" || fail "cow exit"
grep -q "child : fork returned 0, x=101" "$T/c.out" || fail "cow child"
grep -q "x=100" "$T/c.out" || fail "cow parent x"
a=$(sed -n 's/.*&x=\(0x[0-9a-f]*\).*/\1/p' "$T/c.out" | sort -u | wc -l | tr -d ' ')
[ "$a" = "1" ] || fail "cow: addresses differ"

python3 ch12_sched_sim.py > "$T/sim.out" || fail "sim"
grep -E '^fifo +127.5 +77.5 ' "$T/sim.out" > /dev/null || fail "fifo"
grep -E '^sjf +122.5 +72.5 ' "$T/sim.out" > /dev/null || fail "sjf"
grep -E '^stcf +82.5 +5.0 +5 ' "$T/sim.out" > /dev/null || fail "stcf"
grep -E '^rr +107.5 +7.5 +17 ' "$T/sim.out" > /dev/null || fail "rr"
grep -E '^sjf +87.5 +37.5 ' "$T/sim.out" > /dev/null || fail "sjf t0"
grep -E '^fifo +142.5 +92.5 ' "$T/sim.out" > /dev/null || fail "fifo t0"

# context switch: only check that a plausible number is printed (hardware-dependent)
us=$("$T/ctx_switch" 1 | sed -n 's/.* \([0-9.]*\) us per ctx switch.*/\1/p')
[ -n "$us" ] || fail "ctx_switch output"
awk -v u="$us" 'BEGIN{exit !(u>0.2 && u<500)}' || fail "ctx_switch out of range: $us"

echo "ch12 PASS"

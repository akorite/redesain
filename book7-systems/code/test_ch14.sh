#!/bin/bash
# test_ch14.sh -- builds and runs ch14's code and checks the claimed outputs.
cd "$(dirname "$0")" || exit 1
T=$(mktemp -d) || exit 1
trap 'rm -rf "$T"' EXIT
fail() { echo "ch14 FAIL: $1"; exit 1; }

for p in fs_io links direct fsync_sweep; do
  gcc -O2 -w -o "$T/$p" "ch14_$p.c" || fail "compile $p"
done

# names vs inodes
"$T/links" > "$T/links.out" || fail "links run"
i1=$(sed -n 's/^created .*ino=\([0-9]*\) .*/\1/p' "$T/links.out")
i2=$(sed -n 's/^link a->b .*ino=\([0-9]*\) .*/\1/p' "$T/links.out")
[ -n "$i1" ] && [ "$i1" = "$i2" ] || fail "hard link must share the inode"
grep -q "link a->b a .*nlink=2" "$T/links.out" || fail "nlink=2 after link"
grep -q "is-symlink=1 size=1" "$T/links.out" || fail "symlink size"
grep -q "unlinked  a .*(no such name)" "$T/links.out" || fail "unlink a"
grep -q "read via still-open fd: 12 bytes: hello inode" "$T/links.out" || fail "read after unlink"
grep -q "fstat(fd): nlink=0" "$T/links.out" || fail "nlink=0 after unlink"

# journal: plain write corrupts at exactly one crash point, journal at none
python3 ch14_journal_sim.py > "$T/j.out" || fail "journal sim"
grep -q "corrupt states: plain=1, journal=0" "$T/j.out" || fail "journal result"

# max file size and block-map cost
python3 ch14_maxfile.py > "$T/m.out" || fail "maxfile"
grep -q "triple indirect (max)     : 4.0039 TiB" "$T/m.out" || fail "max file size"
grep -q "block-map metadata        : 257 blocks = 1028 KiB" "$T/m.out" || fail "1 GiB block map"

# inode walker on a tree we build: a 1-byte file occupies at least one 512-byte unit
mkdir "$T/tree" && printf x > "$T/tree/one" && printf yy > "$T/tree/two"
python3 ch14_inodes.py "$T/tree" > "$T/w.out" || fail "inode walker"
grep -q "^2 files, 0 KB payload" "$T/w.out" || fail "walker summary"
b=$(sed -n 's/.*blocks= *\([0-9]*\) one$/\1/p' "$T/w.out")
[ -n "$b" ] && [ "$b" -ge 1 ] || fail "walker blocks"

# I/O shapes (hardware dependent: only check orderings that must hold)
"$T/fs_io" > "$T/io.out" || fail "fs_io"
v() { sed -n "s/^$1: \([0-9.]*\) .*/\1/p" "$T/io.out"; }
seq=$(v "sequential read"); w=$(v "write (no fsync)"); wf=$(v "write + fsync per 1MB")
[ -n "$seq" ] && [ -n "$w" ] && [ -n "$wf" ] || fail "fs_io output format"
awk -v a="$w" -v b="$wf" 'BEGIN{exit !(a>b)}' || fail "buffered write should beat fsync-per-1MB ($w vs $wf)"
ms=$(sed -n 's/^fsync per 4KB write: \([0-9.]*\) ms.*/\1/p' "$T/io.out")
awk -v m="$ms" 'BEGIN{exit !(m>0)}' || fail "fsync ms"

if "$T/direct" > "$T/d.out" 2>/dev/null; then
  c=$(sed -n 's/^buffered read, 2nd pass : *\([0-9]*\) MB.*/\1/p' "$T/d.out")
  d=$(sed -n 's/^O_DIRECT read *: *\([0-9]*\) MB.*/\1/p' "$T/d.out")
  [ "$c" -gt "$d" ] || fail "page cache should beat O_DIRECT ($c vs $d)"
else
  echo "ch14 note: O_DIRECT unsupported on /tmp here, check skipped"
fi

"$T/fsync_sweep" > "$T/s.out" || fail "fsync sweep"
[ "$(grep -c ' B ' "$T/s.out")" = 5 ] || fail "sweep rows"
# MB/s must grow with write size (the fixed flush cost is amortised): 4 KB row < 1 MB row
a=$(awk '/^ *4096 B/ {print $NF}' "$T/s.out"); z=$(awk '/^ *1048576 B/ {print $NF}' "$T/s.out")
awk -v a="$a" -v z="$z" 'BEGIN{exit !(z>a)}' || fail "sweep not monotone ($a vs $z)"

echo "ch14 PASS"

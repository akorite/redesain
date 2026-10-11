#!/usr/bin/env python3
# ch14_inodes.py -- inode + size walker over a real directory.
import os, sys
root = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/sys")
n = 0; total = 0
for d, _, files in os.walk(root):
    for fn in files:
        p = os.path.join(d, fn)
        try: st = os.lstat(p)
        except OSError: continue
        n += 1; total += st.st_size
        if n <= 8:
            print(f"ino={st.st_ino:>12} mode={oct(st.st_mode)} blocks={st.st_blocks:>6} {fn}")
print(f"{n} files, {total/1024:.0f} KB payload")

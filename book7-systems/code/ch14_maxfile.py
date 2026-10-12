# ch14_maxfile.py -- how big a file can a classic inode address, and what does
# the block map cost?  4 KB blocks, 4-byte block numbers => 1024 pointers per block.
BLOCK = 4096
PTRS = BLOCK // 4
direct = 12
single, double, triple = PTRS, PTRS**2, PTRS**3
blocks = direct + single + double + triple
print(f"pointers per indirect block : {PTRS}")
print(f"direct only                 : {direct*BLOCK//1024} KiB")
print(f"+ single indirect           : {(direct+single)*BLOCK/2**20:.2f} MiB")
print(f"+ double indirect           : {(direct+single+double)*BLOCK/2**30:.2f} GiB")
print(f"+ triple indirect (max)     : {blocks*BLOCK/2**40:.4f} TiB")
# metadata for one 1 GiB file
f = 2**30
nblk = f // BLOCK
print(f"1 GiB file = {nblk} blocks of 4 KiB")
need_double = nblk - direct - single
l2 = -(-need_double // PTRS)                     # second-level blocks under the double-indirect block
meta = 1 + 1 + l2                                # single-indirect + double-indirect root + its children
print(f"  block-map metadata        : {meta} blocks = {meta*BLOCK/1024:.0f} KiB (+ 12 direct pointers in the inode)")
print(f"  one extent (start,length) : 16 bytes")

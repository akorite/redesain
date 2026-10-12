#!/usr/bin/env python3
"""ch11_sv32_walk.py -- a software model of the RISC-V sv32 page-table walk.

Physical memory is a dict {byte address: 32-bit word}.  A PTE is
    bits 31..10 : PPN (22 bits)      bits 7..0 : D A G U X W R V
A PTE with V=1 and R=W=X=0 points to the next-level table; otherwise it is
a leaf.  Addresses: VA = VPN1(10) | VPN0(10) | offset(12).
"""
import sys

V, R, W, X, U = 1, 2, 4, 8, 16
PAGE = 4096

def pte(ppn, flags):
    return (ppn << 10) | flags

class PageFault(Exception):
    pass

def walk(mem, root_ppn, va, access="r", user=True, trace=None):
    """Return the physical address of VA, or raise PageFault."""
    vpn1, vpn0, off = (va >> 22) & 0x3FF, (va >> 12) & 0x3FF, va & 0xFFF
    table = root_ppn
    for level, idx in ((1, vpn1), (0, vpn0)):
        addr = table * PAGE + idx * 4                  # 4-byte PTEs
        e = mem.get(addr, 0)
        if trace is not None:
            trace.append(f"  level {level}: PTE at 0x{addr:08X} = 0x{e:08X}")
        if not e & V:
            raise PageFault(f"invalid PTE at level {level} (V=0)")
        if e & (R | W | X):                            # leaf
            if level == 1:
                raise PageFault("superpages not modelled")
            need = {"r": R, "w": W, "x": X}[access]
            if not e & need:
                raise PageFault(f"permission: page lacks {access.upper()}")
            if user and not e & U:
                raise PageFault("permission: supervisor-only page")
            return ((e >> 10) << 12) | off
        table = e >> 10                                # pointer to next table
    raise PageFault("no leaf found at level 0")

def demo():
    mem = {}
    # the chapter's worked example: root table at PPN 0x1000
    mem[0x1000 * PAGE + 1 * 4] = pte(0x2000, V)                 # VPN1=1 -> level-0 table
    mem[0x2000 * PAGE + 1 * 4] = pte(0x9ABC, V | R | W | U)     # VPN0=1 -> data page
    mem[0x2000 * PAGE + 2 * 4] = pte(0x9ABD, V | R | U)         # VPN0=2 -> read-only page
    # the exercise: VA 0x00C02ABC, root at PPN 0x4000
    mem[0x4000 * PAGE + 3 * 4] = pte(0x5000, V)
    mem[0x5000 * PAGE + 2 * 4] = pte(0x0777, V | R | W | X | U)
    out = []
    def go(label, root, va, access="r", user=True):
        tr = []
        try:
            pa = walk(mem, root, va, access, user, tr)
            res = f"PA = 0x{pa:08X}"
        except PageFault as e:
            res = f"PAGE FAULT ({e})"
        out.append(f"{label}: VA 0x{va:08X} ({access}) -> {res}")
        out.extend(tr)
    go("walk 1", 0x1000, 0x00401234)
    go("walk 2", 0x1000, 0x00401FFC)
    go("walk 3", 0x1000, 0x00402010, "w")                       # read-only page, store
    go("walk 4", 0x1000, 0x00402010, "r")
    go("walk 5", 0x1000, 0x00801000)                            # VPN1=2: no table
    go("walk 6", 0x4000, 0x00C02ABC)
    return out

if __name__ == "__main__":
    lines = demo()
    print("\n".join(lines))
    # self-check used by test_ch11.sh
    mem = {0x1000 * PAGE + 4: pte(0x2000, V), 0x2000 * PAGE + 4: pte(0x9ABC, V | R | W | U)}
    assert walk(mem, 0x1000, 0x00401234) == 0x09ABC234
    assert walk(mem, 0x1000, 0x00401234) & 0xFFF == 0x234          # offset unchanged
    print("ch11 sv32 model: self-check ok")

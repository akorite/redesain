# ch06_dep_nops.S -- the same chain as ch06_dep.S with just enough nops
# (two between each dependent pair; `or zero,zero,zero` is used as the pad because the ch03 simulator stops at a real nop) for the naive pipeline to be right.
        li   a0, 5
        or   zero, zero, zero   # a pad that is not a nop word
        or   zero, zero, zero   # a pad that is not a nop word
        addi a1, a0, 3
        or   zero, zero, zero   # a pad that is not a nop word
        or   zero, zero, zero   # a pad that is not a nop word
        add  a2, a1, a0
        or   zero, zero, zero   # a pad that is not a nop word
        or   zero, zero, zero   # a pad that is not a nop word
        sw   a2, 0(zero)
        lw   a3, 0(zero)
halt:   j    halt

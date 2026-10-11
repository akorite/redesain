# ch04_inline.S -- same loop, call inlined away.
        li    t6, 0
        li    t5, 100
loop:   addi  t6, t6, 1
        blt   t6, t5, loop
        lui   a7, 0x10000
        li    t2, 66             # 'B'
        sw    t2, 0(a7)
        li    t2, 10
        sw    t2, 0(a7)
done:   nop

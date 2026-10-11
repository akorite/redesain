# ch03_sum_mem.S -- the -O0 habit: i and s live in MEMORY, not registers.
# Same loop as ch03_sum.S but every iteration reloads/restores —
# the dynamic-count difference this chapter measures.
        li    t0, 0x200          # &i
        li    t1, 0x204          # &s
        li    t2, 1
        sw    t2, 0(t0)          # i = 1
        sw    zero, 0(t1)        # s = 0
loop:   lw    t3, 0(t0)          # t3 = i
        lw    t4, 0(t1)          # t4 = s
        add   t4, t4, t3         # s += i
        sw    t4, 0(t1)
        addi  t3, t3, 1
        sw    t3, 0(t0)          # i += 1
        li    t5, 10
        bge   t5, t3, loop
        # result in memory; print hi/lo as before (s = 55)
        lw    t2, 0(t1)
        li    t3, 0
div10:  addi  t2, t2, -10
        addi  t3, t3, 1
        bge   t2, t5, div10
        addi  t4, t2, 0
        lui   a7, 0x10000
        addi  t3, t3, 0x30
        addi  t4, t4, 0x30
        sw    t3, 0(a7)
        sw    t4, 0(a7)
        li    t5, 10
        sw    t5, 0(a7)
done:   nop

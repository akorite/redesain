# ch03_arrsum.S -- sum a 5-element array with lw + pointer bump.
# data: 5 words {1,2,3,4,5} planted at address 0x100 (via .word below
# we hand-write them with sw first — keeps the sim honest).
        li    t0, 0x100          # base = 0x100
        li    t1, 1
        sw    t1, 0(t0)
        li    t1, 2
        sw    t1, 4(t0)
        li    t1, 3
        sw    t1, 8(t0)
        li    t1, 4
        sw    t1, 12(t0)
        li    t1, 5
        sw    t1, 16(t0)
        # now sum them: a0 = base, a1 = n=5, s accumulates in t2
        li    t3, 0              # i = 0
        li    t2, 0              # s = 0
loop:   lw    t4, 0(t0)          # t4 = a[i]
        add   t2, t2, t4         # s += a[i]
        addi  t0, t0, 4          # bump pointer by one word
        addi  t3, t3, 1
        li    t5, 5
        blt   t3, t5, loop       # while i < 5
        # print result (15): hi='1', lo='5'
        li    t3, 0
div10:  addi  t2, t2, -10
        addi  t3, t3, 1
        li    t5, 10
        bge   t2, t5, div10
        addi  t4, t2, 0          # rem
        lui   a7, 0x10000
        addi  t3, t3, 0x30
        addi  t4, t4, 0x30
        sw    t3, 0(a7)
        sw    t4, 0(a7)
        li    t5, 10
        sw    t5, 0(a7)
done:   nop

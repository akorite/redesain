# ch04_callcost.S -- calling overhead, measured on the sim:
# (a) 1000 iterations that CALL an empty function each time
# (b) 1000 iterations with the (empty) body inlined
# The interpreter counts retired instructions; the delta IS the call cost.
        li    t0, 0x300
        li    t1, 0
        sw    zero, 0(t0)        # counter in mem? no — keep registers
        li    t6, 0              # i = 0
        li    t5, 100            # n = 100 calls (keeps the run short)
loop:   call  empty              # the overhead we're timing
        addi  t6, t6, 1
        blt   t6, t5, loop
        # print a marker so we see it ran
        lui   a7, 0x10000
        li    t2, 65             # 'A'
        sw    t2, 0(a7)
        li    t2, 10
        sw    t2, 0(a7)
done:   nop
empty:  ret                      # the called function: one instruction

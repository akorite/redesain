# ch05_sum.S -- sum 1..10 with a bne loop, then a store, a load and a
# load-use pair. Used by ch05 (single-cycle) and ch07 (pipelined, hazards).
        li   t0, 1            # i = 1
        li   t1, 0            # s = 0
        li   t2, 11           # stop when i == 11
loop:   add  t1, t1, t0       # s += i
        addi t0, t0, 1        # i += 1
        bne  t0, t2, loop     # taken 9 times, falls through once
        sw   t1, 0(zero)      # mem[0] = 55
        lw   a0, 0(zero)      # a0 = 55
        addi a1, a0, 1        # load-use: needs a0 right after the lw
        sw   a1, 4(zero)      # mem[1] = 56
halt:   j    halt             # park here

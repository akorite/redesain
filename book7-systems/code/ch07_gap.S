# ch07_gap.S -- one independent instruction between a load and its user.
        li   t0, 41
        sw   t0, 0(zero)
        lw   a0, 0(zero)
        addi a2, zero, 5      # independent filler
        addi a1, a0, 1        # load-use at distance 2: no bubble needed
halt:   j    halt

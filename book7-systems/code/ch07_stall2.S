# ch07_stall2.S -- two load-use pairs: expect exactly two bubbles.
        li   t0, 41
        sw   t0, 0(zero)
        sw   t0, 4(zero)
        lw   a0, 0(zero)
        addi a1, a0, 1        # load-use: bubble 1
        lw   a2, 4(zero)
        addi a3, a2, 1        # load-use: bubble 2
halt:   j    halt

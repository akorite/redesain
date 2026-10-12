# ch05_x0.S -- try to corrupt the constant zero, then use it.
        addi x0, x0, 7        # must be silently dropped
        lui  x0, 0x12345      # so must this one
        addi a0, x0, 1        # a0 = 0 + 1 = 1   (a0 = 8 if x0 were 7)
        add  a1, x0, a0       # a1 = 0 + 1 = 1
        addi a2, zero, 3      # a real write still lands: a2 = 3
halt:   j    halt

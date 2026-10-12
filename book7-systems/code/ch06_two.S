# ch06_two.S -- two independent loads of constants, then a use of both.
        li   a0, 5
        li   a1, 7
        add  a2, a0, a1       # a1 at distance 1, a0 at distance 2
halt:   j    halt

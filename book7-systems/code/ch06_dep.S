# ch06_dep.S -- straight-line code where every instruction needs the
# one just before it. Correct answers: a0=5 a1=8 a2=13 mem[0]=13 a3=13.
        li   a0, 5
        addi a1, a0, 3        # reads a0 one instruction after its writer
        add  a2, a1, a0       # reads a1 (distance 1) and a0 (distance 2)
        sw   a2, 0(zero)      # store data a2 at distance 1
        lw   a3, 0(zero)
halt:   j    halt

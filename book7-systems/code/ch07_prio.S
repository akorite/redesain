# ch07_prio.S -- two back-to-back writers of a0, then a reader.
# When the reader is in EX, EX/MEM holds the newer a0 (2) and MEM/WB the
# older one (1).  Correct: a0=2, a1=2.
        li   a0, 1
        addi a0, a0, 1
        add  a1, a0, zero
halt:   j    halt

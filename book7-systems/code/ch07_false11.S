# ch07_false11.S -- an independent addi right after a load.  Its
# immediate (11) does NOT equal the load's destination register number
# (a0 = x10) and sits in the bit field the hazard unit reads as rs2.
        lw   a0, 0(zero)
        addi a1, zero, 11
halt:   j    halt

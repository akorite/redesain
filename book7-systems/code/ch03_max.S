# ch03_max.S -- max(17, 42) with bge; print "42\n".
        li    a0, 17
        li    a1, 42
        bge   a0, a1, takeA0     # if a0 >= a1 -> max is a0
        addi  a2, a1, 0          # else max = a1
        beq   a2, a2, print
takeA0: addi  a2, a0, 0
print:  li    t3, 0
        li    t5, 10
div10:  addi  a2, a2, -10
        addi  t3, t3, 1
        bge   a2, t5, div10
        addi  t4, a2, 0
        lui   a7, 0x10000
        addi  t3, t3, 0x30
        addi  t4, t4, 0x30
        sw    t3, 0(a7)
        sw    t4, 0(a7)
        li    t5, 10
        sw    t5, 0(a7)
done:   nop

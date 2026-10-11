# ch03_sum.S -- sum 1..10 in RV32I, print "55\n" via MMIO at 0x10000000.
        li    t0, 1              # i = 1
        li    t1, 0              # s = 0
        li    t2, 10             # n = 10
loop:   add   t1, t1, t0         # s += i
        addi  t0, t0, 1          # i += 1
        bge   t2, t0, loop       # while i <= n
        # divide s by 10 with repeated subtraction: t3=quot, t4=rem
        li    t3, 0
div10:  addi  t1, t1, -10
        addi  t3, t3, 1
        bge   t1, t2, div10      # while s >= 10
        addi  t4, t1, 0          # lo digit (s < 10 now)
        lui   a7, 0x10000        # a7 = 0x10000000 (MMIO out)
        addi  t3, t3, 0x30       # '0' + hi
        addi  t4, t4, 0x30       # '0' + lo
        sw    t3, 0(a7)          # print hi
        sw    t4, 0(a7)          # print lo
        li    t5, 10
        sw    t5, 0(a7)          # print '\n'
done:   nop

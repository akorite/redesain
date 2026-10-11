# ch04_fib.S -- recursive fib(7)=13, real stack frames on a real sp.
# MMIO print at 0x10000000 prints result as two ASCII digits.
        li    sp, 0x1000         # sp initialised (Book5's flat RAM grew a stack)
        li    a0, 7
        call  fib                # a0 = fib(7)
        # print a0 as decimal
        li    t3, 0
        li    t5, 10
div10:  addi  a0, a0, -10
        addi  t3, t3, 1
        bge   a0, t5, div10
        addi  t4, a0, 0
        lui   a7, 0x10000
        addi  t3, t3, 0x30
        addi  t4, t4, 0x30
        sw    t3, 0(a7)
        sw    t4, 0(a7)
        li    t5, 10
        sw    t5, 0(a7)
done:   nop

# fib: returns fib(n) in a0; recursive, correct ra discipline
fib:
        addi  sp, sp, -16        # frame: 16 B (keep sp 16-aligned)
        sw    ra, 12(sp)         # save return address  <-- THE discipline
        sw    s0, 8(sp)          # save n
        li    t0, 1
        bge   t0, a0, base       # n <= 1 -> base
        addi  s0, a0, 0          # s0 = n
        addi  a0, a0, -1
        call  fib                # a0 = fib(n-1); ra overwritten inside
        sw    a0, 4(sp)          # park fib(n-1) in frame
        addi  a0, s0, -2
        call  fib                # a0 = fib(n-2)
        lw    t1, 4(sp)
        add   a0, a0, t1         # a0 = fib(n-1)+fib(n-2)
        j     unwind
base:                            # n in {0,1}: a0 already = n
unwind:
        lw    ra, 12(sp)         # restore ra
        lw    s0, 8(sp)          # restore s0
        addi  sp, sp, 16         # pop frame
        ret

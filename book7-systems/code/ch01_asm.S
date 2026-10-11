# ch01_asm.S -- the compile journey's last mile, handwritten:
# an RV32I-style sum in x86-64 assembler (gas syntax), same loop the
# compiler emitted from sum().
    .text
    .globl asum
asum:                       # int asum(int *a, int n)
    xorl  %eax, %eax        # s = 0
    xorl  %ecx, %ecx        # i = 0
.L1:
    cmpl  %esi, %ecx        # i < n ?
    jge   .L2
    addl  (%rdi,%rcx,4), %eax   # s += a[i]
    incl  %ecx
    jmp   .L1
.L2:
    ret

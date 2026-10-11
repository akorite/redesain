# ch01_start.S -- minimal freestanding _start: call sum(), exit via syscall.
    .text
    .globl _start
_start:
    lea   data(%rip), %rdi    # a = &data
    movl  $5, %esi            # n = 5
    call  sum
    movl  %eax, %edi          # exit status = sum = 15
    movl  $60, %eax           # SYS_exit (x86-64)
    syscall
    .data
    .globl data
data:
    .int 1,2,3,4,5

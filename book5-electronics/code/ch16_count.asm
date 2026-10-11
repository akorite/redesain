; ch16_count.asm -- count up forever on OUT (the LED demo).
; r7 = const 1, adds it each lap. Wraps mod 256 naturally.
    LDI A,1
    MOV r7
    LDI A,0
loop:
    ADD r7          ; A = A + 1
    OUT
    JMP loop

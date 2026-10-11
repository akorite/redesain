; ch16_mult.asm -- 7 x 6 by repeated addition, prints 42.
; r1=7 r2=counter r3=const1 r4=result
    LDI A,7
    MOV r1
    LDI A,6
    MOV r2
    LDI A,1
    MOV r3
    LDI A,0
    MOV r4          ; result = 0
loop:
    MOVA r4
    ADD r1          ; result += 7
    MOV r4
    MOVA r2
    SUB r3          ; counter--
    MOV r2
    JZ done
    JMP loop
done:
    MOVA r4
    OUT
    HALT

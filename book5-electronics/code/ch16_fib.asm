; ch16_fib.asm -- Fibonacci mod 256, prints each term on OUT.
; r1=prev r2=cur r3=tmp r4=count r7=const1
    LDI A,0
    MOV r1          ; prev = 0
    LDI A,1
    MOV r2          ; cur = 1
    LDI A,12
    MOV r4          ; count = 12 terms
    LDI A,1
    MOV r7          ; const 1
loop:
    MOVA r2         ; A = cur
    OUT             ; print it
    ADD r1          ; A = cur + prev
    MOV r3          ; tmp = next
    MOVA r2         ; A = cur
    MOV r1          ; prev = cur
    MOVA r3         ; A = next
    MOV r2          ; cur = next
    MOVA r4         ; A = count
    SUB r7          ; count-1 (sets Z at 0)
    MOV r4
    JZ done
    JMP loop
done:
    HALT

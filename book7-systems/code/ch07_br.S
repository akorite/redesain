# ch07_br.S -- a taken branch hops over exactly the two instructions a
# predict-not-taken pipeline has already fetched.  Correct: a2=0, a3=0.
        li   a0, 1
        li   a1, 1
        beq  a0, a1, skip
        li   a2, 99           # wrong-path slot 1 (in ID when beq is in EX)
        li   a3, 99           # wrong-path slot 2 (being fetched)
skip:   li   a5, 7
halt:   j    halt

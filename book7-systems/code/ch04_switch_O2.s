	.attribute	4, 16
	.attribute	5, "rv64i2p1_m2p0_a2p1_c2p0_zmmul1p0_zaamo1p0_zalrsc1p0_zca1p0"
	.file	"ch04_switch.c"
	.text
	.globl	grade                           # -- Begin function grade
	.p2align	1
	.type	grade,@function
grade:                                  # @grade
# %bb.0:
	slli	a1, a0, 1
	slli	a2, a0, 3
	sltiu	a0, a0, 4
	add	a1, a1, a2
	addiw	a1, a1, 60
	neg	a0, a0
	and	a0, a0, a1
	ret
.Lfunc_end0:
	.size	grade, .Lfunc_end0-grade
                                        # -- End function
	.ident	"Homebrew clang version 23.1.3"
	.section	".note.GNU-stack","",@progbits
	.addrsig

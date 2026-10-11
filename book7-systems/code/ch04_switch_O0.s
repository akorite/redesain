	.attribute	4, 16
	.attribute	5, "rv64i2p1_m2p0_a2p1_c2p0_zmmul1p0_zaamo1p0_zalrsc1p0_zca1p0"
	.file	"ch04_switch.c"
	.text
	.globl	grade                           # -- Begin function grade
	.p2align	1
	.type	grade,@function
grade:                                  # @grade
# %bb.0:
	addi	sp, sp, -32
	sd	ra, 24(sp)                      # 8-byte Folded Spill
	sd	s0, 16(sp)                      # 8-byte Folded Spill
	addi	s0, sp, 32
	sw	a0, 8(sp)
	lw	a0, 8(sp)
	sd	a0, 0(sp)                       # 8-byte Folded Spill
	beqz	a0, .LBB0_4
	j	.LBB0_1
.LBB0_1:
	ld	a0, 0(sp)                       # 8-byte Folded Reload
	sext.w	a0, a0
	li	a1, 1
	beq	a0, a1, .LBB0_5
	j	.LBB0_2
.LBB0_2:
	ld	a0, 0(sp)                       # 8-byte Folded Reload
	sext.w	a0, a0
	li	a1, 2
	beq	a0, a1, .LBB0_6
	j	.LBB0_3
.LBB0_3:
	ld	a0, 0(sp)                       # 8-byte Folded Reload
	sext.w	a0, a0
	li	a1, 3
	beq	a0, a1, .LBB0_7
	j	.LBB0_8
.LBB0_4:
	li	a0, 60
	sw	a0, 12(sp)
	j	.LBB0_9
.LBB0_5:
	li	a0, 70
	sw	a0, 12(sp)
	j	.LBB0_9
.LBB0_6:
	li	a0, 80
	sw	a0, 12(sp)
	j	.LBB0_9
.LBB0_7:
	li	a0, 90
	sw	a0, 12(sp)
	j	.LBB0_9
.LBB0_8:
	li	a0, 0
	sw	a0, 12(sp)
	j	.LBB0_9
.LBB0_9:
	lw	a0, 12(sp)
	ld	ra, 24(sp)                      # 8-byte Folded Reload
	ld	s0, 16(sp)                      # 8-byte Folded Reload
	addi	sp, sp, 32
	ret
.Lfunc_end0:
	.size	grade, .Lfunc_end0-grade
                                        # -- End function
	.ident	"Homebrew clang version 23.1.3"
	.section	".note.GNU-stack","",@progbits
	.addrsig

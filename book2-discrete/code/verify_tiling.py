"""verify_tiling.py -- L-tromino tiling of a 2^k x 2^k board minus one cell.

Constructive induction, exactly the proof of the theorem: quarter the board,
drop one L-tromino on the three centre cells away from the hole, and recurse
into each quadrant with its new hole. Prints an ASCII tiling for 8x8.
"""

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"


def tile(board, top, left, size, hr, hc, tid):
    """Tile the size x size block at (top,left) whose hole is (hr,hc)."""
    if size == 2:
        for r in range(top, top + 2):
            for c in range(left, left + 2):
                if (r, c) != (hr, hc):
                    board[r][c] = LETTERS[tid]
        return tid + 1

    h = size // 2
    # quadrant containing the hole: 0=TL, 1=TR, 2=BL, 3=BR
    q = (hr >= top + h) * 2 + (hc >= left + h)
    centers = [(top + h - 1, left + h - 1), (top + h - 1, left + h),
               (top + h, left + h - 1), (top + h, left + h)]
    # centre tromino covers one cell of each quadrant without the real hole
    for i, (r, c) in enumerate(centers):
        if i != q:
            board[r][c] = LETTERS[tid]
    tid += 1
    # recurse: quadrant q keeps the real hole; the others inherit the
    # centre cell just taken, which now plays the role of their hole
    origins = [(top, left), (top, left + h), (top + h, left), (top + h, left + h)]
    for i, (qt, ql) in enumerate(origins):
        nhr, nhc = (hr, hc) if i == q else centers[i]
        tid = tile(board, qt, ql, h, nhr, nhc, tid)
    return tid


def main():
    size, hr, hc = 8, 5, 3   # board and hole (0-indexed)
    board = [["#" if (r, c) == (hr, hc) else "." for c in range(size)]
             for r in range(size)]
    used = tile(board, 0, 0, size, hr, hc, 0)
    print(f"board {size}x{size}, hole at ({hr},{hc})")
    for row in board:
        print(" ".join(row))
    covered = sum(cell != "#" and cell != "." for row in board for cell in row)
    print(f"trominos used: {used}, cells covered: {covered}, "
          f"expected: {(size * size - 1) // 3}")


if __name__ == "__main__":
    main()

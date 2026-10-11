"""diagonal_demo.py -- Cantor diagonalisation on a finite prefix list.

Given a list of decimal strings, print the table with the diagonal marked and
construct a new number differing from every row in its diagonal position.
The mechanism is exactly the proof: flip each diagonal digit.
"""

ROWS = [
    "0.5000000000",
    "0.3333333333",
    "0.1415926535",
    "0.7182818284",
    "0.4142135623",
    "0.6180339887",
    "0.1010010001",
    "0.2500000000",
]


def flip(digit):
    """5->4, everything else ->5. Never produces 9s, so no trailing-9s
    collision can save the list."""
    return "4" if digit == "5" else "5"


def main():
    digits = []
    for i, row in enumerate(ROWS):
        cells = list(row)
        cells[i + 2] = "[" + cells[i + 2] + "]"   # mark position i+2 (after "0.")
        print("".join(cells))
        digits.append(flip(row[i + 2]))
    built = "0." + "".join(digits) + "..."
    print("constructed:", built)
    print("differs from every row at its marked position")


if __name__ == "__main__":
    main()

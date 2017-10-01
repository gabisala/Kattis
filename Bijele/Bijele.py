
# -*- coding: utf-8 -*-

import sys

# Read data
test_input = sys.stdin.readline()
have_pieces = map(int, test_input.split())

correct_pieces = [1, 1, 2, 2, 2, 8]

# Count pieces
chess_pieces = [a - b for a, b in zip(correct_pieces, have_pieces)]

# Output should consist of 66 integers on a single line; the number of pieces of each type Mirko should add or remove.
# If a number is positive, Mirko needs to add that many pieces. If a number is negative, Mirko needs to remove pieces.
for piece in chess_pieces:
    print piece,

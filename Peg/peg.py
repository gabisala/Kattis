
# -*- coding:utf-8 -*-

import sys

# Read data
data = [line.strip() for line in sys.stdin]


# Create bord (7 x 7)
def create_bord(data):
    """
    Create Peg boards

    :param data: raw data
    :return: a list with two board layouts, regular and flip
    """

    # Insert 3 * '-' where the length of row is 3
    fix_board = ['--' + row + '--' if len(row) == 3 else row for row in data]

    # Flip board (left to right)
    flip_board = []

    for x in xrange(7):

        column = []

        for row in fix_board:
            column += row[x]

        flip_board.append(''.join(column))

    return fix_board + flip_board


def find_legal_moves(board):
    """
    Find all legal moves considering board layout

    :param board: board layouts, regular and flip
    :return: number of legal moves
    """

    # Patterns
    space_right = 'oo.'
    space_left = '.oo'

    count_right = sum([row.count(space_right) for row in board])
    count_left = sum([row.count(space_left) for row in board])

    return count_left + count_right

# Output the number of legal moves.
board = create_bord(data)
print find_legal_moves(board)

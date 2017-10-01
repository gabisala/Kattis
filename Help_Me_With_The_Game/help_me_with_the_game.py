
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.extend(line.split())

# Clean data, remove board cells margins
board = []

for i, row in enumerate(data):

    if i % 2 != 0:
        board.append(row.split('|')[1:-1])


def assign_coordinates(chess_piece, column, row):

    """
    Read board layout and return chess piece coordinates
    :param chess_piece: Kings (“K”), Queens (“Q”), Rooks (“R”), Bishops (“B”), Knights (“N”), and Pawns(None) for White
                        Kings (“k”), Queens (“q”), Rooks (“r”), Bishops (“b”), Knights (“n”), and Pawns(None) for Black
    :param column:
    :param row:
    :return: string, the position of the piece in the standard chess notation
    """

    # lower-case letter between “a” and “h” that determines the column (“a” is the leftmost column in the input)
    columns_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    # If the piece is a pawn format coordinates without the name
    if chess_piece == 'P' or chess_piece == 'p':

        # example - coordinate = e7 (column)(raw)
        coordinates = '{}{}'.format(columns_names[column], str(row + 1))

    # Otherwise
    else:
        # example - coordinate = Ke8 (King)(column)(raw)
        coordinates = '{}{}{}'.format(chess_piece.upper(), columns_names[column], str(row + 1))

    return  coordinates


def bord_layout(board):
    """
    Creates a mapping of the pieces(keys) to board positions(values)
    :param board: a list of lists(every row)
    :return: a dictionary
    """

    all_positions = {}

    # For every row of the board(switched)
    for i, row in enumerate(reversed(board)):

        # For every cell in the row
        for j, cell in enumerate(row):

            # Select piece
            piece = cell[1]

            # If not empty cell
            if piece != '.' and piece != ':':

                # Assign position
                position = assign_coordinates(piece, j, i)

                # If piece already in dictionary add only the value
                if all_positions.has_key(piece):
                     all_positions[piece].append(position)

                # Add piece as key and position as value
                else:
                    all_positions[piece] = [position]

    # Return dictionary
    return all_positions


positions = bord_layout(board)

def white_black(positions):
    """
    Creates two dictionary's, from the positions dictionary
    :param positions: a dictionary
    :return: tuple, has two dictionary's
    """

    # White and black piece/position mappings
    white_positions = {'K':[], 'Q':[], 'R':[], 'B':[], 'N':[], 'P':[]}
    black_positions = {'K':[], 'Q':[], 'R':[], 'B':[], 'N':[], 'P':[]}

    # Foe every piece on the board
    for key, value in positions.iteritems():

        # If key it's uppercase add position to white
        if key.isupper():
            white_positions[key].extend(value)

        # Else add to black
        else:
            black_positions[key.upper()].extend(value)

    # Return the two dictionary's in a tuple
    return white_positions, black_positions


white_positions, black_positions = white_black(positions)

def sort_for_output(white_positions, black_positions):
    """
    Sorts the pieces for output in correct order
    In case two pieces of the same type appear in the input, the piece with the smaller row number must be described
    before the other one if the pieces are white, and the one with the larger row number must be described first
    if the pieces are black. If two pieces of the same type appear in the same row, t
    he one with the smaller column letter must appear first.
    :param white_positions: a dictionary
    :param black_positions: a dictionary
    :return: a tuple with two lists(white and black)
    """

    # Correct output order (Kings (“K”), Queens (“Q”), Rooks (“R”), Bishops (“B”), Knights (“N”), and Pawns('P').)
    pieces_output_order = 'KQRBNP'

    # Store pieces in order
    white = []
    black = []

    # Search for every piece in their color dictionary and after sorting add them to their color list
    for piece in pieces_output_order:

        # If pawn
        if piece == 'P':

            white_piece = sorted(white_positions[piece], key=lambda v: v[1])
            black_piece = sorted(black_positions[piece], key=lambda v: v[1], reverse=True)

            white.extend(white_piece)
            black.extend(black_piece)

        # Otherwise
        else:
            white_piece = sorted(white_positions[piece], key=lambda v: v[2])
            black_piece = sorted(black_positions[piece], key=lambda v: v[2], reverse=True)

            white.extend(white_piece)
            black.extend(black_piece)

    return white, black


white, black = sort_for_output(white_positions, black_positions)

# Output
print '{} {}'.format('White:', ','.join(white))
print '{} {}'.format('Black:', ','.join(black))

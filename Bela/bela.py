
# *-* coding:utf-8 -*-

import sys

# Read data
game = []
for line in sys.stdin:
    game.append(line.split())

# Game suit and hands
domin_suit = game[0][1]
hands = game[1:]

# suit value
suit_val = {'A': [11], 'K': [4], 'Q': [3], 'J': [2, 20], 'T': [10], '9': [0, 14], '8': [0], '7': [0]}

# number of points in the game
points = 0

# determine the total number of points in a game
for hand in hands:

    # Play hand
    cards = list(hand[0])
    number = cards[0]
    suit = cards[1]

    if (number == 'J' or number == '9') and suit == domin_suit:
        points += suit_val[number][1]

    else:
        points += suit_val[number][0]

print points

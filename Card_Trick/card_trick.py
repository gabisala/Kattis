
# -*- coding:utf-8 -*-

import sys
from collections import deque

# Read data
data = []

for line in sys.stdin:
    data += map(int, line.split())


# Shuffle cards
def shuffle(deck_size):
    """
    Determine the initial order of the cards for a given number of cards
    :param deck_size: int, number of cards in the deck
    :return: deque, cards in correct order
    """

    # Cards in order
    deck = range(1, deck_size + 1)

    # Empty shuffle deck
    shuffle_deck = deque()

    # For every card in deck, from big to small
    for c in deck[::-1]:
        # Add card
        shuffle_deck.appendleft(c)

        # Shuffle cards
        shuffle_deck.rotate(c)

    # Correct cards order
    return shuffle_deck


# For each test case, output a line with the correct permutation of the values 1 to n, space separated.
for size in data[1:]:

    # Foe each card in deque
    for card in shuffle(size):
        print card,

    print ''

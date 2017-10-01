
# -*- coding:utf-8 -*-

import sys

# Read data
data = sys.stdin.readline()

# The suits of card deck
deck = {'P': 13, 'K': 13, 'H': 13, 'T': 13}

# Cut card from data
card_labels = []

while data is not '':
    card = data[0:3]
    card_labels.append(card)
    data = data[3:]
    card = ''

# Check if duplicates
card_labels_set = set(card_labels)

# How many cards of the suit P, K, H, T are missing.
# If there are two exact same cards in the deck, output “GRESKA”
if len(card_labels_set) < len(card_labels):
    print 'GRESKA'

else:
    # Compute missing cards
    for card in card_labels:
        if card[0] == 'P':
            deck['P'] -= 1
        elif card[0] == 'K':
            deck['K'] -= 1
        elif card[0] == 'H':
            deck['H'] -= 1
        elif card[0] == 'T':
            deck['T'] -= 1

    print '{} {} {} {}'.format(deck['P'], deck['K'], deck['H'], deck['T'])

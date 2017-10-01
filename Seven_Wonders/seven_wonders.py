
# -*- coding:utf-8 -*-

# Read scientific cards a player has played
import sys

played_cards = []

for line in sys.stdin.readline():
    played_cards += line.split()


# Calculate played cards points
def card_point(played_cards):
    t_cards, c_cards, g_cards = 0, 0, 0

    for card in played_cards:
        if card == 'T':
            t_cards += 1
        elif card == 'C':
            c_cards += 1
        elif card == 'G':
            g_cards += 1

    return t_cards, c_cards, g_cards


# Calculate the bonus
def calculate_bonus():
    cards_points = card_point(played_cards)

    if cards_points[0] == cards_points[1] == cards_points[2]:
        return cards_points[0]
    else:
        return min(cards_points[0], cards_points[1], cards_points[2])


# Output the number of scientific points the player earns
def calculate_score():
    bonus_multiplier = calculate_bonus()
    points = card_point(played_cards)
    t, c, g = points

    return t ** 2 + c ** 2 + g ** 2 + 7 * bonus_multiplier


# Submit
score = calculate_score()
print score

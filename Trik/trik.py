
# -*- coding:utf-8 -*-

import sys

# Read data
my_input = sys.stdin.readline()

moves = list(my_input)

# Cups
left_cup = True
middle_cup = False
right_cup = False


# Swaps cups
for move in moves:

    if move == 'A':
        left_cup, middle_cup = middle_cup, left_cup

    elif move == 'B':
        middle_cup, right_cup = right_cup, middle_cup

    elif move == 'C':
        right_cup, left_cup = left_cup, right_cup


# Output the index of the cup under which the ball is: 1 if it is under the left cup, 2 if it is under
# the middle cup or 3 if it is under the right cup.
if left_cup is True:
    print 1
elif middle_cup is True:
    print 2
elif right_cup is True:
    print 3

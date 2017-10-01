# -*- coding: utf-8 -*-

import sys

# Read data
dice_input = sys.stdin.readline()
dice_faces = dice_input.split(' ')

# N,M, specifying the number of faces of the two dice.
dice_N = int(dice_faces[0])
dice_M = int(dice_faces[1])

# Compute sum of the two dices
dice_sum = [i + j for i in range(1, dice_N + 1) for j in range(1, dice_M + 1)]

# Sore outcome
counter_map = {}

for num in dice_sum:
    if num not in counter_map.keys():
        counter_map[num] = 1
    else:
        counter_map[num] += 1

# A line with the most likely outcome for the sum; in case of several outcomes with the same probability,
# they must be listed from lowest to highest value in separate lines.
max_count = max(counter_map.values())

for key, val in counter_map.items():
    if val == max_count:
        print key

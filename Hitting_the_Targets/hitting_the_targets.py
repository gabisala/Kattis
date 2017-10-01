
# -*- coding:utf-8 -*-

import sys
from math import sqrt

# Read data
data = []

for line in sys.stdin:
    data.append(line.strip().split())

# Assign variables
num_targets = int(data[0][0])
targets = data[1: num_targets + 1]
shots = data[num_targets + 2:]


# For each shot
for shot in shots:

    # THe number of targets the shot hits
    count_hits = 0

    # Assign x, y coordinates for the shot
    shot_x, shot_y = int(shot[0]), int(shot[1])

    # For each target
    for target in targets:

        if target[0] == 'rectangle':

            # Assign rectangle edges
            left, bottom, right, top = [int(i) for i in target[1:]]

            # If the shot hits the target
            if left <= shot_x <= right and bottom <= shot_y <= top:

                count_hits += 1

        elif target[0] == 'circle':

            # Assign circle position and radius
            center_x, center_y = [int(i) for i in target[1: 3]]
            radius = int(target[3])

            # Compute the shot distance from the center of the circle
            distance = sqrt((shot_x - center_x) ** 2 + (shot_y - center_y) ** 2)

            if distance <= radius:

                count_hits += 1

    # For each of the n shots, print the total number of targets the shot hits
    print count_hits

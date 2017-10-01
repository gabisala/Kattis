
# -*- coding:utf-8 -*-

import sys
import itertools

# Read data
data = map(int, sys.stdin.readline().split())

# Variables
boxes = data[:6]
first_tower = data[6]

# Combine all boxes and find the first tower by height
figure_out = itertools.combinations(boxes, 3)

height = 0
arrange_boxes = []
while height != first_tower:
    arrange_boxes = next(figure_out)
    height = sum(arrange_boxes)

# First tower
towers = sorted(list(arrange_boxes), reverse=True)

# If boxes are not in the first tower add them to the list (big to small)
for b in sorted(boxes, reverse=True):
    if b not in towers:
        towers.append(b)

# Output the heights of the three boxes in the first tower (i.e., the tower specified by the first tower height
# in the input), then the heights of the three boxes in the second tower. Each set of boxes should be output
# in order of decreasing height. Each test case will have a unique answer.
for b in towers:
    print b,

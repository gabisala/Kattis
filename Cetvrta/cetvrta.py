
# -*- coding:utf-8 -*-

import sys

# Read data
coordinates = []

for line in sys.stdin:
    coordinates.append(map(int, line.split()))

# Assign three points
p1, p2, p3 = coordinates

# x, y coordinates for the points
x_coordinates = [p1[0], p2[0], p3[0]]
y_coordinates = [p1[1], p2[1], p3[1]]

# Find non duplicate element in x, y lists
x = [x for x in x_coordinates if x_coordinates.count(x) == 1]
y = [y for y in y_coordinates if y_coordinates.count(y) == 1]

# Output x, y coordinate for the 4-th point
print x[0], y[0]


# -*- coding:utf-8 -*-

import sys

# Read data
data = sys.stdin.readline().split()
quadkey = data[0]


def quadkey_to_coordinates(quadkey):

    # Calculate zoom
    zoom = len(quadkey)

    # Assign x, y for zoom 1
    x_y = [[0, 0], [1, 0], [0, 1], [1, 1]]

    # Compute x, y coordinates at every zoom level
    coordinates = [0, 0]
    for c in quadkey:
        coordinates[0] *= 2
        coordinates[1] *= 2
        coordinates[0] += x_y[int(c)][0]
        coordinates[1] += x_y[int(c)][1]

    return zoom, coordinates[0], coordinates[1]

# Output three integers, the zoom level and the x and y coordinates of the tile.
zoom, x, y = quadkey_to_coordinates(quadkey)
print zoom, x, y

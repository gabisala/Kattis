
# -*- coding:utf-8 -*-

import sys

# Read data
vertices = int(sys.stdin.readline().strip())

# Compute and output the number of intersections on a single line.
intersections = vertices * (vertices - 1) * (vertices - 2) * (vertices - 3) / 24
print intersections

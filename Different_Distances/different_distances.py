
# -*- coding:utf-8 -*-

import sys

# Read data
data = [map(float, line.split()) for line in sys.stdin]

# For each test case output the p-norm distance between the two points (x1,y1)) and (x2,y2). The answer
# should be accurate within 0.0001 error.
for points in data[:-1]:
    x1, y1, x2, y2, p = points
    p_norm = ((x1 - x2) ** p + (y1 - y2) ** p) ** (1/p)
    print(abs(p_norm))

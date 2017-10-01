
# -*- coding:utf-8 -*-

import sys
import math

# Read data
data = [map(float, line.split()) for line in sys.stdin]

# For each test case, print a line containing two numbers: the true area of the circle and the estimate according to
# the experiment. Both numbers may have a relative error of at most 10 ** −5.
for l in data[:-1]:

    # true radius of the circle, total number of marked points, number of marked points that fall in the circle
    r, m, c = l

    # true area, experiment area
    print '{} {}'.format(math.pi * r ** 2, ((2 * r) ** 2) * c / m)

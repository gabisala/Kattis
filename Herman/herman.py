
# -*- coding:utf-8 -*-

import math
import sys

# Read data
data = sys.stdin.readline().split()
r = float(data[0])

# Euclidian formula for the circle area
circle_area_euclid = math.pi * (r ** 2.0)
print "%.6f" % circle_area_euclid


# Taxicab geometry formula for the circle area
# π_taxi = ( Circumference / Diameter ) or 4
circle_area_taxi = 4.0 * (r ** 2.0) / 2.0
print "%.6f" % circle_area_taxi

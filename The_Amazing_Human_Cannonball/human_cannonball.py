
# -*- coding:utf-8 -*-

import sys
import math

# Read data
test_cases = []

for line in sys.stdin:
    test_cases.append(map(float, line.split()))

test_cases = test_cases[1:]

# Compute trajectory for each test
for test in test_cases:

    # declare parameters
    v0, angle, x1, h1, h2 = test

    # calculate t1 (x(t)= v0 * t * cosθ)
    t1 = x1 / (v0 * math.cos(math.radians(angle)))

    # gravity acceleration
    g = 9.81

    # calculate cannon ball trajectory on y-axis (y(t)= v0 * t * sin⁡θ − 1/2 * gt**2)
    y_t1 = (v0 * t1 * math.sin(math.radians(angle)) - (g * (t1 ** 2)) / 2.0)

    # if the cannon ball can safely make it through the wall, output “Safe”. Otherwise, output “Not Safe”
    if h1 + 1 < y_t1 < h2 - 1:
        print 'Safe'
    else:
        print 'Not Safe'


# -*- coding:utf-8 -*-

import sys
import math

# Read data
data = []

for line in sys.stdin:
    data.append(map(float, line.split()))

data = data[:-1]

# For each case, one line of output should be produced containing a floating point number giving the value of d
# measured in linear units. Your output will be considered correct if it is within relative or absolute error 10**−6.
for case in data:
    D, V = case
    d = (D ** 3.0 - 6.0 * V / math.pi) ** (1.0 / 3.0)
    print d

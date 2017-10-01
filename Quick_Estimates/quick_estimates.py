
# -*- coding:utf-8 -*-

import sys

# Read data
estimated_costs = []

# For each estimated cost, output the number of digits required to represent it
for line in sys.stdin:
    estimated_costs += line.split()
    if len(estimated_costs) > 1:
        print len(estimated_costs[-1])


# -*- coding:utf-8 -*-

import sys

# Read data

input_data = sys.stdin.readline()
# Sort list of ints
walk = sorted(map(int, input_data.split()))

# Compute area
print '{}'.format(walk[0] * walk[2])

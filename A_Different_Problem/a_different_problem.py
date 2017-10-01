
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(map(int, line.split()))

# For each pair of integers in the input, output one line, containing the absolute value of their difference.
for nums in data:
    print abs(max(nums) - min(nums))

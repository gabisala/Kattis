
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(line.split('\n'))

# All lines length
length_lines = [len(l[0]) for l in data]

# Compute longest line
n = max(length_lines)

# Print out a single integer, the raggedness score for paragraph.
print sum([(n-m) ** 2 for m in length_lines[:-1]])

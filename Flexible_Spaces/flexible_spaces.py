
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.extend(map(int, line.split()))

# Delete number of partitions
del data[1]

# Store initial partitions
partitions = sorted(data)[::-1]

# Determine all feasible widths for a meeting by subtracting all partitions combinations
initial_widths = partitions[:]
new_widths = []

while initial_widths:

    for w in initial_widths[1:]:
        new_widths.append(initial_widths[0] - w)

    del initial_widths[0]


# Merge and sort all possible widths
widths = sorted(set(new_widths + partitions))

# From smallest to largest, of each distinct width that can be achieved for a meeting space.
for w in widths:
    print w,


# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(map(int, line.split()))

# Check when trucks are parked
parked_intervals = []
for truck in data[1:]:
    parked_intervals.extend(range(truck[0], truck[1]))

# Count how many trucks are parked each minute
count = {minute: parked_intervals.count(minute) for minute in parked_intervals}

# Parking fees
a, b, c = data[0]

# Output the overall cost of Luka’s parking his three trucks
cost = 0

for val in count.values():
    if val == 1:
        cost += a
    elif val == 2:
        cost += b * 2
    else:
        cost += c * 3

print cost

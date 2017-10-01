
# -*- coding:utf-8 -*-

import sys

# Read data
sensor_data = []

for line in sys.stdin:
    sensor_data += line.split()

sensor_data = sensor_data[1:]

# Create cups
i = 0
cups = []
while i < len(sensor_data):
    slice_data = sensor_data[i:i+2]
    cups.append(slice_data)
    i += 2

# Put the cups in order of the smallest to the largest
for elem in cups:
    try:
        elem[1] = int(elem[1])
    except ValueError:
        elem[0] = int(elem[0]) / 2
        elem[0], elem[1] = elem[1], elem[0]

# Output colors of cups, one color per line, in order of increasing radius.
for elem in sorted(cups, key=lambda elem: elem[1]):
    print elem[0]
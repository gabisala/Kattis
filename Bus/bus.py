
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data += map(int, line.split())


def count_passengers(bus_stops):
    """
    Find the initial number of bus passengers
    :param bus_stops: number of bus stops
    :return: number of bus passengers
    """

    passengers = 0

    for stop in xrange(bus_stops):
        passengers += 0.5
        passengers *= 2

    return int(passengers)

# For each test case, output a single line containing a single integer—the initial number of bus passengers.
for case in data[1:]:
    print count_passengers(case)

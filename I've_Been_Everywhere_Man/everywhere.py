
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data += line.split()

# Create test cases
test_cases = []

i = 1
while i < len(data):
    cut = data[i + 1: i + int(data[i]) + 1]
    test_cases.append(cut)
    i += int(data[i]) + 1

# For each test case, output a single line containing a single integer that is the number of distinct cities
# that Alice has visited on her work trips
travel_log = {}

for test in test_cases:
    for city in test:

        if city not in travel_log.keys():
            travel_log[city] = 1
        else:
            pass

    print len(travel_log.keys())

    # Reset travel log after test case prints output
    travel_log = {}

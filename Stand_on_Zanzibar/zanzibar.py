
# -*- coding:utf-8 -*-

import sys

# Read data
test_cases = []

for line in sys.stdin:
    test_cases.append(map(int, line.split()))

# Compute lower bound for the number of turtles not born on Zanzibar for each taste case
emigrants = 0

for case in test_cases[1:]:

    for i, turtles in enumerate(case[:-1]):

        # Flag population population growth
        flag = case[i+1] > case[i] * 2

        # Till 0 witch signals the end of the sequence
        if (i < len(case) - 2) and flag is True:
            natives = case[i] * 2
            emigrants += (case[i+1] - natives)

    print emigrants

    # Reset number of emigrantes after each test case
    emigrants = 0

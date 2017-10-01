
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(map(int, line.split()))

cases = data[1:]


# Output for each test case a line with the minimal distance Michael must walk given optimal parking.
for case in cases[1::2]:
    # Sort from big to small
    case = sorted(case)[::-1]

    # Create a list witch holds numbers from sorted case except the biggest one and
    # add 0 at the end so that len(case) = len(case_swap)
    case_swap = case[1:] + [0]

    # Compute the differences between lists and subtract the last element of case list
    # than multiply by 2 (return from the last store to the car)
    print (sum([a - b for a, b in zip(case, case_swap)]) - case[-1]) * 2

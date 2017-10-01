
# -*- coding:utf-8 -*-

import sys

# Read data
data = [map(int, line.split()) for line in sys.stdin]

# For each test case, print the member of the list that is the sum of all the other integers in the list.
# Every test case will contain such a value.
for case in data:
    for number in case:
        if number == sum(case) - number:
            print number
            break

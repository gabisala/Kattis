
# -*- coding:utf-8 -*-

import sys

# Read data
my_input = ''
for line in sys.stdin:
    my_input += line

# Convert to integers
nums = map(int, my_input.split())
nums = nums[1:]

# For each x, print either ‘x is odd’ or ‘x is even’ depending on whether x is odd or even.
for element in nums:
    if element % 2 == 0:
        print '{0} is even'.format(element)
    else:
        print '{0} is odd'.format(element)

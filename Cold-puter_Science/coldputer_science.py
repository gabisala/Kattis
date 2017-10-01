# -*- coding: utf-8 -*-

import sys

# Read data
my_input = ''
for line in sys.stdin:
    my_input += line

# Convert to integers
temp_list = map(int, my_input.split())
temperatures = temp_list[1:]

count_less_than_zero = 0

# Count negative temperatures
for temp in temperatures:
    if temp < 0:
        count_less_than_zero += 1

# Output the number of temperatures strictly less than zero
print count_less_than_zero


# -*- coding:utf-8 -*-

import sys

# Read data
input_numbers = []
for line in sys.stdin:
    input_numbers += map(int, line.split())


# Calculate num % 42 reminder
def modulo_42(input_numbers):

    modulo_list = []

    for num in input_numbers:
        modulo = num % 42
        modulo_list.append(modulo)

    return modulo_list

distinct_values = modulo_42(input_numbers)


# Output the number of distinct values when considered modulo 42
def unique_values():
    return len(set(distinct_values))

solution = unique_values()
print solution

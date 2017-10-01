
# -*- coding:utf-8 -*-

import sys

# Read data
numbers = []

for line in sys.stdin:
    numbers.extend(map(int, line.split()))

# After any two pieces are swapped, output the ordering of the pieces, on a single line separated by spaces.
# Implement bubble sort algorithm
for i in xrange(0, len(numbers) - 1):

    for j in xrange(0, len(numbers) - 1 - i):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

            for num in numbers:
                print num,

            print ''

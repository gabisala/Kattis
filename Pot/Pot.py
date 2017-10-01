# -*- coding: utf-8 -*-

import sys

nums_raw = []

for line in sys.stdin:
    nums_raw += line.split()

nums_raw = nums_raw[1:]

numbers = []
powers = []

for num in nums_raw:
    numbers.append(int(num[:-1]))
    powers.append(int(num[-1]))

numbers_sum = sum([number ** power for number, power in zip(numbers, powers)])

print numbers_sum

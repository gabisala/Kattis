
# -*- coding:utf-8 -*-

import sys

# Read data
data = []
for line in sys.stdin:
    data += line.split()

contract = [float(dimension) for dimension in data]


# Compute the cost to sow all of the lawns
def contract_cost(contract):
    price = contract[0]
    width_and_length = contract[2:]
    i = 0
    area = 0

    while i < len(width_and_length):
        area += width_and_length[i] * width_and_length[i + 1]
        i += 2

    return price * area


print contract_cost(contract)

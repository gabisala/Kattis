
# -*- coding:utf-8 -*-

import sys

# Read data
data = map(int, sys.stdin.readline().split())

# Calculate Bob savings
bob_savings = (data[1] - data[0]) * data[2]

# Assign variables
alice_years = data[3]
alice_saving_rate = data[4]
alice_saving = 0

# Output the age at which Alice can retire so that she has more money than Bob will have at age Br
while bob_savings >= alice_saving:
    alice_saving += alice_saving_rate
    alice_years += 1

print alice_years

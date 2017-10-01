
# -*- coding:utf-8 -*-

import sys
import math

# Read data
data = sys.stdin.readline()
data = data.split()

# Pizza and crust radius
r = float(data[0])
c = float(data[1])

# Calculate areas for pizza and cheese
pizza = math.pi * r ** 2
cheese = math.pi * (r-c) ** 2
# print pizza, cheese

# Calculate the percentage of the pizza that has cheese
cheese_percent = (cheese * 100) / pizza

# Output percentage
print cheese_percent

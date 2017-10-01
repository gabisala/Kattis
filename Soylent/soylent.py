
# -*- coding:utf-8 -*-

import sys
import math

# Read data
data = []

for line in sys.stdin:
    data += map(float, line.split())

bottle_calories = 400

# output a single line containing the number of bottles Yraglac needs to consume for the day
for calories in data[1:]:
    print int(math.ceil(calories / bottle_calories))

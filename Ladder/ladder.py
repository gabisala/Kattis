
# -*- coding:utf-8 -*-

import sys
import math

# Read data
data = sys.stdin.readline()
wall_and_angle = map(int, data.split())


# Calculate the minimum possible length of the ladder
print int(math.ceil(wall_and_angle[0] / (math.sin(math.radians(wall_and_angle[1])))))

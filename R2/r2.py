
# -*- coding:utf-8 -*-

import sys

# Read data
data = map(int, sys.stdin.readline().split())

# Assign r1, s
r1, s = data

# Output r2 on a single line
print (2 * s) - r1

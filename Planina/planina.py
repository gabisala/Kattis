
# -*- coding:utf-8 -*-

import sys

# Read data
n = int(sys.stdin.readline())

# Number of points stored after N iterations
print (2 * (2 ** (n - 1)) + 1) ** 2

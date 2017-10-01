
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data += map(int, line.split())


# One line containing the sum of the two integers.
print(sum(data))

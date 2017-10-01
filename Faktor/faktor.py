
# -*- coding:utf-8 -*-

import sys

# Read data
data = map(int, sys.stdin.readline().split())

# The first and only line of output should contain one integer, the minimal number of scientists you need to bribe
print (data[0] * (data[1] - 1)) + 1

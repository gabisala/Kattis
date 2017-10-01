
# -*- coding:utf-8 -*-

import sys

# Read data
data = sys.stdin.readline().split()

# The first and only line of output should contain the larger of the numbers in the input, compared as described in
# the task. The number should be written reversed, to display to Filip how he should read it
if int(data[0][::-1]) > int(data[1][::-1]):
    print data[0][::-1]
else:
    print data[1][::-1]

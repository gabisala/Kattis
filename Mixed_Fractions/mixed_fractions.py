
# -*- coding:utf-8 -*-

import sys

# Read data
data = []
for line in sys.stdin:
    data.append(map(int, line.split()))

data = data[:-1]

# For each test case, display the resulting mixed fraction as a whole number followed by a proper fraction,
# using whitespace to separate the output tokens.
for pair in data:
    if pair[0] < pair[1]:
        print '0 {} / {}'.format(pair[0], pair[1])
    else:
        print '{} {} / {}'.format(pair[0] / pair[1], pair[0] % pair[1], pair[1])

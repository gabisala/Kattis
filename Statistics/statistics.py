
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(map(int, line.split()[1:]))

# For each case, display Case X:, where X is the case number, followed by the min, max, and range of the sample
# (in that order). Follow the format of the sample output.
for i, l in enumerate(data):
    print 'Case {}: {} {} {}'. format(i + 1, min(l), max(l), max(l) - min(l))


# -*- coding:utf-8 -*-

import sys

# Read data
data = [line.strip('\n') for line in sys.stdin]

# For each test case, repeat the command if the first two words were “simon says”. Do not repeat the
# initial “simon says”. Otherwise output a blank line.
for s in data[1:]:
    if s[0:10] == 'simon says':
        print s[11:]
    else:
        print ''


# -*- coding:utf-8 -*-

import sys
import itertools

# Read data
data = sys.stdin.readline().strip()

# Assign integer x and list his digits
x = int(data)
digits = list(data)

# Arrange digits and append to list only the numbers bigger than x! keep the minimum witch is bigger than x
find_bigger = [int(''.join(n)) for n in itertools.permutations(digits) if int(''.join(n)) > x]

# If no such number print 0
if find_bigger:
    print min(find_bigger)
else:
    print 0

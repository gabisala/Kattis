
# -*- coding:utf-8 -*-

import sys
from collections import Counter

# Read data
data = sys.stdin.readline().strip()

# Count letters in the string
letters_count = Counter(data)

# Compute number of odd number of letters
odd = 0
for v in letters_count.values():
    if v % 2 != 0:
        odd += 1

# Output should consist of a single integer on a single line, the minimum number of characters that have to be removed
# from the string to make it a Peragram.
if odd > 0:
    print odd - 1
else:
    print 0

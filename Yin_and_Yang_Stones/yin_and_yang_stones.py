
# -*- coding:utf-8 -*-

import sys

# Read data
stones = sys.stdin.readline().strip()

# Output 1 if it is possible for Ming to balance the stones with his rules. Otherwise, output 0
count = [stones.count('B'), stones.count('W')]

if count[0] == count[1]:
    print 1
else:
    print 0


# -*- coding:utf-8 -*-

import sys

# Read data
data = map(int, sys.stdin.readline().split())

# Output should consists of a single word on a single line. If it is Paul’s turn to serve the ball, your program should
# output paul. Otherwise, your program should output opponent.
if ((data[1] + data[2]) / data[0]) % 2 == 0:
    print 'paul'
else:
    print 'opponent'

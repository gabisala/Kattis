
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data += map(int, line.split())

# Assign variables
rooms = set(xrange(1, data[0] + 1))
booked = set(data[2:])
available = rooms - booked

# If there are available rooms, output the room number of any such room. Otherwise, output “too late”.
if len(available) is 0:
    print('too late')
else:
    print(available.pop())

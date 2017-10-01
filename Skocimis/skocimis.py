
# -*- coding:utf-8 -*-

import sys

# Read data
positions = map(int, sys.stdin.readline().split())

# Count jumps posible from left to right(smallest to biggest position)
def count_jumps(position):
    # initial positions
    a, b, c = position
    count = 0

    while True:
        if b + 1 < c:
            a = b
            b += 1
            count += 1
        else:
            return count

jumps = count_jumps(positions)


# Count jumps posible from right to left(biggest to smallest position)
def count_jumps_reversed(position):
    # initial positions
    a, b, c = position
    count = 0

    while True:
        if b - 1 > a:
            c = b
            b -= 1
            count += 1
        else:
            return count


jumps_reversed = count_jumps_reversed(positions)
print max(jumps, jumps_reversed)

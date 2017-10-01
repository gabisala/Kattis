
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data += map(int, line.split())


def distance(current_direction, correct_direction):
    """
    Finds the two distances from the current needle direction to the correct direction

    :param current_direction: the current direction of the needle
    :param correct_direction: the correct direction of the needle
    :return: two integers, clockwise and counter_clockwise distances
    """

    if n1 > n2:
        clockwise = (360 - n1) + n2
        counter_clockwise = (360 - clockwise) * -1
    elif n2 > n1:
        clockwise = (n2 - n1)
        counter_clockwise = (360 - clockwise) * -1
    else:
        clockwise = 0
        counter_clockwise = 0

    return clockwise, counter_clockwise


# n1 - the current direction of the needle
# n2 - the correct direction of the needle
n1 = data[0]
n2 = data[1]


def needle_spin(spins):
    """
    Output the change in direction that would make the needle spin the shortest distance from n1 to n2

    :param spins: two integers, clockwise and counter_clockwise distances
    :return: shortest path
    """

    clockwise, counter_clockwise = spins

    # shortest distance
    sd = min(clockwise, abs(counter_clockwise))

    if sd == clockwise:
        return clockwise
    else:
        return counter_clockwise


# Compute distances
distances = distance(n1, n2)

# Output the change in direction that would make the needle spin the shortest distance from n1 to n2. A positive
# change indicates spinning the needle clockwise, and a negative change indicates spinning the needle counter-clockwise.
# If the two input numbers are diametrically opposed, the needle should travel clockwise.
print needle_spin(distances)


# -*- coding:utf-8 -*-

import sys

# Read data
data = [map(int, line.split()) for line in sys.stdin]


def party_day(data):
    """
    Find out when is the earliest day when the party can take place. Jon can choose the order of planting the
    trees as he likes, so he wants to plant the trees in such a way that the party will be as soon as possible.
    :param data: list with two lists, input data
    :return: int, the earliest day when the party can be organized
    """

    # Crop seeds list from data and rearrange from big to small
    seeds = sorted(data[1])[::-1]

    days_to_grow = []

    # For every seed compute the day it reach maturity by adding day of seeding to the days it has to grow
    for i, s in enumerate(seeds):

        planted_in_day = i + 1
        days = s
        cycle = planted_in_day + days

        days_to_grow.append(cycle)

    # The earliest day when the party can be organized is the maximum grow cycle plus one day
    party = max(days_to_grow) + 1

    return party

# Output exactly one line containing one integer, denoting the earliest day when the party can be organized.
# The days are numbered 1,2,3,… beginning from the current moment.
print party_day(data)

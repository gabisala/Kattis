
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(map(int, line.split()))

# For each case, output one of the following results on its own line (without quotes).
l = 'Left beehind.'
u = 'Undecided.'
c = 'To the convention'
n = 'Never speak again.'

decisions = []

for case in data[:-1]:
    # 13 jars
    if sum(case) == 13:
        decisions.append(n)

    # more jars of sweet honey than sour
    elif case[0] > case[1]:
        decisions.append(c)

    # more jars of sour honey than sweet
    elif case[0] < case[1]:
        decisions.append(l)

    # same number of sweet and sour jars
    else:
        decisions.append(u)

    print decisions[-1]


# -*- coding:utf-8 -*-

import sys

# Read data
input_data = []
for line in sys.stdin:
    input_data.append(map(int, line.split()))

# Cut data sets
data_sets = input_data[1:]


# Compute s1, s2, s3
def sum_num_and_odd_and_even(n):

    # S1 = The sum of the first N positive integers.
    sum_n = n * (n + 1) / 2

    # S2 = The sum of the first N odd integers.
    odd = sum([x for x in xrange(1, (n * 2 + 1), 2)])

    # S3 = The sum of the first N even integers.
    even = sum([x for x in xrange(2, (n * 2 + 1), 2)])

    yield sum_n, odd, even


# Output for each data set there is one line of output. The single output line consists of the data set number, K,
# followed by a single space followed by three space separated integers S1, S2 and S3 such that:
for i, l in enumerate(data_sets):

    gen = sum_num_and_odd_and_even(l[1])

    s1, s2, s3 = next(gen)

    print i + 1, s1, s2, s3

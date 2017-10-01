
# -*- coding:utf-8 -*-

import sys

# Read data
test_cases = []
for line in sys.stdin:
    test_cases += map(int, line.split())


# Compute the number digits sum
def sum_digits(num):

    sum_digits = 0

    while num != 0:
        sum_digits += num % 10
        num /= 10

    return sum_digits


# Return a number p which is the minimal number such that N⋅p has the same sum of digits as N and p is bigger than 10
def minimal_number(n):

    p = 11
    n_sum = sum_digits(n)

    while True:

        n_x_p = p * n
        n_x_p_sum = sum_digits(n_x_p)

        if n_sum == n_x_p_sum:
            break
        else:
            p += 1

    return p


# Output p
for n in test_cases[:-1]:
    print minimal_number(n)


# -*- coding:utf-8 -*-

import sys

# Read data
input_val = []
for line in sys.stdin:
    input_val += line.split()

# Assign variables
lower_bound, upper_bound, target_sum = input_val[0], input_val[1], input_val[2]


def sum_digits(num):
    """
    Determine the sum of the digits for the number
    :param num: an integer
    :return: an integer, digits sum
    """
    digits_sum = 0
    while num != 0:
        digits_sum += num % 10
        num //= 10
    return digits_sum


def find_min_num(lower_bound, upper_bound, target_sum):
    """
    Find minimum number
    :param lower_bound: an integer
    :param upper_bound: an integer
    :param target_sum: an integer
    :return: an integer, min number
    """
    for num in xrange(lower_bound, upper_bound + 1):
        if sum_digits(num) != target_sum:
            num += 1
        else:
            return num


def find_max_num(lower_bound, upper_bound, target_sum):
    """
    Find maximal number
    :param lower_bound: an integer
    :param upper_bound: an integer
    :param target_sum: an integer
    :return: an integer, max number
    """
    for num in reversed(xrange(lower_bound, upper_bound + 1)):
        if sum_digits(num) != target_sum:
            num -= 1
        else:
            return num

min_num = find_min_num(lower_bound, upper_bound, target_sum)
max_num = find_max_num(lower_bound, upper_bound, target_sum)

# The first line of output must contain the integer N from the task.
# The second line of output must contain the integer M from the task.
print min_num, '\n', max_num

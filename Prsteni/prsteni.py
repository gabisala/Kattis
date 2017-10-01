
# -*- coding:utf-8 -*-

import sys

# Read data
data = [map(int, line.split()) for line in sys.stdin]

# Assign variables
first_circle = data[1][0]
circles = data[1][1:]


def gcd(a, b):
    """
    Find the greatest common divisor of two positive integers
    :param a: positive integer
    :param b: positive integer
    :return: a positive integer, the greatest common divisor of a & b. 
    """
    # Your code here
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# The output must contain N−1 lines. For every ring other than the first, in the order they are given in the input,
# output a fraction A/B, meaning that the respective ring turns A/BA/B times while the first ring turns once. The
# fractions must be in reduced form (the numerator and denominator must not have a common divisor larger than 1).
for c in circles:

    # Find greatest common divisor for the two numbers
    greatest_common_divisor = gcd(first_circle, c)

    # Output a fraction
    print '{}/{}'.format(first_circle / greatest_common_divisor, c / greatest_common_divisor)

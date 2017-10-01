
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data += line.split()

# Create the battleground, two lists with N, M digits converted to lists
integers = [map(int, list(n)) for n in data]


def fix_less_digits(n, m):
    """
    If a number doesn’t consist of a corresponding digit, then we consider it to be zero
    Fix the list if it has less digits,  by adding 0 in front of the list
    :param n: a list of digits, one of the integers from the task
    :param m: a list of digits, one of the integers from the task
    :return: a tuple with two fixed lists
    """

    # Fix n list
    if len(n) < len(m):
        dif = len(m) - len(n)
        n = [0] * dif + n

    # Fix m list
    else:
        dif = len(n) - len(m)
        m = [0] * dif + m

    return n, m


def compare_integers(n, m):
    """
    Compares digit n to the corresponding digit of the other number m
    :param n: a list of digits, one of the integers from the task
    :param m: a list of digits, one of the integers from the task
    :return: a tuple with two lists containing bigger digits from the numbers
    """

    # Compare itself to the corresponding digit of the other number
    n_winner = [i for i, j in zip(n, m) if i >= j]
    m_winner = [i for i, j in zip(m, n) if i >= j]

    return n_winner, m_winner


def create_new_value(digits):
    """
    Create values after collision
    :param digits: a list, digits of the number
    :return: If it happens that all the digits of one number fell out,
    then for that number output the message “YODA”, else output new number
    """

    # If empty list
    if not digits:
        value = 'YODA'

    # List to string to int
    else:
        digits_to_str = ''.join([str(d) for d in digits])
        value = int(digits_to_str)

    return value


def collision_of_integers(integers):
    """
    For two given integers, determine their values after collision. If it happens that all the digits of one number
    fell out, then for that number output the message “YODA”.
    :param integers: a list with two lists, numbers digits
    :return: int or 'YODA', new values for the two given integers
    """

    # Assign N
    n = integers[0]

    # Assign M
    m = integers[1]

    # Both integers have the same number of digits
    if len(n) == len(m):

        n, m = compare_integers(n, m)
        n = create_new_value(n)
        m = create_new_value(m)

        return n, m

    # Integers have diferent number of digits
    else:
        n, m = fix_less_digits(n, m)
        n, m = compare_integers(n, m)
        n = create_new_value(n)
        m = create_new_value(m)

        return n, m


# Output
n_new, m_new = collision_of_integers(integers)
print n_new
print m_new


# -*- coding:utf-8 -*-

import sys

# Read data
data = sys.stdin.readline()
integers = data.split()

# Three integers less than 100
first, second, third = integers

# Basic arithmetic operations
arithmetic_operations = ['+', '-', '*', '/']

# Output a valid equation
for operator in arithmetic_operations:

    # Create expressions to be evaluated
    left_side_equal = '{}{}{}{}{}'.format(first, '==', second, operator, third)
    right_side_equal = '{}{}{}{}{}'.format(first, operator, second, '==', third)

    # Evaluate and print if expression is True for the right side and left side if right is False
    try:

        if eval(right_side_equal):
            print '{}{}{}{}{}'.format(first, operator, second, '=', third)
            break

        elif eval(left_side_equal):
            print '{}{}{}{}{}'.format(first, '=', second, operator, third)
            break

    except ZeroDivisionError:
        pass

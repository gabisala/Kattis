
# -*- coding:utf-8 -*-

import sys

# Map ascii representation to numbers and plus sign
ascii_to_numbers = {

    'xxxxxx...xx...xx...xx...xx...xxxxxx': '0',
    '....x....x....x....x....x....x....x': '1',
    'xxxxx....x....xxxxxxx....x....xxxxx': '2',
    'xxxxx....x....xxxxxx....x....xxxxxx': '3',
    'x...xx...xx...xxxxxx....x....x....x': '4',
    'xxxxxx....x....xxxxx....x....xxxxxx': '5',
    'xxxxxx....x....xxxxxx...xx...xxxxxx': '6',
    'xxxxx....x....x....x....x....x....x': '7',
    'xxxxxx...xx...xxxxxxx...xx...xxxxxx': '8',
    'xxxxxx...xx...xxxxxx....x....xxxxxx': '9',
    '.......x....x..xxxxx..x....x.......': '+',
}

# Map numbers and plus sign to ascii representation
numbers_to_ascii = {

    '0': ['xxxxx', 'x...x', 'x...x', 'x...x', 'x...x', 'x...x', 'xxxxx'],
    '1': ['....x', '....x', '....x', '....x', '....x', '....x', '....x'],
    '2': ['xxxxx', '....x', '....x', 'xxxxx', 'x....', 'x....', 'xxxxx'],
    '3': ['xxxxx', '....x', '....x', 'xxxxx', '....x', '....x', 'xxxxx'],
    '4': ['x...x', 'x...x', 'x...x', 'xxxxx', '....x', '....x', '....x'],
    '5': ['xxxxx', 'x....', 'x....', 'xxxxx', '....x', '....x', 'xxxxx'],
    '6': ['xxxxx', 'x....', 'x....', 'xxxxx', 'x...x', 'x...x', 'xxxxx'],
    '7': ['xxxxx', '....x', '....x', '....x', '....x', '....x', '....x'],
    '8': ['xxxxx', 'x...x', 'x...x', 'xxxxx', 'x...x', 'x...x', 'xxxxx'],
    '9': ['xxxxx', 'x...x', 'x...x', 'xxxxx', '....x', '....x', 'xxxxx'],
}


def read_display(display):
    """
    Convert input data a list of lists, every digit ascii representation
    :param display: a generator, input data row by row
    :return: a list of lists, every digit ascii representation
    """

    # Store the ascii representation for every digit and the plus sign
    ascii_digits = []

    # Read row by row
    for r in xrange(7):

        # Select characters
        row = next(display)

        # Cut row in layers for every digit
        digit = [row[i:i + 5] for i in xrange(0, len(row), 6)]

        # Add layer to the appropriate digit by his location
        for i, layer in enumerate(digit):
            try:
                ascii_digits[i].append(layer)

            # If first layer of the digit
            except IndexError:
                ascii_digits.append([])
                ascii_digits[i].append(layer)

    return ascii_digits


def convert_to_integers(ascii_digits, ascii_to_numbers):
    """
    Converts ascii digits from the display to integers (as strings, ex: '4')
    :param ascii_digits: a list of lists, every digit ascii representation
    :param ascii_to_numbers: a dictionary, map ascii to numbers(strings)
    :return: a string, representing the two integers addition
    """

    # Store mathematical expression
    expression = []

    # Convert
    for d in ascii_digits:

        ascii_digit = ''.join(d)
        expression.append(ascii_to_numbers.get(ascii_digit))

    return ''.join(expression)


def add_integers(math_expression):
    """
    Compute the result of the integers addition
    :param math_expression: a string, representing the two integers addition
    :return: a string, the addition result
    """

    # Assign integers
    first, second = math_expression.split('+')

    # Compute the addition result
    result = str(int(first) + int(second))

    return result


def convert_to_ascii(addition_result, numbers_to_ascii):
    """
    Convert the addition result to an ascii representation
    :param addition_result: a string, the addition result
    :param numbers_to_ascii: a dictionary, map numbers(strings) to ascii representation(list of strings)
    :return: a list of lists, every digit ascii representation
    """

    # Store the ascii representation for every digit and the plus sign
    representation = []

    for digit in addition_result:

        # Get the ascii representation for every digit in result
        ascii_digit = numbers_to_ascii.get(digit)

        # Add layer to the appropriate digit by his location
        for i, layer in enumerate(ascii_digit):

            try:
                representation[i].append(layer)

            # If first layer of the digit
            except IndexError:
                representation.append([])
                representation[i].append(layer)

    return representation


# Read input data
data = (line.strip() for line in sys.stdin)

# Read digits and the plus sign from display
digits = read_display(data)

# Convert to integers
expression = convert_to_integers(digits, ascii_to_numbers)

# Add the two integers
result = add_integers(expression)

# Create ascii output
ascii_representation = convert_to_ascii(result, numbers_to_ascii)

# Output 7 lines containing ASCII art corresponding to the result of the addition, without leading zeros.
for r_row in ascii_representation:
    print '.'.join(r_row)

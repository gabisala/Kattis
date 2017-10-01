
# -*- coding:utf-8 -*-

import sys

# Read data
binary = sys.stdin.readline().strip()


def pad_binary(binary_numeral):
    """
    # Pad the binary numeral with zeros on the left until the number of digits is divisible by three.
    :param binary_numeral: a string, binary numeral
    :return: a string, padded binary numeral
    """

    # Pad binary string
    binary_padded = binary_numeral

    # Add one zero till the padded version of binary is divisible by three
    while len(binary_padded) % 3 != 0:
        binary_padded = '0' + binary_padded

    return binary_padded


def group_digits(binary_numeral):
    """
    Group adjacent binary digits into groups of 3 digits.
    :param binary_numeral: a string, binary numeral
    :return: a list of strings(3 digits)
    """

    # Pad number if necessary
    binary_padded = pad_binary(binary_numeral)

    # Group adjacent binary digits into groups of 3 digits
    groups = [binary_padded[i:i + 3] for i in range(0, len(binary_padded), 3)]

    return groups


def create_octal_digits(groups):
    """
    # Replace each group of binary digits with the corresponding octal digit (as in Table 1).
    :param groups: a list of strings(3 digits)
    :return: a list, the number in octal
    """

    # Binary digits mapped to the corresponding octal digit
    oclat_digits = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}

    # The number in octal
    octal_number = []

    # For every group find the octal digit and add it to the octal number
    for group in groups:
        octal_number.append(oclat_digits[group])

    return octal_number


# Output the number in octal.
grouped = group_digits(binary)
number = create_octal_digits(grouped)
print ''.join(number)

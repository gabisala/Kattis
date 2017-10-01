
# -*- coding:utf-8 -*-

import sys

# Read number to convert
num = int(raw_input())


# Convert to reversed binary
def convert_to_binary(num):
    num_in_binary = ''

    while num > 0:
        binary = num % 2
        num_in_binary += str(binary)
        num /= 2

    return num_in_binary[::-1]


reversed_binary = convert_to_binary(num)


# Convert to integer
def convert_to_integer(reversed_binary):
    binary = list(reversed_binary)
    binary_to_num = 0

    for digit_index, digit in enumerate(binary):
        binary_to_num += int(digit) * 2 ** int(digit_index)

    return binary_to_num


integer = convert_to_integer(reversed_binary)
print integer

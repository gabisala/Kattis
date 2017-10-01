
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(map(int, line.split()))


def arithmetic(sequence):
    """
    Checks if the sequence is an arithmetic sequence
    :param sequence: a list, a number sequence
    :return: a bool, True if sequence, otherwise False
    """

    # Calculate the difference between the second number in sequence and the first
    difference = sequence[1] - sequence[0]
    # print difference

    # Check the difference for the next consecutive number and return False if difference changes
    for i, num in enumerate(sequence[1:]):

        check_difference = sequence[i+1] - sequence[i]

        if check_difference != difference:
            return False

    # Otherwise the sequence is arithmetic
    return True


# For each sequence, output a line that says “arithmetic” if the sequence is an arithmetic sequence.
# Output “permuted arithmetic” if the sequence can be reordered to make an arithmetic sequence.
# Otherwise, output “non-arithmetic”.
for seq in data[1:]:

    number_sequence = seq[1:]

    if arithmetic(number_sequence):
        print 'arithmetic'

    elif arithmetic(sorted(number_sequence)):
        print 'permuted arithmetic'

    else:
        print 'non-arithmetic'

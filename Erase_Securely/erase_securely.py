
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data += line.split()


def erase_bits(bits):
    """
    Overwritte bits
    :param bits: represent the bits of the file before deletion
    :return: a string of bits after file deletion
    """

    bits_erased = ''

    # Switch 0 with 1 and 1 with 0
    for bit in bits:
        if bit == '0':
            bits_erased += '1'
        elif bit == '1':
            bits_erased += '0'

    return bits_erased


# Output a single line containing either the words “Deletion succeeded” if each bit is switched NN times or
# “Deletion failed” if this is not the case.

# If n is odd
if int(data[0]) % 2 != 0:
    if erase_bits(data[1]) == data[2]:
        print 'Deletion succeeded'
    else:
        print 'Deletion failed'

# If n is even
else:
    if data[1] == data[2]:
        print 'Deletion succeeded'
    else:
        print 'Deletion failed'

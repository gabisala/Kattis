
# -*- coding:utf-8 -*-

import sys
import math

# Read data
data = []

for line in sys.stdin:
    data += line.split()


def decoder(secret):
    """
    Find original message

    :param secret: coded message
    :return: original message
    """

    # Calculate square row length
    square_length = int(math.sqrt(len(secret)))

    # Populate the rows
    rows = []
    temp_secret = list(secret)

    for x in xrange(square_length):
        rows.append(temp_secret[0: square_length])
        temp_secret = temp_secret[square_length:]

    # Rearrange letters
    decode = [row.pop(-1) for row in rows * square_length]

    # Original message
    return ''.join(decode)


# Per test case output one line with the original message.
for secret in data[1:]:
    print decoder(secret)

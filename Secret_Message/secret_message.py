
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data += line.split()


def padded_message(message):
    """
    Create a padded message 
    :param message: original message
    :return: original message + '*' * (m - l) 
    """

    l = len(message)

    # Find K and M such that M = K**2 M >= L
    k = 1
    while k**2 < l:
        k += 1

    m = k**2

    # Padded message
    padded_message = message + '*' * (m - l)

    return k, padded_message


def secret_message(k, padded_message):
    """
    Converts padded message to a secret message
    :param k: number of cell and rows(equal)
    :param padded_message: padded_message
    :return: secret message
    """

    # Split message in to chunks of length K
    chunks, chunk_size = len(padded_message), len(padded_message) / k
    table = [padded_message[i:i+chunk_size] for i in xrange(0, chunks, chunk_size)]

    # Rotate table
    rotate_tabele = [row[-i] for i in xrange(1, k + 1) for row in table if row[-i] != '*'][::-1]

    # Output secret message
    return ''.join(rotate_tabele)


# For each original message, output the secret message
for message in data[1:]:
    k, p_message = padded_message(message)
    print secret_message(k, p_message)


# -*- coding:utf-8 -*-

import sys
from itertools import combinations
from collections import deque

# Read data
data = []

for line in sys.stdin:
    data += line.split()


def unique_compound_words(a_list):
    """
    Write a program that reads a list of words from standard input and prints out a sorted list of all unique compound
    words that can be made by concatenating two different words from the input list. If the same compound word can be
    formed more than one way, it should only be listed once in the output.
    :param a_list: a list of words
    :return: a set of unique compound words
    """

    # Number of elements in the list
    num_words = len(data)

    # Create a deque
    d = deque(data)

    compound_words = []

    # Rotate deque and compute permutations for every deque
    for s in xrange(num_words):
        # Rotate left
        d.rotate(-1)

        # Compute permutations and add them to a list
        new_compound_words = sorted([''.join(l) for l in list(combinations(d, 2))])

        # Add list to main list
        compound_words.extend(new_compound_words)

    return set(compound_words)

# Output unique compound words, one per line
unique = unique_compound_words(data)

for u in sorted(unique):
    print u

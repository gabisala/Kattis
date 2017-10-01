
# -*- coding:utf-8 -*-

import sys

# Read data
data = [line.split() for line in sys.stdin]


def sort_segments(case):
    """
    Sort the segments in blue and red
    :param case: a list of test cases
    :return: a tuple with blue and red segments lists sorted from big to small
    """
    blue = []
    red = []
    for segment in case:

        if segment[-1] == 'B':
            blue.append(int(segment[:-1]))
        else:
            red.append(int(segment[:-1]))

    # sort from big to small
    blue.sort(reverse=True)
    red.sort(reverse=True)

    return blue, red


def create_loop(segments):
    """
    Create loop of segments
    :param segments: blue and red segments
    :return: loop, pairs of blu, red from big to small
    """
    blue, red = segments
    loop = []

    while len(blue) is not 0 and len(red) is not 0:
        loop.append((blue[0], red[0]))
        del blue[0]
        del red[0]

    return loop


def measure_rope(loop):
    """
    Measure the rope
    :param loop: pairs of blu, red from big to small
    :return: maximum length of the rope loop that can be generated with the rope segments provided
    """
    measure = []

    # Note that pieces of string that have length 1, if used in making the cycle, might get reduced to just a pair of
    # knots of total length 0. This is allowed, and each such piece counts as having been used.
    for s in loop:

        if s[0] > 1 and s[1] > 1:
            measure.append(s[0] + s[1] - 1)
        else:
            measure.append(max(s[0], s[1]))
        measure.append(-1)

    return sum(measure)

# For each test case, output one line containing "Case #xx: " followed by the
# maximum length of the rope loop that can be generated with the rope segments provided.

for i, case in enumerate(data[2::2]):

    segments = sort_segments(case)
    loop = create_loop(segments)
    measure = measure_rope(loop)

    print 'Case #{}: {}'.format(i + 1, measure)

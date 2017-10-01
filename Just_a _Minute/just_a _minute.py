
# -*- coding:utf-8 -*-

import sys


def compute_average(measurements):
    """
    Compute the average length of an S.L. minute, measured in real minutes
    :param measurements: a list of lists(integers)
    :return: a float, average length of an S.L. minute
    """

    # Store the subway service and the wait time in second
    sl = []
    wait = []

    # Measurements in seconds
    for measurement in measurements:
        sl_in_seconds = measurement[0] * 60
        wait_seconds = measurement[1]

        sl.append(sl_in_seconds)
        wait.append(wait_seconds)

    # Compute average waiting time
    average = sum(wait) / sum(sl)

    return average


# Store case data except first entry
data = [map(float, line.split()) for line in sys.stdin][1:]

# Compute average of an S.L. minute
average = compute_average(data)

# Output average if bigger than normal minute
if average > 1.0:
    print average

# If shorter than or equal to a normal minute
else:
    print 'measurement error'

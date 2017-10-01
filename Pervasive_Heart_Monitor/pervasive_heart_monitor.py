
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(line.split())


def average_heart_rate(customer):
    """

    :param customer: name and heart rate measurements
    :return: average heart rate and name
    """

    name = []
    readings = []

    for reading in customer:

        try:
            readings.append(float(reading))
        except ValueError:
            name.append(reading)

    average = sum(readings) / len(readings)

    return average, ' '.join(name)


# For each customer in the order given in the input, print a line with the average of all their heart rate readings,
# followed by the name. The average heart rate should be accurate within 0.01 beats per minute.

for l in data:
    average_rate, customer_name = average_heart_rate(l)
    print average_rate, customer_name

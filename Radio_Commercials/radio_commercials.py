
# -*- coding:utf-8 -*-

import sys


def max_sequence(radio_listeners, commercial_breaks, break_price):
    """
    Finds the continuous sequence of commercial breaks such that their profit is maximal.
    Kadane's algorithm, largest sum contiguous sub-array
    :param radio_listeners: a list of integers, the number of listeners on every commercial break
    :param commercial_breaks: an integer, number of commercial breaks
    :param break_price: an integer, the price of one commercial break
    :return: integer, the biggest expected extra profit from selecting a continuous sequence of commercial breaks.
    """

    # Current profit
    current_sum = 0
    current_index = None

    # Best profit so far
    best_sum = 0
    best_start_index = None
    best_end_index = None

    for i in range(commercial_breaks):

        # Calculate current profit
        val = current_sum + radio_listeners[i] - price

        # If profit
        if val > 0:

            if current_sum == 0:
                current_index = i

            current_sum = val

        # Else reset
        else:
            current_sum = 0

        # If current profit is bigger than past profit
        if current_sum > best_sum:

            best_sum = current_sum
            best_start_index = current_index
            best_end_index = i

    # Slice best sequence
    continuous_sequence = radio_listeners[best_start_index: best_end_index + 1]

    # Compute expected extra profit
    profit = sum(continuous_sequence) - (break_price * len(continuous_sequence))

    return profit


# Read data
data = []

for line in sys.stdin:

    data.append(map(int, line.split()))

# Assign variables
breaks = data[0][0]
price = data[0][1]
listeners = data[1]

# Output contains one line with one integer – the biggest expected extra profit Onid can get by selecting a continuous
# sequence of commercial breaks.
print max_sequence(listeners, breaks, price)

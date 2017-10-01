
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:

    data.append(line.split())


cases = []

# Convert data to a list of test cases
for l in data[1:]:

    case = list(l[0])

    for num in l[1:]:
        case.append(int(num))

    cases.append(case)


def hour_to_minutes(hour):
    """
    Convert hour in minutes
    :param hour: an integer, current hour
    :return: an integer, minutes
    """

    # If midnight, use 24 instead of 0
    if hour == 0:
        minutes = 24 * 60

    else:
        minutes = hour * 60

    return minutes


def minutes_to_hour(minutes):
    """
    Converts from minutes back to hour, minutes
    :param minutes: int, new time in minutes
    :return: a tuple, new hour and new minutes
    """

    # Convert back from minutes
    new_hour = minutes // 60
    new_minutes = minutes % 60

    # If new hour bigger than 24
    if new_hour > 24:
        new_hour -= 24

    return new_hour, new_minutes


def adjust_clock(roll_clock, minutes_to_change, current_hour, current_minutes):
    """
    Compute new time in minutes, after adjustment
    :param roll_clock: a single character to indicate whether the clock will roll forwards (F) or backwards (B)
    :param minutes_to_change: an integer indicating the number of minutes to change by
    :param current_hour: an integer indicating the hour the clock currently reads (without leading zeros)
    :param current_minutes: an integer indicating the minutes the clock currently reads
    :return: an integer, new time represented in minutes
    """

    # Transform hour in minutes
    minutes = hour_to_minutes(current_hour)

    # Current time in minutes
    time =  minutes + current_minutes

    # New time in minutes
    time_adjustment = 0

    # Roll the clock backwards
    if roll_clock == 'B':

        # Fix negative time by adding 24 hours in minutes
        if time < minutes_to_change:

            time_adjustment = ((24 * 60) + time) - minutes_to_change

        else:
            time_adjustment = time - minutes_to_change

    # Roll the clock forward
    elif roll_clock == 'F':

        time_adjustment = time + minutes_to_change

    return time_adjustment


def new_time(time_adjusted):
    """
    Convert minutes back to hours and minutes and format time after the adjustment has occurred
    :param time_adjustment: an integer, new time represented in minutes
    :return: a string, the new time (hours in 24-hour format, followed by a space, followed by minutes)
    """

    new_hour, new_minutes = minutes_to_hour(time_adjusted)

    # If midnight, use 0 instead of 24
    if new_hour == 24:
        return '{} {}'.format(0, new_minutes)

    else:
        return '{} {}'.format(new_hour, new_minutes)


# Output
# For each test case, give the time (hours in 24-hour format, followed by a space, followed by minutes) after
# the adjustment has occurred, one test case per line. You may report the numbers without leading zeros.
for c in cases:

    roll, change, hour, minutes = c

    adjusted = adjust_clock(roll, change, hour, minutes)
    print new_time(adjusted)

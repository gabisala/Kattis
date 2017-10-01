
# -*- coding:utf-8 -*-

import sys

# Read data
data = [line.split() for line in sys.stdin]


# Develop a program to generate a report of the day’s orders
def day_report(reports):
    """
    For each day, print out a report of who ordered each menu item, one line per menu item.
    :param reports: list of lists of clients names and what items they ordered
    :return: a dict, key = name, val = items
    """

    # A dict with menu items as keys, and who ordered what as values
    menu_orders = {}

    # For each client
    for report in reports:

        client = report[0]
        order = report[1:]

        for item in order:

            if item not in menu_orders.keys():
                menu_orders[item] = [client]
            else:
                menu_orders[item] += [client]

    return menu_orders

# Cut test cases
num_customers = int(data[0][0])
start_day = 1
finish_day = num_customers + 1

# While case is not 0
# For each day, print out a report of who ordered each menu item, one line per menu item. The line should give the name
# of the menu item, followed by a space-separated list of all the people who ordered it. The list of menu items for a
# given day should be sorted lexicographically, and the list of names reported for an item should also be sorted
# lexicographically. Print a blank line after the report for each day.
while num_customers != 0:

    day_reports = data[start_day: finish_day]
    menu_orders = day_report(day_reports)

    # For each item output who ordered
    for k, v in sorted(menu_orders.iteritems()):
        print '{} {}'.format(k, ' '.join(sorted(v)
))
    print ''

    # Move to next case
    data = data[finish_day:]

    # Reset cut
    num_customers = int(data[0][0])
    start_day = 1
    finish_day = num_customers + 1

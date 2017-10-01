
# -*- coding:utf-8 -*-

import sys

# Read data
log = []

for line in sys.stdin:
    log.extend(line.split())

# Present day
day = 1

# Check every entry in the amusement park log
for i, entry in enumerate(log):

    # When the park opens
    if entry == 'OPEN':

        # Reset customers for a new day
        customers = {}


    # When a customer enters
    elif entry == 'ENTER':

        # Find his name
        name = log[i + 1]

        # If customers has bean before, in the same day
        if customers.has_key(name):
            # Add a new enter time
            customers[name].append(int(log[i + 2]))

        # If first entry in this day
        else:
            enter_time = int(log[i + 2])
            customers[name] = [enter_time]


    # When a customer lives
    elif entry == 'EXIT':

        # Find his name
        name = log[i + 1]

        # Find exit time
        exit_time = int(log[i + 2])

        # Compute his time spent in the park
        customers[name][-1] = exit_time - customers[name][-1]


    # When the park closes
    elif entry == 'CLOSE':

        # Output the present day
        print 'Day {}'.format(day)

        # Add day passed
        day += 1

        # For each day, print out a report. Give the total bill for each customer. Sort your report
        # alphabetically by customer name and leave a blank line between reports for consecutive days.
        for customer, time in sorted(customers.iteritems()):
            # Calculate bill
            bill = sum(time) * 0.10

            # Output bill
            print '{} ${}'.format(customer, '%.2f' % bill)

        print ''

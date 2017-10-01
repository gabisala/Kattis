
# -*- coding:utf-8 -*-

import sys

# Read data
for line in sys.stdin:

    try:

        # Assign values
        no_advertise, advertise, cost = map(int, line.split())

        # If more money after advertise
        if no_advertise < advertise - cost:
            print 'advertise'

        # If it does not make any difference
        elif no_advertise == advertise - cost:
            print 'does not matter'

        # If less money after advertise
        else:
            print 'do not advertise'

    # Pass first line of input (number of test cases)
    except ValueError:
        pass

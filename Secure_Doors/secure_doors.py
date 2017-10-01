
# -*- coding:utf-8 -*-

import sys

# Read data
entry_log = [line.split() for line in sys.stdin][1:]

# Store name and status
card_check = {}

# Check employees cards and print name and status
for card in entry_log:

    # Read card
    status, name = card

    # If first entry
    if name not in card_check.keys() and status == 'entry':
        card_check[name] = status
        print '{} {}'.format(name, 'entered')

    # If first entry anomaly
    elif name not in card_check.keys() and status == 'exit':
        print '{} {} {}'.format(name, 'exited', '(ANOMALY)')

    # If another entry anomaly entered
    elif name in card_check.keys() and status == 'entry':
        if card_check[name] == 'entry':
            print '{} {} {}'.format(name, 'entered', '(ANOMALY)')
        else:
            card_check[name] = status
            print '{} {}'.format(name, 'entered')

    # If another entry anomaly exited
    elif name in card_check.keys() and status == 'exit':
        if card_check[name] == 'exit':
            print '{} {} {}'.format(name, 'exited', '(ANOMALY)')
        else:
            card_check[name] = status
            print '{} {}'.format(name, 'exited')

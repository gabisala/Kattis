
# -*- coding:utf-8 -*-

import sys
from collections import OrderedDict

# Read data
data = []

for line in sys.stdin:
    data.append(line.split())

# Current song
song = data[1]


# Create a ordered dictionary with notes as keys and empty values that will store staffs for every note
all_notes = 'GFEDCBAgfedcba'
representation = OrderedDict()

for key in all_notes:
    representation[key] = ''


# Notes with white pad
white_pad = 'ACEGbcdf'

# For every note in the song
for note in song:

    # For every key, value in the representation dictionary
    for k, v in representation.iteritems():

        # If the note has a second character it has more than one beat, play it how many times the character denotes
        if len(note) > 1:

            # How many times the note play's
            multiply = int(note[1])

            # Find the current note in the representation dictionary and edit it's value
            if note[0] == k:

                # Multiply note representation(*) and than add white padding
                if k in white_pad:
                    representation[k] += '*' * multiply + ' '

                # Otherwise multiply note and than add '-'
                else:
                    representation[k] += '*' * multiply + '-'

            # For the rest of the notes
            else:

                # If white padding needed add space as many as beats plus one
                if k in white_pad:
                    representation[k] += ' ' * multiply + ' '

                # Otherwise add '-' as many as beats plus one
                else:
                    representation[k] += '-' * multiply + '-'

        # If one beat note
        else:

            # Find the current note in the representation dictionary and edit it's value
            if note == k:

                # Add note representation(*) and than add white padding
                if k in white_pad:
                    representation[k] += '* '

                # Otherwise note representation(*) and than add '-'
                else:
                    representation[k] += '*-'

            # For the rest of the notes
            else:

                # If white padding needed add two spaces
                if k in white_pad:
                    representation[k] += '  '

                # Otherwise add two '--'
                else:
                    representation[k] += '--'


# Output every note
for k, v in representation.iteritems():
    print '{}: {}'.format(k, v[:-1])

# -*- coding:utf-8 -*-

import sys

# Input data
data = (line.strip('\n') for line in sys.stdin)

# While still data
while True:

    try:

        # Assign the number of cd's owned by Jack and Jill
        jack_num_cds, jill_num_cds = next(data).split()

        if jack_num_cds != '0' and jill_num_cds != '0':

            # Store the cd's in sets
            jack = set()
            jill = set()

            # Add the cd's to Jack's collection
            for cd in xrange(int(jack_num_cds)):

                jack.add(next(data))

            # Add the cd's to Jill's collection
            for cd in xrange(int(jill_num_cds)):

                jill.add(next(data))

            # Intersect the two collections and output a line containing one integer,
            # the number of CDs that Jack and Jill both own
            print len(jack & jill)

        # The input is terminated by a line containing two zeros
        else:
            break


    # If no more data break out of the loop
    except StopIteration:
        break


# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(map(int, line.split()))


def simultanously(earth, mars):
    """
    Count how long it will take until both planets are on day 0 of their orbits simultanously.
    :param earth: int, day earth orbit
    :param mars: int, day mars orbit
    :return: int, the smallest number of days until the two planets will both be on day 0 of their orbits
    """

    # Count days
    counter = 0

    # While mars and earth are not on day 0 of their orbits
    while True:

        # If the two planets will both be on day 0 of their orbits
        if earth == 0 and mars == 0:

            # Return number of days
            return counter

        # If not one day to the begging of a new year
        elif earth < 364 and mars < 686:

            earth += 1
            mars += 1
            counter += 1

        # If new year on earth and mars
        elif earth == 364 and mars == 686:

            earth = 0
            mars = 0
            counter += 1

        # If new year on earth
        elif earth == 364:

            earth = 0
            mars += 1
            counter += 1

        # If new year on mars
        elif mars == 686:

            mars = 0
            earth += 1
            counter += 1


# For each case, display the case number followed by the smallest number of days until the two planets will both be on
# day 0 of their orbits. Follow the format of the sample output.
for i, test in enumerate(data):

    # Assign current day
    earth = test[0]
    mars = test[1]
    num_days = simultanously(earth, mars)

    print 'Case {}: {}'.format(i + 1, num_days)

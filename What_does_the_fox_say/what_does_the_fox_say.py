
# -*- coding:utf-8 -*-

import sys
import itertools

# Read data
data = [line.strip('\n') for line in sys.stdin]


def fox_goes(case):
    """
    Find sounds made by the fox, in the order from the recording
    :param case: a list of strings, the test case
    :return: a string, the fox sound
    """

    # Case recording
    recording = case[0].split()

    # Cut data with the pre-gathered sounds
    pre_gathered_sounds = [s.split() for s in case[1:]]

    # Cut the sound for every animal
    animals_sounds = [l[l.index('goes') + 1:] for l in pre_gathered_sounds]

    # Create a list with all the known sounds
    other_animals = list(itertools.chain.from_iterable(animals_sounds))

    # Find the fox
    fox = [s for s in recording if s not in other_animals]

    return ' '.join(fox)


# For each test case, output one line containing the sounds made by the fox, in the order from the recording. You may
# assume that the fox was not silent (contrary to popular belief, foxes do not communicate by Morse code).
num_cases = int(data[0])

case = []

for s in data[1:]:

    if s[-1] == '?':

        # Output
        print fox_goes(case)
        case = []
    else:
        case.append(s)

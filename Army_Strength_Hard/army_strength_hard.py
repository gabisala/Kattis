
# -*- coding:utf-8 -*-

import sys

def battle(godzilla_army, mechaGodzilla_army):
    """
    Finds out who wins the war
    :param godzilla_army: a list of strings, representing godzilla's army
    :param mechaGodzilla_army: a list of strings, representing mechaGodzilla's army
    :return: a string, the winner, otherwise output the string “uncertain”
    """

    # Sort army's from strongest to weakest monster
    godzilla = sorted(godzilla_army)
    mechaGodzilla = sorted(mechaGodzilla_army)

    # Start battle
    while godzilla and mechaGodzilla:

        # If MechaGodzilla has the weakest monster or both armies have at least one of the weakest monsters
        if int(mechaGodzilla[-1]) <= int(godzilla[-1]):

            # The weakest monster of MechaGodzilla’s army is killed
            del mechaGodzilla[-1]

        # Otherwise
        else:

            # The weakest monster of Godzilla’s army is killed
            del godzilla[-1]


    # If Godzilla’s army wins
    if len(godzilla) > len(mechaGodzilla):
        return 'Godzilla'

    # If MechaGodzilla’s army wins
    elif len(godzilla) < len(mechaGodzilla):
        return 'MechaGodzilla'

    else:
        return 'uncertain'


# Store army's
godzillaArmy = []
mechaGodzillaArmy = []

# Army's position in input data
select_army = [3, 4]

# Read data
for i, line in enumerate(sys.stdin):

    # If we find Godzilla’s army
    if i == select_army[0]:

        # Prepare army
        godzillaArmy = line.strip().split()

        # Find the army position for the next test case
        select_army[0] += 4

    # If we find MechaGodzilla army
    elif i == select_army[1]:

        # Prepare army
        mechaGodzillaArmy = line.strip().split()

        # Find the army position for the next test case
        select_army[1] += 4

        # Start battle and find the winner if any
        print battle(godzillaArmy, mechaGodzillaArmy)

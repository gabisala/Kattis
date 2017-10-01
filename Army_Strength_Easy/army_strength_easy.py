
# -*- coding:utf-8 -*-

import sys

# Read data
data = [map(int, line.split()) for line in sys.stdin]


def war(godzilla_army, mecha_army):
    """
    Find the outcome of the battle
    :param godzilla_army: a list of ints
    :param mecha_army: a list of ints
    :return: a string, battle outcome
    """

    # Sort army's from weak to strong
    godzilla = sorted(godzilla_army)
    mecha = sorted(mecha_army)

    # While there are alive mosters
    while godzilla and mecha:

        # If godzilla soldier is stronger than mecha's
        if godzilla[0] < mecha[0]:
            godzilla.pop(0)

        # If mecha soldier is stronger than godzilla's
        elif godzilla[0] > mecha[0]:
            mecha.pop(0)

        # If there is a tie
        else:
            mecha.pop(0)

    # If no more soldiers in the two army's
    if not godzilla and not mecha:
        return 'uncertain'

    # If no more soldiers in godzilla's army
    elif not godzilla:
        return 'MechaGodzilla'

    # If no more soldiers in meca's army
    else:
        return 'Godzilla'


# For each test case, output a single line with a string that describes the outcome of the battle. If it is sure
# that Godzilla’s army wins, output the string “Godzilla”. If it is sure that MechaGodzilla’s army wins, output
# the string “MechaGodzilla”. Otherwise, output the string “uncertain”.
case = []

for l in data[2:]:

    # If list is empty or the last list in data
    if not l or l is data[-1]:

        # If the last list in data
        if l is data[-1]:

            case.append(l)
            godzilla_army = case[-2]
            mechagodzilla_army = case[-1]

            print war(godzilla_army, mechagodzilla_army)

        # If list is empty
        else:

            godzilla_army = case[-2]
            mechagodzilla_army = case[-1]

            print war(godzilla_army, mechagodzilla_army)
            case = []

    # Else add to case list
    else:
        case.append(l)

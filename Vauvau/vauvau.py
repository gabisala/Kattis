
# -*- coding:utf-8 -*-

import sys

# Read data
data = []
for line in sys.stdin:
    data += map(int, line.split())


# Compute dogs behaviour at specific minute of the day
def dogs_behaviour(dogs, man):
    """

    :param dogs: Both dogs behaviours
    :param man: Minute of the day
    :return: list[dog1, dog2], True if aggressive, False if calm
    """

    dogs_behaviour = []

    for dog in dogs:
        aggressive = dog[0]
        calm = dog[1]
        routine_length = aggressive + calm
        routine = list(xrange(1, routine_length + 1))

        behaviour = [True if (man % routine_length in routine[:aggressive]) else False]
        dogs_behaviour += behaviour

    return dogs_behaviour


# Check dogs timing
def dogs_timing(behaviour):
    """
    :param behaviour: list[dog1, dog2], True if aggressive, False if calm
    :return: 'both' if the two dogs are aggressive, 'one' if only one, 'none' if the two dogs are calm
    """

    if behaviour[0] is True and behaviour[1] is True:
        return 'both'
    elif behaviour[0] is True or behaviour[1] is True:
        return 'one'
    else:
        return 'none'


# Tuple with dog1, dog2 behaviour
dogs = data[0:2], data[2:4]

# Postman, milkman and garbage man
service_man = data[4:]

# Output for each of the three mans, postman, milkman and garbage man
for man in service_man:
    behaviour = dogs_behaviour(dogs, man)
    print dogs_timing(behaviour)

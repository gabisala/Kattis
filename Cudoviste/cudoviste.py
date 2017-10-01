
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.extend(line.split())

# Extract the city map from data
city_map = data[2:]


def count_squashe_cars(city_map):
    """
    Count the number of parking spaces Mirko can park on if he squashes
    0 cars, 1 car, 2 cars, 3 cars, 4 cars
    :param city_map: a list of strings
    :return: a list
    """

    # Store the squashed cars count
    count_cars = []

    # Foe every row in the table except the last one
    for i, row in enumerate(city_map[:-1]):

        # For every cell in row
        for j, cell in enumerate(row[:-1]):

            # A monster truck is quite huge, 2 by 2 cells
            up = cell + row[j + 1]  # the current cell plus the next one to it
            down = city_map[i + 1][j] + city_map[i + 1][j + 1]  # the corresponding cell from the next row and the next

            # Create space
            possible_space = up + down

            # If building in the parking space don't count it
            if '#' in possible_space:
                pass

            # Count cars in the parking space
            elif 'X' in possible_space:
                count_cars.append(possible_space.count('X'))

            # If no cars parked in space
            else:
                count_cars.append(0)

    return count_cars


# The output consists of five lines, the total number of parking spaces Mirko can park on if he squashes
# 0 cars (first line), 1 car (second line), 2 cars (third line), 3 cars (fourth line), 4 cars (fifth line).
parking_spaces = count_squashe_cars(city_map)

for squashed_car in xrange(5):

    if squashed_car in parking_spaces:
        print parking_spaces.count(squashed_car)

    else:
        print 0

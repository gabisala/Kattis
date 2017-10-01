
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(map(int, line.split()))

# The distance from the start
destination = data[0][1]

# A list of lists. Every list contains three integers, describing one traffic light.
# First int in list is the distance of the traffic light from the start of the road.
# The second ints denote how long the red and green lights are on, respectively.
traffic_lights = data[1:]


def waiting_time(current_time, red_on, green_on):
    """
    Compute the time spent at red light
    :param current_time: int, time passed since the start of the road
    :param red_on: int, number of seconds the red light is on
    :param green_on: int, number of seconds the green light is on
    :return: int, seconds spent waiting for the green light to turn on
    """

    # Traffic light time since start
    lights_time = 0

    # Time spent at red light
    waiting = 0

    # True if light is on, otherwise False
    red = True
    green = False


    # Figure out which light is on at the moment the car arrives at the traffic light
    while lights_time <= current_time:

        # If the light is red
        if red:

            # Add red light time to the overall traffic light time
            lights_time += red_on

            # Change light color
            red = False
            green = True

        # If the light is green
        elif green:

            # Add green light time to the overall traffic light time
            lights_time += green_on

            # Change light color
            red = True
            green = False

    # If the color changed to green
    if green:

        # The waiting time is time spent at traffic light minus the time spent on the road
        waiting = lights_time - current_time

    # If the color changed to red
    elif red:

        # The time spent at the traffic light is 0 because in the moment of arrival the light was green
        waiting = 0

    return waiting



def drive(traffic_lights):
    """
    Time needed to reach the end of the road
    :param traffic_lights: a list, all traffic lights positions and reg/green cycles
    :return: int, number of seconds spent on the road
    """

    # Last car position, either the start or the last traffic light
    last_position = 0

    # Time spent since start
    time = 0

    # For every traffic light
    for light in traffic_lights:

        # Current car position
        position = light[0]

        # Red and green time on
        red = light[1]
        green = light[2]

        # Distance traveled by the car
        traveled = (position - last_position)

        # Update current time, for every unit add one second
        time += traveled

        # Update position
        last_position = position

        # Update current time, add time spent at red light
        time += waiting_time(time, red, green)

    # If no more traffic light but the car is not at the end of the road
    if last_position < destination:

        # Add one second for every unit till the end of the road
        time += (destination - last_position)

    return time


# Output the time (in seconds) Luka needs to reach the end of the road.
print drive(traffic_lights)

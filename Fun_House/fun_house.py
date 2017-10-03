
# -*- coding:utf-8 -*-

import sys


def set_up_room(fun_house):
    """
    Create the room diagram and find the entrance position
    :param fun_house: a list of strings, the room rows representation
    :return: a tuple with a dictionary (position: character) and a tuple (entrance position)
    """

    # Map character position, (row, column): 'char', tuple: string
    diagram = {}

    # Entrance position
    entrance = False

    # Assign positions
    for i, row in enumerate(fun_house):

        if not entrance:
            if '*' in row:

                # Entrance found
                entrance = (i, row.find('*'))

        for j, character in enumerate(row):

            diagram[(i, j)] = character

    return diagram, entrance


def first_step(entrance, room_width, room_length):
    """
    Finds the direction to move, after entering the room
    :param entrance: a tuple, row and column index of the door
    :param room_width: int, how width is the room, walls included
    :param room_length: int, the length  the room, walls included
    :return: a string, the direction of the next move
    """

    # Door index for the row and the column
    row, column = entrance

    # If door on the north wall
    if row == 0:
        return 'down'

    # If door on the south wall
    elif row == room_length - 1:
        return 'up'

    # If door on the west wall
    elif column == 0:
        return 'right'

    # If door on the east wall
    elif column == room_width - 1:
        return 'left'


def move(position, direction):
    """
    Determine the new position after we move
    :param position: a tuple, position before we move
    :param direction: a string, the direction of the next move
    :return:a tuple, position after we move
    """

    row, column = position

    # If moving up
    if direction == 'up':
        row -= 1

    # If moving down
    elif direction == 'down':
        row += 1

    # If moving right
    elif direction == 'right':
        column += 1

    # If moving left
    elif direction == 'left':
        column -= 1

    # New position after moving inside the room
    new_position = row, column

    return new_position


def turn(previous_direction, mirrors):
    """
    Determines the new direction after we turn
    :param previous_direction: a string, direction before turning
    :param mirrors: a string, represented by the forward and backward slash characters (/ and \)
    :return: a string, direction after turning
    """

    new_direction = None

    if mirrors == '/':

        if previous_direction == 'up':
            new_direction = 'right'

        elif previous_direction == 'down':
            new_direction = 'left'

        elif previous_direction == 'right':
            new_direction = 'up'

        elif previous_direction == 'left':
            new_direction = 'down'

    # Use '\\' to escape '\'
    if mirrors == '\\':

        if previous_direction == 'up':
            new_direction = 'left'

        elif previous_direction == 'down':
            new_direction = 'right'

        elif previous_direction == 'right':
            new_direction = 'down'

        elif previous_direction == 'left':
            new_direction = 'up'

    return new_direction


def walk(room_diagram, position, width, length):
    """
    Walk into the room and find the wall where the door should be placed
    :param room_diagram: a dictionary (position: character)
    :param position: a tuple, our position in the room
    :param width: int, how width is the room, walls included
    :param length: int, the length  the room, walls included
    :return: a tuple, the position in the wall where the door should be placed
    """

    step_direction = None
    new_position = position
    exit_door = False

    # We walk till we find the position where the exit should be placed
    while not exit_door:

        # Determine position
        char = room_diagram[new_position]

        # If we hit the wall
        if char == 'x':
            exit_door = True

        # If no obstacle
        elif char == '.':
            new_position = move(new_position, step_direction)

        # If we find a mirror
        elif char == '/':
            step_direction = turn(step_direction, char)
            new_position = move(new_position, step_direction)

        # If we find a mirror
        elif char == '\\':
            step_direction = turn(step_direction, char)
            new_position = move(new_position, step_direction)

        # If we are at the entrance
        elif char == '*':
            step_direction = first_step(enter_door, width, length)
            new_position = move(new_position, step_direction)

    # Build exit here
    wall_exit = new_position

    return wall_exit


def create_exit(room, exit_position):
    """
    Build the exit door
    :param room: a list of strings, row by row representation of the room
    :param exit_position: a tuple, the position in the wall where the door should be placed
    :return: a list of strings, a room diagram which includes the proper placement of the exit door
    """

    # Add exit door
    row, column = exit_position
    wall = list(room[row])
    wall[column] = '&'
    modified_wall = ''.join(wall)

    # Create new diagram
    new_diagram = room[:row] + [modified_wall] + room[row + 1:]

    return new_diagram


# Read data
f = open('fun_house_data', 'r')
data = []

for line in sys.stdin:
    data += line.split()


# Houses layouts
houses = []

# Extract every case from input data
while data:

    # Select house
    start = 0
    finish = int(data[1]) + 2
    house = data[start: finish]
    houses.append(house)

    # Remove case from data
    data = data[finish:]


# Output
# For each test case, the first line will contain the word, HOUSE, followed by a space and then an integer that
# identifies the given fun house sequentially. Following that should be a room diagram which includes the proper
# placement of the exit door, as marked by an ampersand (&).
for i, house in enumerate(houses[:-1]):

    print 'HOUSE {}'.format(i + 1)

    room_width = int(house[0])
    room_length = int(house[1])
    fun_house = house[2:]

    # Create the room diagram and find the entrance position
    room, enter_door = set_up_room(fun_house)

    # Find the exit position
    exit_position = walk(room, enter_door, room_width, room_length)

    # Create a diagram which includes the proper placement of the exit door
    house_diagram = create_exit(fun_house, exit_position)

    # Output new diagram
    for line in house_diagram:
        print line

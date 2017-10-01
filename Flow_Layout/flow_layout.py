
# -*- coding:utf-8 -*-

import sys

# Generate test cases data
data = (map(int, line.split())for line in sys.stdin)


def create_window(maximum_width, rectangles):
    """
    Compute of the resulting window width and height
    :param maximum_width: an integer, window maximum width
    :param rectangles: a list of lists, each containing the dimensions of one rectangle, width first, then height
    :return: integers, width and height
    """

    # Initial values
    resulting_width = [0]
    resulting_height = [0]

    # Takes rectangular objects and places them in a rectangular window
    for rectangle in rectangles:

        # Rectangle measurements
        width, height = rectangle
        current_width = resulting_width[-1] + width

        # If still space on current row
        if current_width <= maximum_width:

            # Add current rectangle width to the previous rectangle
            resulting_width[-1] += width

            # If current rectangle has a bigger height than the previous one
            if resulting_height[-1] < height:

                # Replace the heights
                resulting_height[-1] = height

        # If no more space
        else:

            # Store current width and height
            resulting_width.append(width)
            resulting_height.append(height)

    # Return the widest row and the sum of the heights of the rows
    return max(resulting_width), sum(resulting_height)


# Window maximum width
max_width = 0

# While test cases
while True:

    # Generate data
    generated = next(data)

    # If one set of data
    if len(generated) == 1:

        if generated[0] != 0:

            # Assign maximum width of the window
            max_width = generated[0]

            # Reset rectangles for the next test case
            rectangles = []

        # If end of test cases
        else:
            break

    # If more sets of data
    else:

        # Store rectangles for the current test case
        if generated[0] != -1:
            rectangles.append(generated)

        # Output width and height of the resulting window
        else:
            window_width, window_height = create_window(max_width, rectangles)
            print '{} x {}'.format(window_width, window_height)

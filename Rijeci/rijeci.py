
# -*- coding:utf-8 -*-

import sys

# Read data
press_button = int(sys.stdin.readline())

# Store previous computed values
letters_cache = {}


# Compute after K times of pressing the button, how many
# letters A and how much letters B will be displayed on the screen
def num_letters(press_button):

    # If we have cached the value, return it
    if press_button in letters_cache:
        return letters_cache[press_button]

    # Compute the n-th term
    if press_button == 0:
        value = 0
    elif press_button == 1:
        value = 1
    elif press_button == 2:
        value = 1
    elif press_button > 2:
        value = num_letters(press_button - 1) + num_letters(press_button - 2)

    # Cache the value and return it
    c_value = letters_cache[press_button]
    return c_value

# Output the number of letters A and the number of letter B
print num_letters(press_button - 1), num_letters(press_button)

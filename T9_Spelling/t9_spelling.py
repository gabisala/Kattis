
# -*- coding:utf-8 -*-

import sys

# Read data
data = [line.strip('\n') for line in sys.stdin]

# Letters mapped to phone keys
characters_mapping = {

    ' ': '0',
    'a': '2', 'b': '22', 'c': '222',
    'd': '3', 'e': '33', 'f': '333',
    'g': '4', 'h': '44', 'i': '444',
    'j': '5', 'k': '55', 'l': '555',
    'm': '6', 'n': '66', 'o': '666',
    'p': '7', 'q': '77', 'r': '777', 's': '7777',
    't': '8', 'u': '88', 'v': '888',
    'w': '9', 'x': '99', 'y': '999', 'z': '9999'

}


def message_to_key_presses(message):
    """
    Translate message into a sequence of key presses
    :param message: string, message to translate
    :return: string, sequence of key presses
    """

    # Sequence of key presses
    message_in_digits = ''

    # Last key press
    last_press = 'None'

    # Translate
    for char in message:
        if char in characters_mapping.keys():

            # Assign key digit
            key_press = characters_mapping[char]

            # If letter is on the same key as last letter
            if key_press[0] == last_press[0]:
                # Add a space and the key
                message_in_digits += ' ' + key_press
                last_press = key_press[-1]

            # Otherwise
            else:
                # Add key
                message_in_digits += key_press
                last_press = key_press[-1]

    return message_in_digits


# For each test case, output one line containing “Case #xx: ” followed by the message translated into the
# sequence of key presses.
for i, message in enumerate(data[1:]):
    print 'Case #{}: {}'.format(i + 1, message_to_key_presses(message))

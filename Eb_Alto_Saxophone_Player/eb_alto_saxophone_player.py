
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(line.strip('\n'))


# 14 different notes. They are: C D E F G A B in one octave and C D E F G A B in a higher octave.
# We use c,d,e,f,g,a,b,C,D,E,F,G,A,B to represent them as keys
# and numbers in 1 to 10 to represent the fingers as values
notes = {

    'a': [2, 3],
    'A': [1, 2, 3],
    'c': [2, 3, 4, 7, 8, 9, 10],
    'b': [2],
    'e': [2, 3, 4, 7, 8],
    'd': [2, 3, 4, 7, 8, 9],
    'g': [2, 3, 4],
    'f': [2, 3, 4, 7],
    'F': [1, 2, 3, 4, 7],
    'C': [3],
    'G': [1, 2, 3, 4],
    'B': [1, 2],
    'E': [1, 2, 3, 4, 7, 8],
    'D': [1, 2, 3, 4, 7, 8, 9]

}


def fingers_presses(song):
    """
    Count the number of times each finger presses the button
    :param song: a string, containing the song. The only allowed characters are “cdefgabCDEFGAB”
    :return: a list, with the values for the number of times each finger presses the button
    """

    # 10 different fingers.
    # Numbers in 1 to 10 to represent the fingers as keys, and button presses as values
    # Count the number of times each finger presses the button

    fingers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

    # Previous note played
    previous_note = []

    # Check fingers values for each note
    for note in song:

        # Current note played
        current_note = []

        # A list with all fingers values
        note_fingers = notes[note]

        # For every finger used to play a note
        for finger in note_fingers:

            # If finger not already in use
            if finger not in previous_note:
                # Press the button
                current_note.append(finger)
                # Count the press
                fingers[finger] += 1

            # If finger on the button
            else:
                # Keep pressing the button
                current_note.append(finger)

        # Current note becomes the previous one, getting ready for a new cycle
        previous_note = current_note

    # A list, 10 numbers indicating the number of presses for each finger
    return fingers.values()


# For each test case, print 10 numbers indicating the number of presses for each finger.
# Numbers are separated by a single space.
for song in data[1:]:

    # If no song
    if song == '':
        print '0 0 0 0 0 0 0 0 0 0'

    else:
        # Count
        presses = fingers_presses(song)

        # Output
        for p in presses:
            print p,

        # Move to next line
        print ''

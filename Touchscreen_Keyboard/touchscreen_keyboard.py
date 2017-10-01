
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data += line.split()


# Create touchscreen keyboard
# Keyboard letters
keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

# Map letters to the keyboard position ('q': (0, 0) - q is located at the row 0 and column 0)
position = {}

for i, line in enumerate(keyboard):

    for j, char in enumerate(line):
        position[char] = (i, j)


def distance(typed_letter, proposed_letter):
    """
    Compute the distance between typed letter and the proposed letter
    :param typed_letter: a string, one char
    :param proposed_letter: a string, one char
    :return: an integer, distance
    """

    # If the typed letter is the same as the proposed_letter the distance is 0
    if typed_letter == proposed_letter:
        return 0

    # Otherwise
    else:

        # Find the positions for the typed and the proposed letter
        typed_row, typed_column = position.get(typed_letter)
        proposed_row, proposed_column = position.get(proposed_letter)

        # Compute distance between letters
        distance = abs(proposed_row - typed_row) + abs(proposed_column - typed_column)

        return distance


def spell_checker(typed_word, proposed_words):
    """
    Compute the distance between typed word and the proposed words
    :param typed_word: a string, user typed word
    :param proposed_words: a list, spell checker proposed words
    :return: a sorted list of tuples, each tuple contains the distance and the proposed word
    """

    # Store distance and word for every proposed word
    checker = []

    # Compute the distance and append distance and word
    for proposed in proposed_words:
        words_distance = sum([distance(a, b) for a, b in zip(typed_word, proposed)])
        checker.append((words_distance, proposed))

    return sorted(checker)


# Select all cases from data
cases = data[1:]

# For each test case, print the list of words sorted by their distance ascending. If two words have the same distance,
# sort them alphabetically. Print the distance of each word in the same line.
while cases:

    # Select case
    case_end = int(cases[1]) + 2
    case = cases[0: case_end]

    # Assign typed word end proposed words list
    typed = case[0]
    proposed = case[2:]

    # Check every proposed word
    checked = spell_checker(typed, proposed)

    # Format output
    for info in checked:
        print '{} {}'.format(info[1], info[0])

    # Remove processed case from cases
    cases = cases[case_end:]


# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(line.strip())

words = data[1:-1]
digits = data[-1]

keyboard = {

    'a': '2', 'b': '2', 'c': '2',
    'd': '3', 'e': '3', 'f': '3',
    'g': '4', 'h': '4', 'i': '4',
    'j': '5', 'k': '5', 'l': '5',
    'm': '6', 'n': '6', 'o': '6',
    'p': '7', 'q': '7', 'r': '7', 's': '7',
    't': '8', 'u': '8', 'v': '8',
    'w': '9', 'x': '9', 'y': '9', 'z': '9'

}


def possible_words(keyboard, words, digits):
    """
    Finds the number of words from the dictionary possible to construct from the letters on the keys determined by
    digits pressed on phone keyboard
    :param keyboard: a dictionary, letters in alphabet mapped to the corresponding digits on phone keyboard
    :param words: a list, T9 proposed words
    :param digits: a string, consisting of digits 2–9
    :return: a integer, number of words
    """

    # Count possible words
    possible = 0

    # For every digit pressed
    for i, digit in enumerate(digits):

        # If more then one possible word
        if len(words) > 1:

            for j, word in enumerate(words):

                try:

                    letter = word[i]

                    # If pressing the digit doesn't produce the letter
                    if keyboard.get(letter) != digit:
                        del words[j]

                # If word to short but has the correct letters
                except IndexError:

                    possible += 1
                    del words[j]


        # If a single possible word, check if correct
        elif len(words) == 1:

            word = words[0]

            for letter in word:

                if keyboard.get(letter) != digit:
                    break

            possible += 1
            del words[0]

    return possible + len(words)


# The first and only line of output must contain the number of words from the dictionary possible to construct from
# the letters on the keys determined by the string S(digits)
print possible_words(keyboard, words, digits)

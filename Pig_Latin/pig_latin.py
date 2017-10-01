
# -*- coding:utf-8 -*-

import sys

# Read data
data = [line.strip('\n') for line in sys.stdin]

# Vowels
vowels = ('a', 'e', 'i', 'o', 'u', 'y')


def translate_to_pig(text):
    """
    Translate from english to pig latin
    :param text: a string, in english
    :return: a string, in pig latin
    """

    translated = []

    # Split line in words, and translate each one
    for word in text.split():
        # print word

        # If a word begins with a vowel (a, e, i, o, u, or y), simply add yay to the end of the word. For this problem,
        # y is always a vowel. Examples: and → andyay, ordinary → ordinaryyay.
        if word[0] in vowels:
            translated.append(word + 'yay')

        # If a word begins with a consonant, take all of the letters before the first vowel and move them to the end
        # of the word, then add ay to the end of the word. Examples: pig → igpay, there → erethay.
        else:
            for i, c in enumerate(word):
                if c in vowels:
                    translated.append(word[i:] + word[:i] + 'ay')
                    break

    # Translated version of the text
    return ' '.join(translated)


# Output the text translated to Pig Latin
for line in data:
    print translate_to_pig(line)

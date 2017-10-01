
# -*- coding:utf-8 -*-

import sys

# Read data
messages = []
for line in sys.stdin:
    messages += line.split()


# Assign morse code for each letter and compute the length of the code
morse = {',': '.-.-', '.': '---.', '?': '----', 'A': '.-', 'C': '-.-.', 'B': '-...', 'E': '.', 'D': '-..', 'G': '--.',
         'F': '..-.', 'I': '..', 'H': '....', 'K': '-.-', 'J': '.---', 'M': '--', 'L': '.-..', 'O': '---', 'N': '-.',
         'Q': '--.-', 'P': '.--.', 'S': '...', 'R': '.-.', 'U': '..-', 'T': '-', 'W': '.--', 'V': '...-', 'Y': '-.--',
         'X': '-..-', 'Z': '--..', '_': '..--'}


morse_flip = {'---': 'O', '--.': 'G', '-...': 'B', '-..-': 'X', '.-.': 'R', '--.-': 'Q', '--..': 'Z', '.--': 'W',
              '.-': 'A', '..': 'I', '-.-.': 'C', '..-.': 'F', '..--': '_', '-.--': 'Y', '-': 'T', '.': 'E',
              '.-.-': ',', '.-..': 'L', '...': 'S', '..-': 'U', '----': '?', '---.': '.', '-.-': 'K', '-..': 'D',
              '.---': 'J', '.--.': 'P', '--': 'M', '-.': 'N', '....': 'H', '...-': 'V'}


length = {',': '4', '.': '4', '?': '4', 'A': '2', 'C': '4', 'B': '4', 'E': '1', 'D': '3', 'G': '3', 'F': '4', 'I': '2',
          'H': '4', 'K': '3', 'J': '4', 'M': '2', 'L': '4', 'O': '3', 'N': '2', 'Q': '4', 'P': '4', 'S': '3', 'R': '3',
          'U': '3', 'T': '1', 'W': '3', 'V': '4', 'Y': '4', 'X': '4', 'Z': '4', '_': '4'}


# Decode message
def morse_to_text(message):
    """
    Convert the text to Morse code without pauses but with a string of numbers to indicate code lengths.
    Reverse the string of numbers.
    Convert the dots and dashes back into the text using the reversed string of numbers as code lengths.

    :param message: message to be decoded
    :return: decoded
    """

    # Convert the text to Morse code without pauses but with a string of numbers to indicate code lengths.
    code = ''.join([morse[letter] for letter in message])
    # Reverse the string of numbers.
    code_length = ''.join([length[letter] for letter in message])[::-1]

    converted = []

    # Put spaces back in the message
    for n in code_length:

        cut = code[:int(n)]
        converted.append(cut)
        code = code[int(n):]

    # Convert the dots and dashes back into the text using the reversed string of numbers as code lengths.
    decoded = ''

    for i in converted:

        if i in morse_flip.keys():
            decoded += morse_flip[i]

    return decoded


# Decode every message and store it in a list
decoded_messages = [morse_to_text(message) for message in messages]

# For each message in the input, output the decoded message on one line
for message in decoded_messages:
    print message

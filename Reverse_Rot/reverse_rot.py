
# -*- coding:utf-8 -*-

# SOLUTION
import sys

# Read data
data = []
for line in sys.stdin:
    data.append(line.split())

# Reverse strings and add them to a list
rotation = [int(l[0]) for l in data[:-1]]
reversed_msg = [l[1][::-1] for l in data[:-1]]
reversed_data = zip(rotation, reversed_msg)

# Create original and reversed original(reverse key, val) dictionary's
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ_.')
original = {k: v for v, k in enumerate(alphabet)}
original_reverse = {k: v for v, k in original.items()}


# Create shifted dictionary
def shift_alphabet(shift):

    shifted = {}

    for key, val in original.items():

        if val + shift > 27:
            val = (val + shift) - 28
            shifted[key] = val

        else:
            val += shift
            shifted[key] = val

    return shifted


# Encrypt the message
def encrypt_message(message, shift):

    # shift alphabet
    shifted_alph = shift_alphabet(shift)
    encrypted_message = ''

    for char in message:
        # find char in shifted alphabet and replace with the one at the position in original alphabet
        encrypted_message += original_reverse[shifted_alph[char]]

    return encrypted_message


# Output the “encrypted” message that results after being reversed and then shifted
for case in reversed_data:
    encrypted = encrypt_message(case[1], case[0])
    print encrypted

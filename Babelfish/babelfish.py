
# -*- coding:utf-8 -*-

import sys

# Read data
data = [line.split() for line in sys.stdin]

# Try mapping each foreign word to his english counterpart (two values per list)
# Add exceptions to the message (one or space values per list)
translation = {}
message = []

for l in data:
    try:
        translation[l[1]] = l[0]

    except IndexError:
        message.extend(l)

# Output is the message translated to English, one word per line.
# Foreign words not in the dictionary should be translated as “eh”.
for s in message:
    try:
        print translation[s]
    except KeyError:
        print 'eh'

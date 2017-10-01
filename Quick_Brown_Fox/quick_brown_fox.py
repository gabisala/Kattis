
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    # Append phrase all lowercase
    data.append(line.lower().split('\n'))

# Alphabet lowercase
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# For each input phrase, output “pangram” if it qualifies as a pangram. Otherwise, output the word “missing”
# followed by a space and then the list of letters that didn’t occur in the phrase. The list of missing letters
# should be reported in lower case and should be sorted alphabetically.

for phrase in data[1:]:

    # check if there are unused letters
    is_pangram = [char for char in alphabet if char not in phrase[0]]

    if is_pangram == []:
        print 'pangram'
    else:
        print '{} {}'.format('missing', ''.join(is_pangram))

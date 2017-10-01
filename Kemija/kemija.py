
# -*- coding:utf-8 -*-

import sys

# Read coded sentence
sentence = sys.stdin.readline()

# Declare patterns to partially remove
remove_patterns = ['apa', 'epe', 'ipi', 'opo', 'upu']

# Replace the pattern with the corresponding vowel and output decoded sentence
for patt in remove_patterns:

    if patt in sentence:
        replace_in_sen = sentence.replace(patt, patt[:1])
        sentence = replace_in_sen

print sentence

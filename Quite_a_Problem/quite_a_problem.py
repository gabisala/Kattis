
# -*- coding:utf-8 -*-

import sys
import re

# Create pattern
word = re.compile(r'([pP][rR][oO][bB][lL][eE][mM])')

# For each line of input, print yes if the line contains ‘problem’, and no otherwise. Any capitalization of ‘problem’
# counts as an occurrence.
for line in sys.stdin:
    if re.findall(word, line):
        print 'yes'
    else:
        print 'no'

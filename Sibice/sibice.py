
# -*- coding:utf-8 -*-

import sys
import math

# Read data
data = [map(int, line.split()) for line in sys.stdin]

# Assign variables and compute the box diagonal
box_width = data[0][1]
box_height = data[0][2]
diagonal = int(math.sqrt(box_width ** 2 + box_height ** 2))

# For each match, in the order they were given in the input, output on a separate line “DA” if the match fits in the
# box or “NE” if it does not.
for match in data[1:]:

    if match[0] <= diagonal:
        print 'DA'
    else:
        print 'NE'

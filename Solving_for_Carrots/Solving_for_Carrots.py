
# -*- coding: utf-8 -*-

import sys

# Read data
contest_data = []

for line in sys.stdin:
    contest_data += line.split()

# Output the number of carrots that will be handed out during the contest.
carrots = int(contest_data[1])

print carrots

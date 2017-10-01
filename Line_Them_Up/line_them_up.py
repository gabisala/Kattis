
# -*- coding:utf-8 -*-

import sys

# Read data
team = []

for line in sys.stdin:
    team.extend(line.split())

team = team[1:]

# Sort team in increasing and decreasing order
team_increasing = sorted(team)
team_decreasing = sorted(team)[::-1]

# Output a single word: INCREASING if the list is in increasing alphabetical order, DECREASING if it is in decreasing
# alphabetical order, and otherwise NEITHER.
if team == team_increasing:
    print 'INCREASING'
elif team == team_decreasing:
    print 'DECREASING'
else:
    print 'NEITHER'


# -*- coding:utf-8 -*-

import sys
from collections import Counter

# Read data
data = []

for line in sys.stdin:
    data.append(line.strip('\n'))

# Count votes
results = Counter(data[:-1])

# Find winner and runner-up
winner, winner_votes = results.most_common()[0]
runner_up_votes = results.most_common()[1][1]

# If a candidate obtained a simple or absolute majority of all votes cast (that is, more than any other candidate),
# output the name of this candidate! If no candidate obtained a simple majority, output: “Runoff!”
if winner_votes == runner_up_votes:
    print 'Runoff!'
else:
    print winner

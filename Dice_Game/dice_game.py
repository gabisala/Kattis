
# -*- coding:utf-8 -*-

import sys

# Read data
game = []
for line in sys.stdin:
    game.append(map(int, line.split()))

# Output the name of the player that has higher probability of winning. Output “Tie” if both players
# have same probability of winning.
if sum(game[0]) > sum(game[1]):
    print 'Gunnar'
elif sum(game[0]) < sum(game[1]):
    print 'Emma'
else:
    print 'Tie'

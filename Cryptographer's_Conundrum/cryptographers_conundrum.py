
# -*- coding:utf-8 -*-

import sys

# Read data
data = sys.stdin.readline()
puzzle = data.split()
puzzle = list(puzzle[0])

# Output the number of days needed to change the cipher text to a string containing only Per’s name
days = 0

for char_index in xrange(0, len(puzzle), 3):

    if puzzle[char_index] != 'P':
        puzzle[char_index] = 'P'
        days += 1
    if puzzle[char_index + 1] != 'E':
        puzzle[char_index + 1] = 'E'
        days += 1
    if puzzle[char_index + 2] != 'R':
        puzzle[char_index + 2] = 'R'
        days += 1

print days

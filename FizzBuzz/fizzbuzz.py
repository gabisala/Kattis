
# -*- coding:utf-8 -*-

import sys

# Read data
data = sys.stdin.readline()
division_game = data.split()

# Assign values to x, y, n
x = int(division_game[0])
y = int(division_game[1])
n = int(division_game[2])

# Output game
for num in range(1, n +1):
    if num % x == 0 and num % y == 0:
        print 'FizzBuzz'
    elif num % x == 0:
        print 'Fizz'
    elif num % y == 0:
        print 'Buzz'
    else:
        print num

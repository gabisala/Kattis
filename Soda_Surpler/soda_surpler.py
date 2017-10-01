
# -*- coding:utf-8 -*-

import sys

# Read data
data = map(int, sys.stdin.readline().split())

# Number of empty soda bottles in Tim’s possession at the
# start of the day plus the number of empty soda bottles found during the day
bottles = data[0] + data[1]
price = data[2]


# How many sodas did Tim drink on his extra thirsty day?
drinks = 0
while bottles >= price:
    drinks += bottles / price
    bottles = bottles / price + bottles % price

print drinks

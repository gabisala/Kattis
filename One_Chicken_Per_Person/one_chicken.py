
# -*- coding:utf-8 -*-

import sys

# Read data
data = map(int, sys.stdin.readline().split())

people, chicken = data

# Output message with the ratio(people, chicken)
if people > chicken:
    if people - chicken == 1:
        print 'Dr. Chaz needs 1 more piece of chicken!'
    else:
        print 'Dr. Chaz needs {} more pieces of chicken!'.format(people - chicken)

elif people < chicken:
    if chicken - people == 1:
        print 'Dr. Chaz will have 1 piece of chicken left over!'
    else:
        print 'Dr. Chaz will have {} pieces of chicken left over!'.format(chicken - people)

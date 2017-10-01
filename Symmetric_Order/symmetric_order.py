
# -*- coding:utf-8 -*-

import sys

# Read data
data_str = []
for line in sys.stdin:
    data_str += line.split()

f = open('data', 'r')
data_str = []
for line in f:
    data_str += line.split()

names_sets = []

# Create name sets
while data_str != ['0']:
    cut_set = data_str[1:int(data_str[0]) + 1]

    names_sets.append(cut_set)
    del data_str[0:int(data_str[0]) + 1]

# SET counter
counter = 1

# Arrange every set in proper order and print it
for name_set in names_sets:

    print 'SET {}'.format(counter)

    for i, name in enumerate(name_set):
        if i % 2 == 0:
            print name

    if len(name_set) % 2 != 0:
        name_set = name_set[:-1]

    for i, name in enumerate(reversed(name_set)):
        if i % 2 == 0:
            print name

    counter += 1

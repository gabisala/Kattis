
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

# Transform strings to lower case and append last element
for line in sys.stdin:
    data.append(line.lower().split()[-1])


# Create animals list
animals = []
anim_list = []

for s in data:
    try:
        int(s)
        if anim_list != []:
            animals.append(anim_list)
            anim_list = []
    except ValueError:
        anim_list.append(s)

# Count animals
unique_animals = [sorted(set(l)) for l in animals]
animal_count = []

for i, l in enumerate(unique_animals):
    animal_count_temp = []
    for animal in l:
        name = animal
        count = animals[i].count(animal)
        statistic = (name, count)
        animal_count_temp.append(statistic)

    animal_count.append(animal_count_temp)

# For each test case, output the list number, followed by the animals Dr. Back has in his zoo in lowercase and
# alphabetical order, with each animal followed by one space and the delimiter | and then another space and their count.
for i, l in enumerate(animal_count):
    print 'List {}:'.format(i + 1)
    for animal in l:
        print '{} | {}'.format(animal[0], animal[1])

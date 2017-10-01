
# -*- coding:utf-8 -*-

import sys

# Read data
data = []
for line in sys.stdin:
    data.append(line.split())

students = data[1:]


# For each line of output, print the student’s name, followed by a space, followed by one of the strings eligible,
# ineligible, and coach petitions as appropriate.
for student in students:

    name = student[0]
    post_secondary = int(student[1][0:3])
    born_year = int(student[2][0:3])
    courses = int(student[3])
    status = None

    if post_secondary >= 2010 or born_year >= 1991:
        status = 'eligible'

    elif courses >= 41:
        status = 'ineligible'

    else:
        status = 'coach petitions'

    print '{} {}'.format(name, status)

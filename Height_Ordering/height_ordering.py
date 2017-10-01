
# -*- coding:utf-8 -*-

import sys
from collections import deque

# Read data
data = []

for line in sys.stdin:

    data.append(map(int, line.strip().split()))


def count_back_step(students):
    """
    Calculates the total number of steps taken back during the ordering process for a given class of students.
    :param students: an unordered list of strings, the height (in millimeters) of each student in the class
    :return: int, total number of steps
    """

    # Store ordered heights
    ordered = []

    # Store count
    back_steps = 0

    # Unordered heights
    students = deque(students[1:])

    # While unordered students
    while students:

        # Select student
        student = students.popleft()

        # Find the first person in the line that is taller than him, and stand in front of that person
        for i, s in enumerate(ordered):

            if student < s:

                ordered.insert(i, student)
                back_steps += len(ordered[i+1:])
                break

        # If there is no student that is taller, then he would stand at the end of the line
        else:
            ordered.append(student)

    return back_steps


# For each data set there is one line of output. The single output line consists of the data set number, K,
# followed by a single space followed by total number of steps taken back.
for case in data[1:]:
    print '{} {}'.format(case[0], count_back_step(case))

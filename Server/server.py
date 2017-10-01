
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(map(int, line.split()))

# Maximum time and minutes for each task in order
time = data[0][1]
tasks = data[1]

# Compute completed tasks and task processing time
completed = 0
processing = 0

for t in tasks:

    processing += t

    if processing > time:
        break
    else:
        completed += 1

# Display the number of tasks that can be completed in T minutes on a first-come, first-served basis
print completed

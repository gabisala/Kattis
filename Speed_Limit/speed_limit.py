
# -*- coding:utf-8 -*-

import sys

# Read data
trip_log = []
for line in sys.stdin:
    trip_log += line.split()

log_entries = int(trip_log[0])

# Compute the total distance driven
while int(trip_log[0]) != -1:

    log_entries = int(trip_log[0])
    log_end = (log_entries * 2) + 1
    data_set = trip_log[1: log_end]

    speed = []
    time = []

    for i in xrange(len(data_set)):
        if i % 2 == 0:
            speed.append(int(data_set[i]))
        else:
            time.append(int(data_set[i]))

    correct_time = []

    while len(time) > 0:

        if len(time) >= 2:
            new_time = time[-1] - time[-2]
            correct_time.append(new_time)
            del time[-1]
        else:
            correct_time.append(time[0])
            break

    correct_time.reverse()
    distance_driven = sum([a * b for a, b in zip(speed, correct_time)])

    # For each input set, print the distance driven, followed by a space, followed by the word “miles”
    print '%d miles' % distance_driven

    trip_log = trip_log[log_end:]

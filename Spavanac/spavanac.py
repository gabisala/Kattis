
# -*- coding:utf-8 -*-

import sys

read_time = sys.stdin.readline()
input_time = read_time.split(' ')
input_hour = int(input_time[0])
input_minutes = int(input_time[1])


def early_alarm(hour, minutes):
    if hour == 0:
        hour = 24

    time_in_minutes = (hour * 60) + minutes
    set_alarm = time_in_minutes - 45
    new_hour = set_alarm / 60
    new_minutes = set_alarm - (new_hour * 60)

    return new_hour, new_minutes


hour, minutes = early_alarm(input_hour, input_minutes)
print hour, minutes

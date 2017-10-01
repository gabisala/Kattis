
# -*- coding:utf-8 -*-

import sys
import datetime

# Read data
data = map(int, sys.stdin.readline().split())

# Construct the day
d = datetime.date(2009, data[1], data[0])

# Find the day of the week, Monday-1 Sunday-7
day_of_the_week = d.isoweekday()

# Index days in a dict
weekdays = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

# Output the day of the week on day D of month M in 2009. The output should be one of the words “Monday”,
# “Tuesday”, “Wednesday”, “Thursday”, “Friday”, “Saturday” or “Sunday”.
print weekdays[day_of_the_week]

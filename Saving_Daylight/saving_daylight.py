
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(line.split())

# Print the month, day, and year as given in the input followed by the amount of time that the sun is above the horizon
# in hours and minutes (always plural).
for day in data:

    # Extract hours and minutes and convert to numbers
    sunrise, sunset = day[-2:]
    sunrise = [int(sunrise[:-3]), int(sunrise[-2:])]
    sunset = [int(sunset[:-3]), int(sunset[-2:])]

    # Compute day time in minutes
    sunrise_in_minutes = sunrise[0] * 60 + sunrise[1]
    sunset_in_minutes = sunset[0] * 60 + sunset[1]
    day_time_in_minues = sunset_in_minutes - sunrise_in_minutes

    # Convert back from minutes to hour: minutes
    day_time_hours = day_time_in_minues / 60
    day_time_minutes = day_time_in_minues % 60

    # Output
    print '{} {} hours {} minutes'.format(' '.join(day[:3]), day_time_hours, day_time_minutes)

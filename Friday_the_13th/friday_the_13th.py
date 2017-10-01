
# -*- coding:utf-8 -*-

import sys

# Read data
data = [map(int, line.split()) for line in sys.stdin]


def gen_days_name():
    """
    Generate days name Sunday to Saturday
    :return: day name
    """

    days_name = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']

    for n in days_name:
        yield n


def create_calendar(year):
    """
    Create Htrae calendar after specifications
    :param year: Htrae year
    :return: Htrae calendar
    """

    # Generate days name
    days_generator = gen_days_name()

    calendar = []

    # Create month by month
    for month in year:

        # Expand days of the month
        month = xrange(1, month + 1)

        # Create date(day number + day name)
        for day in month:
            try:
                date = str(day) + next(days_generator)
                if date == '13Fr':
                    calendar.append(date)

            # Restart if the generator is consumed
            except StopIteration:
                days_generator = gen_days_name()
                date = str(day) + next(days_generator)
                if date == '13Fr':
                    calendar.append(date)

    return calendar

# For each test case, output the number of Friday the 13ths in the specified year.
for year in data[::2][1:]:
    print len(create_calendar(year))

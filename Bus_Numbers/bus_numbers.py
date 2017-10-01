
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(map(int, line.split()))

# Bus numbers in sorted order(small to big)
buses = sorted(data[1])

# Create arranged numbers representation
arranged = []

for i, b in enumerate(buses):

    # Add the first bus number to the list as a string
    if i == 0:
        arranged.append(str(b))

    # For the rest of the numbers
    else:

        try:
            # If the bus number is equal to the previous number + 1 and equal to next number - 1 they are consecutive
            # so add '-' instead of the number
            if b == buses[i - 1] + 1 and b == buses[i + 1] - 1:

                # If the previous number was also consecutive don't add another '-', otherwise add it
                if arranged[-1] != '-':
                    arranged.append('-')

            # Otherwise add the bus number as a string
            else:
                arranged.append(str(b))

        # If the last bus in the list
        except IndexError:
            arranged.append(str(b))


# Create a string from all the bus numbers and '-'
representation = ' '.join(arranged)

# Clean representation
# Print the shortest representation of the list of bus numbers. Use the format as in the example, separate numbers
# with single spaces and output them in sorted order.
print representation.replace(' - ', '-')

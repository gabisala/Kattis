
import sys

# Read data
data = [line.split() for line in sys.stdin]

# Rearrange values, and assign to A, B, C
a, b, c = sorted(map(int, data[0]))

# Output A, B and C in the desired order on a single line, separated by single spaces
for letter in data[1][0]:

    if letter == 'A':
        print a,
    elif letter == 'B':
        print b,
    else:
        print c,

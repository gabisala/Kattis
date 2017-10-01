
# -*- coding:utf-8 -*-

import sys

# Read data
point = [int(line.strip()) for line in sys.stdin]

# Check if strings represent positive or negative numbers
# Output the quadrant number (1, 2, 3 or 4) for the point (x,y)
if point[0] > 0 and point[1] > 0:
    print 1

elif point[0] < 0 and point[1] > 0:
    print 2

elif point[0] < 0 and point[1] < 0:
    print 3

else:
    print 4

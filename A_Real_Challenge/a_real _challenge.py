
import math
import sys

# Read data
area = map(int, sys.stdin.readline().split())

# Output the total length of fence needed for the pasture, in meters. The length should be accurate to an absolute
print 4 * math.sqrt(area[0])

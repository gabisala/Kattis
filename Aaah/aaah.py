
import sys

# Read data
data = []

for line in sys.stdin:
    data += line.split()

# Output 'go' if Marius can go to that doctor, 'no otherwise'
if len(data[0]) == len(data[1]):
    print 'go'
elif len(data[0][:-1]) < len(data[1][:-1]):
    print 'no'
else:
    print 'go'


# -*- coding:utf-8 -*-

import sys

# Read data
data = []
for line in sys.stdin:
    data.append(line.split())


# For each line that begins with precisely “Simon says”, output the rest of the line. Each line that does not begin
# with precisely “Simon says” should be ignored.
for command in data[1:]:

    if command[0] == 'Simon' and command[1] == 'says':
        print ' '.join(command[2:])

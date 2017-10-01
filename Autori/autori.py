
# -*- coding:utf-8 -*-

import sys

# Read data
name = sys.stdin.readline().strip()

# Add to list if letter is uppercase
short_name = [char for char in name if 65 <= ord(char) <= 90]

# The first and only line of output should contain the appropriate short variation.
print ''.join(short_name)

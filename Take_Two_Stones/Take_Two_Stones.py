
# -*- coding: utf-8 -*-

import sys

# Read data
stones_num = int(raw_input())

# Output the winner, “Alice” or “Bob” (without the quotes), on a line
if stones_num % 2 == 0:
    print 'Bob'
else:
    print 'Alice'
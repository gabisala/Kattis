
# -*- coding:utf-8 -*-

import sys

# Read data
# Output the maximum number of bishops that can be placed on i-th chessboard without threatening each other.
for board in sys.stdin:
    size = int(board)

    if size == 1:
        print size

    else:
        print (size * 2) - 2

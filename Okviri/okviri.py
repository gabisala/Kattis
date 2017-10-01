
# -*- coding:utf-8 -*-

import sys

# Read data
letters = sys.stdin.readline().strip()

# Frame lines
line_1 = ''
line_2 = ''
line_3 = ''
line_4 = ''
line_5 = ''

wendy_frame = False

# Create frames for every letter
for n, l in enumerate(letters):

    # Every third letter
    if (n + 1) % 3 == 0:

        wendy_frame = True

        line_1 = line_1[:-1] + '..*..'
        line_2 = line_2[:-1] + '.*.*.'
        line_3 = line_3[:-1] + '*.' + l + '.*'
        line_4 = line_4[:-1] + '.*.*.'
        line_5 = line_5[:-1] + '..*..'

    else:
        # If first letter
        if n == 0:

            line_1 += '..#..'
            line_2 += '.#.#.'
            line_3 += '#.' + l + '.#'
            line_4 += '.#.#.'
            line_5 += '..#..'

        else:
            # If previous frame was a Wendy frame don't add first column
            if wendy_frame is True:

                line_1 += '.#..'
                line_2 += '#.#.'
                line_3 += '.' + l + '.#'
                line_4 += '#.#.'
                line_5 += '.#..'

                wendy_frame = False

            else:

                line_1 = line_1[:-1] + '..#..'
                line_2 = line_2[:-1] + '.#.#.'
                line_3 = line_3[:-1] + '#.' + l + '.#'
                line_4 = line_4[:-1] + '.#.#.'
                line_5 = line_5[:-1] + '..#..'

# All frames
frame = [line_1, line_2, line_3, line_4, line_5]

# Output the word written using Peter Pan and Wendy frames on 5 lines.
for line in frame:
    print line

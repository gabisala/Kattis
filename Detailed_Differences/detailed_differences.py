
# -*- coding:utf-8 -*-

import sys

# Read data
strings = []
for line in sys.stdin:
    strings += line.split()

# Output the two input strings on two lines, and then identify the differences on the line below
# Loop from index 1
i = 1

while i < len(strings) - 1:

    a_string = list(strings[i])
    b_string = list(strings[i + 1])

    # Identify those characters which differ between the two given strings in a visually striking way
    def detailed_dif(a_string, b_string):

        # Compare this two from the strings list
        pairs_of_strings = [char_a == char_b for char_a, char_b in zip(a_string, b_string)]

        output_pattern = ''

        # Compute difference pattern
        for elem in pairs_of_strings:

            if elem is False:
                output_pattern += '*'
            else:
                output_pattern += '.'

        return output_pattern

    # Output the two lines in the order they appear in the input
    print strings[i]
    print strings[i + 1]

    # Output a third line indicating similarities and differences
    output_pattern = detailed_dif(a_string, b_string)
    print output_pattern

    print ''

    # next test case
    i += 2

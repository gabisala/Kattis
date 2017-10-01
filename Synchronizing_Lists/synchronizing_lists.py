
# -*- coding:utf-8 -*-

import sys

# Read data
data = []
for line in sys.stdin:
    data += map(int, line.split())


# Select the test cases
def cut_test_cases(a_list):
    raw_data = a_list[:]
    processed_data = []

    while raw_data != [0]:
        start = 1
        finish = (raw_data[0] * 2) + 1
        processed_data.append(raw_data[start: finish])
        raw_data = raw_data[finish:]

    return processed_data


processe_data = cut_test_cases(data)


# Rearrange wrong list
def rearrange(fixed_order, wrong_order):

    sorted_vals = zip(sorted(fixed_order), sorted(wrong_order))
    corect_order = []

    for i in fixed_order:
        for j in sorted_vals:
            if i == j[0]:
                corect_order.append(j[1])
                break

    return corect_order


# Synchronize positions in list
def synchronize(a_list):

    corrected_order = []

    for l in a_list:

        fixed_order = l[:len(l) / 2]
        wrong_order = l[len(l) / 2:]

        rearranged = rearrange(fixed_order, wrong_order)
        corrected_order.append(rearranged)

    return corrected_order


synchronized = synchronize(processe_data)

# For each test case, print out the second list so that it has the same ordering as the first list. Print a blank
# line between lists.
for l in synchronized:
    for i in l:
        print i
    print ''

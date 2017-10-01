
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.append(map(int, line.split()))


# Single out whoever came alone
def single_guest(guest_list):

    for guest in guest_list:

        if guest_list.count(guest) == 1:
            return guest

# For each test case, output one line containing “Case #x: ” followed by the number C of the guest who is alone
for i, test in enumerate(data[2::2]):
    single = single_guest(test)
    print 'Case #{}: {}'.format(i+1, single)

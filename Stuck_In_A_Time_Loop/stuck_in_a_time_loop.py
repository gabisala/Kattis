
# -*- coding:utf-8 -*-

import sys

# Read data
magic_num = int(sys.stdin.readline())

# Output the entire wizard’s spell by counting from 11 to NN, giving one number and “Abracadabra” per line
for num in range(1, magic_num + 1):
    print num, 'Abracadabra'
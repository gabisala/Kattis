
# -*- coding:utf-8 -*-

import sys
import random

# Read data
dwarves = []

for line in sys.stdin:
    dwarves += map(int, line.split())

# Pick seven random dwarves and if their hat numbers add to 100 break
while True:
    seven_dwarves = random.sample(dwarves, 7)
    if sum(seven_dwarves) == 100:
        break

# Output the numbers in the same order they are given in the input
for dwarve in dwarves:
    if dwarve in seven_dwarves:
        print dwarve

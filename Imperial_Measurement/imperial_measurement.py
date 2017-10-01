
# -*- coding:utf-8 -*-

import sys

# Read data
data = sys.stdin.readline().split()

# All units amount have bean calculated in thou(the smallest amount)
unit_conversion = {

    'thou': 1, 'th': 1,
    'inch': 1000, 'in': 1000,
    'foot': 12000, 'ft': 12000,
    'yard': 36000, 'yd': 36000,
    'chain': 792000, 'ch': 792000,
    'furlong': 7920000, 'fur': 7920000,
    'mile': 63360000, 'mi': 63360000,
    'league': 190080000, 'lea': 190080000

}

# Variables
distance = float(data[0])
from_unit = data[1]
to_unit = data[3]

# Output the distance converted into ũ
converted = distance * unit_conversion[from_unit] / unit_conversion[to_unit]
print converted

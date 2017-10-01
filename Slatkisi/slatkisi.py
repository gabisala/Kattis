
# -*- coding:utf-8 -*-

import sys
import math


def pay_amount(price, smallest_bill):
    """
    Compute the amount Mirko can pay
    :param price: float, price for candy
    :param smallest_bill: integer
    :return: integer, the amount to pay
    """

    # Round down and up the amount to pay
    down = math.floor(price / smallest_bill) * smallest_bill
    up = math.ceil(price / smallest_bill) * smallest_bill

    # Rounds amount to the nearest number he can pay
    if price - down < up - price:
        return int(down)

    else:
        return int(up)


# Process data
data = map(float, sys.stdin.readline().split())

# Price of candy
price = data[0]

# Number of zeros on the smallest bill
num_zeros = data[1]
smallest_bill = 10 ** num_zeros

print pay_amount(price, smallest_bill)

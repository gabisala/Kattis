
# -*- coding:utf-8 -*-

import sys

# Read data
string = sys.stdin.readline().split()
email = string[0]

# Calculate length of the string
length_string = len(string[0])

# ASCII codes between 33 and 126
# Counters
whitespace = 0
uppercase = 0
lowercase = 0
symbols = 0

# Add letters by ASCII code
for c in email:

    if ord(c) == 95:
        whitespace += 1

    elif 97 <= ord(c) <= 122:
        lowercase += 1

    elif 65 <= ord(c) <= 90:
        uppercase += 1

    else:
        symbols += 1

# Compute ratios
whitespace_ratio = float(whitespace) / length_string
lowercase_ratio = float(lowercase) / length_string
uppercase_ratio = float(uppercase) / length_string
symbols_ratio = float(symbols) / length_string

# Output four lines, containing the ratios of whitespace characters, lowercase letters, uppercase letters,
# and symbols (in that order). Your answer should have an absolute or relative error of at most 10 ** −6.
print whitespace_ratio
print lowercase_ratio
print uppercase_ratio
print symbols_ratio

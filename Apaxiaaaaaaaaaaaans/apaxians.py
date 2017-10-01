
import sys

# Read data
name = sys.stdin.readline()

# Translate name
translate = ['0']

for char in list(name):

    if char != translate[-1]:
        translate += char

print ''.join(translate)[1:]


import sys

# Read data
data = []

for line in sys.stdin:
    data += map(int, line.split())

# Assign variables
data_plan = data[0]
spent = data[2:]

# Compute how many megabytes Pero will have available in the N+1 month of using the plan
available_mega = data_plan

for month_amount in spent:
    available_mega += data_plan - month_amount

print available_mega

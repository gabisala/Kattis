
import sys

# Read data
data = []

for line in sys.stdin:
    data.extend(map(int, line.split()))


# Sort books from most expensive to cheapest
price_sorted = sorted(data[1:], reverse=True)

# Group books in groups of three
grouped = [price_sorted[n:n+3] for n in range(0, len(price_sorted), 3)]

# Minimal price for books after discount
minimal_price = 0

# Compute minimal price
for group in grouped:

    # If group of three
    if len(group) == 3:

        # Add to the price the first two books and give the last for free(cheapest one)
        minimal_price += sum(group[:2])

    # Otherwise
    else:

        # Add the price of the book/books to the bill
        minimal_price += sum(group)

# Output minimal price
print minimal_price

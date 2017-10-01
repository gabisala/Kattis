
# -*- coding:utf-8 -*-

import sys

# Read data
data = []
for line in sys.stdin:
    data += line.split()

# Extract rows
rows_words = data[2:]

# Extract columns
num_columns = int(data[1])
columns_words = ['' for s in xrange(num_columns)]
for row in rows_words:
    for i, column in enumerate(row):
        columns_words[i] += column

# Extract words from rows
all_row_words = '#'.join(rows_words)
legal_row_words = all_row_words.split('#')

# Extract words from columns
all_column_words = '#'.join(columns_words)
legal_column_words = all_column_words.split('#')

# All words
words = legal_row_words + legal_column_words

# All words with minimum two characters
legal_words = []
for word in words:
    if len(word) >= 2:
        legal_words.append(word)

# Output the lexicographically smallest word in the crossword.
print min(legal_words)

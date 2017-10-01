
# -*- coding:utf-8 -*-

import sys

# Read data
data = []
for line in sys.stdin:
    data += line.split()

# Assign multiplier values
scanner_row = int(data[2])
scanner_column = int(data[3])

# Assign article
article = data[4:]


# Multiply rows in an article
def multiply_row(article, multiplier):

    multiply_rows = []

    for row in article:
        multiply_rows += [row] * multiplier

    return multiply_rows


# Multiply columns in an article
def multiply_column(article, multiplier):

    multiply_columns = []
    multiply_char = ''

    for row in article:

        for char in row:
            multiply_char += char * multiplier

        multiply_columns.append(multiply_char)
        multiply_char = ''

    return multiply_columns


# Compute the characters matrix article enlargement
def enlarge_article(article):

    enlarged_article = []

    # Multiply rows and columns in an article
    if scanner_row > 1 and scanner_column > 1:
        multiplied_row = multiply_row(article, scanner_row)
        enlarged_article += multiplied_row

        # Continue mutating article list and reset the enlarged one
        article = enlarged_article
        enlarged_article = []

        multiplied_column = multiply_column(article, scanner_column)
        enlarged_article += multiplied_column

        return enlarged_article

    # Multiply rows in an article
    elif scanner_row > 1:
        multiplied_row = multiply_row(article, scanner_row)
        enlarged_article += multiplied_row

        return enlarged_article

    # Multiply columns in an article
    elif scanner_column > 1:
        multiplied_column = multiply_column(article, scanner_column)
        enlarged_article += multiplied_column

        return enlarged_article

    # If no change
    else:
        return article


characters_matrix = enlarge_article(article)
# Output characters matrix
for row in characters_matrix:
    print row

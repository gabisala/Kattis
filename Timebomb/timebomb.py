
# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.extend(line.split('\n'))


def clean_and_fix(data):
    """
    Remove empty strings ang fix number 6 display
    :param data: raw data
    :return: list, clean and fixed data
    """

    # Clean by removing '' empty strings
    clean_data = [s for s in data if s != '']

    # Fix number 6 as last digit problem by adding two spaces
    fix_data = []

    for row in clean_data:

        # If row repr has a length smaller than other rows, add two '--' and than
        # replace all spaces with '-'
        if len(row) < len(clean_data[0]):
            row += '--'
            fix = row.replace(' ', '-')
            fix_data.append(fix)
        else:
            fix = row.replace(' ', '-')
            fix_data.append(fix)

    return fix_data


fixed_data = clean_and_fix(data)


def create_ascii_rep(fixed_data):
    """
    Create the ascii representation of the data
    :param fixed_data: list, fix and clean data
    :return: list, ascii digits
    """

    # Add all digits rows
    digits_rows = []

    for line in fixed_data:

        # Cut digit row
        start = 0
        finish = 3

        # Add row by row
        digits_cut = []

        while finish < len(line) + 1:
            cut = line[start: finish]
            digits_cut.append(cut)
            start += 4
            finish += 4

        digits_rows.append(digits_cut)

    # Find how many digits in fixed_data by the rows number
    rows = (len(fixed_data[0]) + 1) / 4

    # Arrange digits
    digits_ordered = [l[i] for i in xrange(rows) for l in digits_rows]

    # Create ascii representation
    ascii_rep = [digits_ordered[i:i+5] for i in range(0, len(digits_ordered), 5)]

    return ascii_rep


# Ascii to numbers mapping
digits_representation = {

    "['***', '*-*', '*-*', '*-*', '***']": "0",
    "['--*', '--*', '--*', '--*', '--*']": "1",
    "['***', '--*', '***', '*--', '***']": "2",
    "['***', '--*', '***', '--*', '***']": "3",
    "['*-*', '*-*', '***', '--*', '--*']": "4",
    "['***', '*--', '***', '--*', '***']": "5",
    "['***', '*--', '***', '*-*', '***']": "6",
    "['***', '--*', '--*', '--*', '--*']": "7",
    "['***', '*-*', '***', '*-*', '***']": "8",
    "['***', '*-*', '***', '--*', '***']": "9"

}

ascii_representation = create_ascii_rep(fixed_data)


def ascii_to_number(ascii_representation):
    """
    Converts the ascii representation to a list of digits representing the number
    :param ascii_representation: list, ascii representation
    :return: list of digits, None if no such digit
    """

    # Create number
    number = []

    for line in ascii_representation:

        # Add digit
        if str(line) in digits_representation.keys():
            number.append(digits_representation[str(line)])

        # If incorrect display of digit add None
        else:
            number.append(None)

    return number


number = ascii_to_number(ascii_representation)


def press_the_button(number):
    """
    What happens if you press the button
    :param number: list of digits, None if no such digit
    :return: Print one line with “BEER!!” if it is safe to press the button and defuse the bomb, 
            and “BOOM!!” otherwise
    """

    # If invalid representation for any digit, the bomb will explode
    if None in number:
        return 'BOOM!!'

    else:
        # Convert list to number
        number = int(''.join(number))

        # If number is divisible by 6: It's BEER time!!
        if number % 6 == 0:
            return 'BEER!!'

        # BOOM!!
        else:
            return 'BOOM!!'


print press_the_button(number)

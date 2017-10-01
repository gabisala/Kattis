
# -*- coding:utf-8 -*-

import sys

# Read data
data = sys.stdin.readline().split()


# Assign password and password string
password = list(data[0])
p_string = list(data[1])


def check_password(password, password_string):
    """
    Check if a password is valid or not
    :param password: list, password characters
    :param password_string: list, password string characters
    :return: string, PASS if the second string is a valid message for the password, or FAIL otherwise
    """

    while True:

        # If we pop every char the password is valid
        if not password:
            return 'PASS'

        # If we pop every char the password is false
        elif not password_string:
            return 'FAIL'

        # If the first char in password is the same as the first in password string, remove them
        elif password[0] == password_string[0]:
            password.pop(0)
            password_string.pop(0)

        # If the first char in password is NOT the same as the first in password string,
        # remove first char from password string
        elif password[0] != password_string[0] and password_string[0] not in password:
            password_string.pop(0)

        # If the first char in password is NOT the same as the first in password string,
        # but exists in the password the password is false
        else:
            return 'Fail'

# Output a single line with the word PASS if the second string is a valid message for the password, or FAIL otherwise.
print check_password(password, p_string)

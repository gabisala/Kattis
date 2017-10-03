
# -*- coding:utf-8 -*-

import sys

# Read data
data = [line.strip() for line in sys.stdin]

# The largest absolute difference between the number of women and number of men
absolute_difference = int(data[0])

# A list consisting solely of the characters ’W’ and ’M’ of length at most 100,
# describing the genders of the people in the queue
people_queue = list(data[1])

# Store the difference after every person enters the club, males count, females count
present_difference = 0
males = 0
females = 0

# While the absolute difference wasn't surpass and there are still people in the queue
while absolute_difference >= present_difference and len(people_queue) >= 1:

    # First person in the queue
    person = people_queue[0]

    # If the present difference equals the tolerated absolute difference
    if present_difference == absolute_difference:

        # If there are more males in the club
        if males > females:

            # If the first person is a male
            if person == 'M':

                # Check the second person in the queue
                next_person = people_queue[1]

                # If the person is a male declare that the club is full
                if next_person == 'M':
                    break

                # If the person is a female
                else:
                    # Add her to the female count
                    females += 1
                    # Let her in, remove her from the queue
                    del people_queue[1]

            # If the first person is a female
            else:
                females += 1
                del people_queue[0]

            # Compute the present difference between males and females in the club
            present_difference = abs(females - males)


        # If there are more males in the club
        elif males < females:

            # If the first person is a female
            if person == 'W':

                # Check the second person in the queue
                next_person = people_queue[1]

                # If the person is a female declare that the club is full
                if next_person == 'W':
                    break

                # If the person is a male
                else:
                    # Add him to the male count
                    males += 1
                    # Let him in, remove him from the queue
                    del people_queue[1]

            # If the person is a male
            else:
                males += 1
                del people_queue[0]

            # Compute the present difference between males and females in the club
            present_difference = abs(females - males)


    # If difference wasn't reached
    else:

        # If is a male add him to the male count
        if person == 'M':
            males += 1

        # If is a female add her to the female count
        elif person == 'W':
            females += 1

        # Compute the present difference between males and females in the club
        present_difference = abs(females - males)
        # Remove person from the queue
        del people_queue[0]


# Output the maximum number of people Bruno can let into the club without losing track of his counting.
in_the_club = females + males
print in_the_club


# -*- coding:utf-8 -*-

# Read contest data
import sys

grades = []
for line in sys.stdin:
    grades.append(map(int, line.split()))


# Calculate score for each contestant
def calculate_score(grades):
    contestants_score = []
    for grades_list in grades:
        contestants_score.append(sum(grades_list))
    return contestants_score

score_list = calculate_score(grades)


# Output on a single line the winner’s number and their points
def winner_and_points(score_list):

    winner_points = max(score_list)

    for contestant_number, points in enumerate(score_list):
        if points == winner_points:
            return str(contestant_number + 1) + ' ' + str(points)


the_winner_is = winner_and_points(score_list)
print the_winner_is


# -*- coding:utf-8 -*-

import sys

# Read data
data = []

for line in sys.stdin:
    data.extend(map(int, line.split()))


def count_votes(case):

    # total number of votes
    total_votes = float(sum(case[1:]))
    # print 'total number of votes =', total_votes

    # candidates individual votes
    votes = case[1:]
    # print 'candidates individual votes =', votes

    # candidates individual percentages
    percentage = [(v * 100) / total_votes for v in votes]
    # print 'candidates individual percentages =', percentage

    # winner
    the_winner = max(percentage)

    # how many winners
    number_of_winners = percentage.count(the_winner)
    # print 'number of winners =', number_of_winners

    # if one winner
    if number_of_winners == 1:

        # if majority
        if the_winner > 50:
            return 'majority winner {}'.format(percentage.index(max(percentage)) + 1)

        # if minority
        else:
            return 'minority winner {}'.format(percentage.index(max(percentage)) + 1)

    # if equal percentages
    else:
        return 'no winner'


# Provide a line of output for each test case. If the winner receives more than half of the votes, print the phrase
# majority winner followed by the candidate number of the winner. If the winner does not receive more than half
# of the votes, print the phrase minority winner followed by the candidate number of the winner. If a winner cannot be
# determined because no single candidate has more vote than others, print the phrase no winner. The candidate numbers
# in each case are 1,2,…,n.

all_cases = data[1:]

while all_cases:

    # cut case from data
    cut = all_cases[0] + 1
    case = all_cases[0: cut]

    # output result
    print count_votes(case)

    # prepare new case
    all_cases = all_cases[cut:]

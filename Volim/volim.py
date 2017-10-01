
# -*- coding:utf-8 -*-

import sys

# Read data
contest_log = []
for line in sys.stdin:
    contest_log.append(line.split())

# Variables
box_at_player = int(contest_log[0][0])
questions = contest_log[1]
game = contest_log[2:]
countdown = 210
player = box_at_player

# Create two lists, one for time to answer and one for answers
time_log = [int(t) for turn in game for t in turn[:-1]]
answers_log = [ans for turn in game for ans in turn[-1]]


# Yield answers when needed
def provide_answer(answers_log):
    for ans in answers_log:
        yield ans

gen_answer = provide_answer(answers_log)


# Compute the numbered label of the player who had the box when it finally exploded
while countdown >= 0:

    for i, t in enumerate(time_log):

        answer = gen_answer.next()

        if answer == 'T':
            countdown -= t

            if countdown < 0:
                print player
                break

            if player == 8:
                player = 1

            else:
                player += 1

        elif answer == 'P':
            countdown -= t
            if countdown < 0:
                print player
                break

        elif answer == 'N':
            countdown -= t
            if countdown < 0:
                print player
                break

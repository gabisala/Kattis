
# -*- coding:utf-8 -*-

import sys

# Read data
data = []
for line in sys.stdin:
    data += line.split()


# Answers pattern for each boy
adrian_sequence = ['A', 'B', 'C']
bruno_sequence = ['B', 'A', 'B', 'C']
goran_sequence = ['C', 'C', 'A', 'A', 'B', 'B']


# Input number of questions and answers
questions = int(data[0])
correct_answers = list(data[1])


# Generate answers by sequence and number of questions
def generate_answers(boy_sequence, questions):

    answers = 0
    boy_answers = []

    while answers <= questions:

        if len(boy_answers) == questions:
            break
        elif answers > len(boy_sequence) - 1:
            answers = -1
        else:
            boy_answers += boy_sequence[answers]

        answers += 1

    return boy_answers


# Generate answers for each boy
adrian = generate_answers(adrian_sequence, questions)
bruno = generate_answers(bruno_sequence, questions)
goran = generate_answers(goran_sequence, questions)


# Check answers for correctness
boys_answers = adrian, bruno, goran
check_answer = []

for boy in boys_answers:
    check_answer.append([q == a for q, a in zip(correct_answers, boy)])


# Compute score for each boy
score = []
for result in check_answer:
    score.append(result.count(True))


# Bind boy name to result
boys_names = ['adrian', 'bruno', 'goran']
adrian, bruno, goran = score
boy_result = [(b, s) for b, s in zip(boys_names, score)]


# Best score
max_correct_answers = max(adrian, bruno, goran)


# Output the names of the boys (in alphabetical order) whose sequences result in M correct answers
print max_correct_answers
for boy in boy_result:
    if boy[1] == max_correct_answers:
        print boy[0]

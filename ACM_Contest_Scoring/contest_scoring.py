
import sys

# Read data

log = []
for line in sys.stdin:
    log.append(line.split())

problem_status = {}
score = 0
problems_solved = 0

# Calculate the number of problems solved and final score
for problem in log:

    # Break if at the end of log
    if problem[0] == '-1':
        break

    # Create a dictionary with information about problem trials and penalties
    if problem[1] not in problem_status.keys():
        problem_status[problem[1]] = [False, 0]

    if problem[-1] == 'right' and problem_status[problem[1]][0] is False:
        score += int(problem[0])
        problems_solved += 1

    elif problem[-1] == 'right' and problem_status[problem[1]][0] is True:
        score += int(problem[0]) + problem_status[problem[1]][1]
        problems_solved += 1

    elif problem[-1] == 'wrong' and problem_status[problem[1]][0] is False:
        problem_status[problem[1]][0] = True
        problem_status[problem[1]][1] += 20

    elif problem[-1] == 'wrong' and problem_status[problem[1]][0] is True:
        problem_status[problem[1]][1] += 20


print problems_solved, score

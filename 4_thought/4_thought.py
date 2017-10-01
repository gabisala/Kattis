
import sys
from itertools import combinations_with_replacement as combine
from itertools import permutations


def expression(target_number):
    """
    Given an integer n as input, will produce a mathematical expression whose solution is n
    :param target_number: int, n
    :return: string, the mathematical expression or the string 'no solution'
    """

    # Generate possible operations layouts as strings
    operations = combine('+-/*', 3)

    # For every combination layout
    for combination in operations:

        # Generate every permutation of the current combination
        operations_layouts = permutations(combination)

        # For every permutation layout
        for operation in operations_layouts:

            # Create the mathematical expression
            equation = '4 {} 4 {} 4 {} 4 == {}'.format(operation[0], operation[1], operation[2], target_number)

            # Evaluate the expression
            correct = eval(equation)

            # If true
            if correct:
                return equation.replace('==', '=')

    # Otherwise
    return 'no solution'


# Skip first line of input
next(sys.stdin)

# For every test case
for number in sys.stdin:
    # Remove the new line character
    number = number.strip('\n')

    # Print one line containing either an equation using four 4 to reach the target number or the phrase no solution
    print expression(number)



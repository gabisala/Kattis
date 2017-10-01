
# -*- coding:utf-8 -*-

# https://open.kattis.com/rationalsequence2

# A sequence of positive rational numbers is defined as follows:

# An infinite full binary tree labeled by positive rational numbers is defined by:
# The label of the root is 1/1.
# The left child of label p/q is p/(p+q).
# The right child of label p/q is (p+q)/q.

# The sequence is defined by doing a level order (breadth first) traversal of the tree
# (indicated by the light dashed line). So that:

# F(1)=1/1, F(2)=1/2, F(3)=2/1, F(4)=1/3, F(5)=3/2, F(6)=2/3,…
# F(1)=1/1, F(2)=1/2, F(3)=2/1, F(4)=1/3, F(5)=3/2, F(6)=2/3,…

# Write a program which finds the value of n for which F(n) is p/q for inputs p and q.

# Input
# The first line of input contains a single integer P, (1≤P≤1000), which is the number of data sets that follow.
# Each data set should be processed identically and independently. Each data set consists of a single line of input.
# It contains the data set number, K, a single space, the numerator, p, a forward slash (/) and the denominator, q,
# of the desired fraction.

# Output
# For each data set there is a single line of output. It contains the data set number, K, followed by a single space
# which is then followed by the value of n for which F(n) is p/q. Inputs will be chosen so n will fit in
# a 32-bit integer.


# SKETCH

# Read data
f = open('a_rational_sequence_2_data', 'r')

data = [line.split() for line in f][1:]

print 'data =', data
#
#
root = [(1, 1)]
n = 1
target = (217, 134)
found = False


while found is False:
    new_root = []
    p_q_cache = {}

    for t in root:
        # print 'n =', n

        # print ''
        # print t
        # print 'n =', n

        # If we have cached the value, than return it
        if t in p_q_cache:
            new_root.append(p_q_cache[t])

        else:

            p, q = t
            # print 'p = {}, q = {}'.format(p, q)

            if p != target[0] or q != target[1]:

                left = (p, (p + q))
                n += 1

                if left[0] == target[0] and left[1] == target[1]:
                    print 'hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'

                    print n
                    found = True
                    break

                else:
                    new_root.append(left)

                # print 'left = ', new_root


            if p != target[0] or q != target[1]:

                right = ((p + q), q)
                n += 1

                if right[0] == target[0] and right[1] == target[1]:
                    print 'hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
                    print n
                    found = True
                    break

                else:
                    new_root.append(right)

                # print 'right = ', new_root



            else:
                found = True
                # print 'n =', n
                break

    # print ''
    # print 'cache =', p_q_cache
    p_q_cache[t[::-1]] = [(b, a) for a, b in new_root]
    root = new_root
    # print 'cache =', p_q_cache


# target_found = False
#
# p, q = root
# # left = [p, (p+q)]
# # right = [(p+q), q]
#
# # print 'left =', left
# # print 'right =', right
#
# p_q_cache = {}
#
# def n_value(target):
#     # # If we have cached the value, than return it
#     # if left in p_q_cache:
#     #     return  p_q_cache[left]
#
#     if p != target[0] and q != target[1]:
#
#         left = (p, (p + q))
#         n += 1
#
#     if p != target[0] and q != target[1]:
#         right = ((p + q), q)
#         n += 1
#
#     else:
#         print n
#
#     p_q_cache.update((p, q), (left, right))
#
#
#
#     # Cache the value and return it
#     fibonacci_cache[n] = value
#     return value
#
# for n in range(1, 10):
#     print "{} : {}".format(n, fibonacci(n))
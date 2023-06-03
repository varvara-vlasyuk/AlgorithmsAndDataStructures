"""
Given number N. Find the number of ways to express N as a sum of 1, 3 4.
e.g
N=4 --> {4},{1,3},{3,1},{1,1,1,1} -> 4 ways to express
N=5 --> {4,1},{1,4},{1,1,3},{3,1,1},{1,3,1},{1,1,1,1,1} -> 6 ways
"""

number = 5
# values = [1, 3, 4]


def num_factor(num):
    if num < 0:
        return
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    if num == 3:
        return 2
    if num == 4:
        return 4
    else:
        res1 = num_factor(num - 1)
        res2 = num_factor(num - 4)
        res3 = num_factor(num - 3)
        return res1 + res2 + res3


print(num_factor(number))



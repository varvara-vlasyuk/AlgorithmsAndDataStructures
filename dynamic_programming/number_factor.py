"""
Given number N. Find the number of ways to express N as a sum of 1, 3 4.
e.g
N=4 --> {4},{1,3},{3,1},{1,1,1,1} -> 4 ways to express
N=5 --> {4,1},{1,4},{1,1,3},{3,1,1},{1,3,1},{1,1,1,1,1} -> 6 ways
"""


# top-bottom approach
def number_factor(number: int, meta: dict = None) -> int:
    if meta is None:
        meta = {}
    if number == 0:
        return 0
    if number in (1, 2):
        return 1
    if number == 3:
        return 2
    if number == 4:
        return 4

    if number not in meta.keys():
        meta[number] = number_factor(number - 1, meta) +\
                       number_factor(number - 3, meta) +\
                       number_factor(number - 4, meta)
    return meta[number]


print(number_factor(5))

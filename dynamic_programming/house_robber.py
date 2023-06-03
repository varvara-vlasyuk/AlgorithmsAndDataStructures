"""
Given N number of houses along the street and amounts of money available in the houses.
Find the maximum amount that could be stolen assuming that adjacent houses can not be robbed.
E.g.
houses:
/\    /\    /\    /\     /\    /\    /\
H(6), H(7), H(1), H(30), H(8), H(2), H(4)
max amount is 7 + 30 + 4 = 41
"""


# top-down approach
def max_amount_td(houses: list, index: int, meta: dict = None) -> int:
    if meta is None:
        meta = {}
    if index >= len(houses):
        return 0
    if index not in meta.keys():
        skip = max_amount_td(houses, index + 1, meta)
        rob = max_amount_td(houses, index + 2, meta)
        meta[index] = max(skip, rob + houses[index])

    return meta[index]


# bottom-up approach
def max_amount_bu(houses: list):
    meta = [0] * (len(houses) + 2)
    for i in range(len(houses) - 1, -1, -1):
        meta[i] = max(houses[i] + meta[i + 2], meta[i + 1])

    return meta[0]


houses = [6, 7, 1, 30, 8, 2, 4]
print(max_amount_bu(houses))

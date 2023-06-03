"""
Given 2D matrix. Each cell represents the cost for accessing it.
Implement the method to calculate the number of ways to reach (n-1,n-1) cell starting from (0,0) with a given cost
assuming that you only allowed to move down or right.
"""

matrix = [[4, 7, 1, 6],
          [5, 7, 3, 9],
          [3, 2, 1, 2],
          [7, 1, 6, 3],
          ]


# we will start from the end to decrease the number of arguments
def min_path_cost(mtx: list, ind1: int, ind2: int, curr_cost: float, target_cost: float):
    if ind1 == 0 and ind2 == 0:
        return 1 if curr_cost + mtx[ind1][ind2] == target_cost else 0
    if ind1 == -1 or ind2 == -1:
        return 0

    curr_cost += mtx[ind1][ind2]
    left = min_path_cost(mtx, ind1, ind2 - 1, curr_cost, target_cost)
    up = min_path_cost(mtx, ind1 - 1, ind2, curr_cost, target_cost)
    return left + up


print(min_path_cost(matrix, len(matrix) - 1, len(matrix) - 1, 0, 25))

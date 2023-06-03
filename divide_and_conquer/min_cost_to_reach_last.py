"""
Given 2D matrix. Each cell represents the cost for accessing it.
Implement the method to reach (n-1,n-1) cell starting from (0,0) with a minimum cost
assuming that you only allowed to move down or right.
"""

matrix = [[4, 7, 8, 6, 4],
          [6, 7, 3, 9, 2],
          [3, 8, 1, 2, 4],
          [7, 1, 7, 3, 7],
          [2, 9, 8, 9, 3]
          ]


def min_path_cost(mtx: list, ind1: int, ind2: int, rnum: int, cnum: int):
    if ind1 == rnum and ind2 == cnum:
        return mtx[ind1][ind2]
    if ind1 > rnum or ind2 > cnum:
        return float("inf")

    right = min_path_cost(mtx, ind1, ind2 + 1, rnum, cnum)
    down = min_path_cost(mtx, ind1 + 1, ind2, rnum, cnum)
    return mtx[ind1][ind2] + min(right, down)


print(min_path_cost(matrix, 0, 0, len(matrix) - 1, len(matrix[0]) - 1))

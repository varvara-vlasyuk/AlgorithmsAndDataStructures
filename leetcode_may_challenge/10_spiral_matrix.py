"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
E.g.: n=3
1 2 3
8 9 4
7 6 5
"""
from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    result = []
    for i in range(0, n):
        result.append(n*[0])
    cur_size = n
    cur_num = 1
    for start in range(0, int(n/2) + 1):
        # right
        for j in range(start, cur_size):
            result[start][j] = cur_num
            cur_num += 1

        # down
        for i in range(start+1, cur_size):
            result[i][cur_size - 1] = cur_num
            cur_num += 1

        # left
        for j in range(cur_size - 2, start-1, -1):
            result[cur_size - 1][j] = cur_num
            cur_num += 1

        # up
        for i in range(cur_size - 2, start, -1):
            result[i][start] = cur_num
            cur_num += 1

        cur_size -= 1

    return result



print(generateMatrix(6))
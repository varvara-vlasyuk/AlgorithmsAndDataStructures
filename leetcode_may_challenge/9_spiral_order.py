from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    n = len(matrix)
    m = len(matrix[0])
    right = m
    bottom = n
    left = 0
    top = 1
    for start in range(0, int(n/2) + 1):
        # right
        for j in range(start, right):
            result.append(matrix[start][j])

        # down
        for i in range(start + 1, bottom):
            result.append(matrix[i][right - 1])

        # left
        for j in range(right - 2, left, -1):
            result.append(matrix[bottom - 1][j])

        # up
        for i in range(bottom - 2, start, -1):
            result.append(matrix[i][left])

        right -= 1
        bottom -= 1
        left += 1
        top += 1

    return result


# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))

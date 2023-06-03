"""
- Divide an array into two parts
- Find the right place in the sorted(left) part for the first element from the unsorted(right) part
- Repeat until unsorted part is empty
"""
from typing import List


def insertion_sort(arr: list) -> List:
    for i in range(1, len(arr)):
        ind = i
        for j in range(i - 1, -1, -1):
            if arr[ind] < arr[j]:
                arr[ind], arr[j] = arr[j], arr[ind]
                ind = j
            else:
                break

    return arr


# lst = [1, 8, 7, 9, 4, 2, 5, 6]
# print(insertion_sort(lst))

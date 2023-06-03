"""
on each iteration we find minimum in the right part of array and swap first element with min in the unsorted part
E.g.: iteration 3 -> 1,2,5,7,3,6. 1,2 is sorted part, 5,7,3,6 is unsorted part. On this iteration we will swap 5 and 3
"""
from typing import List


def selection_sort(arr: list) -> List:
    for i in range(0, len(arr)):
        ind_min = i
        for j in range(i, len(arr)):
            if arr[ind_min] > arr[j]:
                ind_min = j

        arr[i], arr[ind_min] = arr[ind_min], arr[i]

    return arr


# lst = [4, 5, 6, 2, 3, 6, 7, 10]
# print(selection_sort(lst))

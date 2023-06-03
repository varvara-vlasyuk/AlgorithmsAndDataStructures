"""
- Divide the array in halves until reach 1 element in each
- Merge halves sorting them -> 3,6 and 2,4 will become 2,3,4,6
"""
from typing import List


def merge(arr: list, left, middle, right) -> List:
    merged = []
    i = left
    j = middle + 1
    while i <= middle and j <= right:
        if arr[i] < arr[j]:
            merged.append(arr[i])
            i += 1
        else:
            merged.append(arr[j])
            j += 1

    if i <= middle:
        merged.extend(arr[i:middle+1])
        s = arr[i:middle]
    if j <= right:
        merged.extend(arr[j:right+1])
        s = arr[j:right]

    return merged


def merge_sort(arr: list) -> List:
    part_size = 1
    target_arr = arr
    temp_arr = []
    while part_size < len(arr):
        temp_arr = target_arr
        target_arr = []
        for left in range(0, len(temp_arr), part_size * 2):
            middle = left + part_size - 1
            right = left + part_size * 2 - 1
            target_arr.extend(merge(temp_arr, left, middle, right))
            print(target_arr)

        part_size *= 2

    return target_arr


lst = [3, 2, 5, 9, 11, 15, 1, 10]
print(merge_sort(lst))

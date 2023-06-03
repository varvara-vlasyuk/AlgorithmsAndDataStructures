from typing import List


def bubble_sort(arr: list) -> List:
    arr_len = len(arr)
    for i in range(0, arr_len):
        for j in range(i, arr_len):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


lst = [3, 1, 5, 9, 6, 2]
print(bubble_sort(lst))

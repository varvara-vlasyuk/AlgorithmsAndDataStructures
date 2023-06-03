"""
1. Set up an array of empty buckets.
2. Iterate through the input array, assigning each element to the appropriate bucket based on its value.
3. Sort each individual bucket using another sorting algorithm or by recursively applying bucket sort.
4. Concatenate the sorted buckets to produce the final sorted array.
"""
import math
from selection_sort import selection_sort


def bucket_sort(arr: list) -> list:
    # using values range to find the most suitable number of buckets
    num_of_buckets = round(math.sqrt(len(arr)))
    buckets = [[] for _ in range(num_of_buckets)]
    max_value = max(arr)
    for value in arr:
        b_num = math.ceil(value * num_of_buckets / max_value)
        buckets[b_num-1].append(value)

    target_arr = []
    for bucket in buckets:
        target_arr.extend(selection_sort(bucket))

    return target_arr


lst = [8, 4, 80, 56, 22, 13, 5, 2, 30, 45]
print(bucket_sort(lst))

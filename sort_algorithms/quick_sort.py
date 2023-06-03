"""
3 5 0 6 2 1 4
p s i
3 0 5 6 2 1 4
p   s   i
3 0 2 6 5 1 4
p     s   i
3 0 2 1 5 6 4
p     s     i

1 2 0     5 6 4
p i       p i
0 2 1     5 6 4
p   i     p   i
0 1 2     5 6 4
p   i     p   i
"""
from typing import List

import queue


def pivot(in_list: list, pv: int, end: int):
    swap = pv
    for i in range(pv + 1, end + 1):
        if in_list[pv] > in_list[i]:
            swap += 1
            in_list[swap], in_list[i] = in_list[i], in_list[swap]
    in_list[pv], in_list[swap] = in_list[swap], in_list[pv]
    return swap


def quick_sort(in_list: list, left: int, right: int):
    print(f'{left}, {right}')
    pv = pivot(in_list, left, right)
    print(in_list)
    if left < pv - 1:
        quick_sort(in_list, left, pv - 1)
    if pv + 1 < right:
        quick_sort(in_list, pv + 1, right)


def quick_sort_it(in_list: list):
    q = queue.Queue()
    q.put((0, len(in_list) - 1))
    while not q.empty():
        left, right = q.get()
        pv = pivot(in_list, left, right)
        if left < pv - 1:
            q.put((left, pv - 1))
        if pv + 1 < right:
            q.put((pv + 1, right))


lst = [3, 5, 2, 6, 1, 0, 4, 8]
quick_sort_it(lst)
print(lst)

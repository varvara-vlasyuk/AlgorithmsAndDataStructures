"""
- insert into binary heap tree
- extract from binary heap tree
"""
from typing import List, Tuple, Any


class BinaryHeap:
    def __init__(self):
        self.list = [None]
        self.size = 0

    def _balance_up(self):
        node_index = self.size
        while node_index > 1:
            parent_index = int(node_index / 2)
            if self.list[node_index] < self.list[parent_index]:
                self.list[node_index], self.list[parent_index] = self.list[parent_index], self.list[node_index]
                node_index = parent_index
            else:
                break

    def _balance_down(self):
        index = 1
        while (index * 2) <= self.size:
            left_index = index * 2
            right_index = left_index + 1

            if right_index <= self.size and self.list[left_index] > self.list[right_index]:
                swap = right_index
            else:
                swap = left_index

            if self.list[swap] > self.list[index]:
                break
            else:
                temp = self.list[swap]
                self.list[swap] = self.list[index]
                self.list[index] = temp

                index = swap

    def add_value(self, value):
        self.list.append(value)
        self.size += 1
        self._balance_up()

    def extract(self):
        elem = self.list[1]
        self.list[1] = self.list[self.size]
        self.list[self.size] = None
        self.size -= 1
        self._balance_down()
        return elem

    def is_empty(self):
        return True if self.size == 0 else False


def heap_sort(in_list: list) -> List:
    heap = BinaryHeap()
    for elem in in_list:
        heap.add_value(elem)
    print(heap.list)
    in_list.clear()
    while not heap.is_empty():
        in_list.append(heap.extract())
        print(heap.list)

    return in_list


def get_min_child(in_list: list, ind1: int, ind2: int, size: int) -> Tuple[Any, int]:
    if ind1 < size and ind2 < size:
        return (in_list[ind1], ind1) if in_list[ind1] < in_list[ind2] else (in_list[ind2], ind2)
    else:
        return (in_list[ind2], ind2) if ind2 < size else (in_list[ind1], ind1)


def heapify(in_list: list, index: int, size: int):
    while ((index + 1) * 2 - 1) < size:
        left = (index + 1) * 2 - 1
        right = (index + 1) * 2
        min_child_val, min_child_ind = get_min_child(in_list, left, right, size)
        if in_list[index] > min_child_val:
            in_list[index], in_list[min_child_ind] = in_list[min_child_ind], in_list[index]
            index = min_child_ind
        else:
            break


def heap_sort_one_array(in_list: list):
    for i in range(int(len(in_list) / 2) - 1, -1, -1):
        heapify(in_list, i, len(in_list))
        print(i)
        print(in_list)
    print("back")
    for i in range(len(in_list)-1, 0, -1):
        in_list[i], in_list[0] = in_list[0], in_list[i]
        print(in_list)
        heapify(in_list, 0, i)
        print(i)
        print(in_list)
    return in_list


lst = [8, 2, 4, 15, 6, 11, 12, 9, 23, 14, 1]
print(heap_sort_one_array(lst))     # result [23, 15, 14, 12, 11, 9, 8, 6, 4, 2, 1]

"""
Binary Heap is a Binary Tree with following properties:
- Complete Tree: It is a complete binary tree.
That is, all levels of the tree are fully filled except for the last level, which is filled from left to right.
- Heap Property: Either every parent node is less than or equal to its child node
according to a comparison function defined for the heap (this property makes it a Min Heap)
or every parent node is greater than or equal to its child node (this property makes it a Max Heap).

Min heap
     10
   /   \
 20     100
/  \    /
30  40 200

Max heap
    200
  /   \
100   150
/  \  /
50 70 80

"""


from enum import Enum


class HeapType(Enum):
    MAX = 0
    MIN = 1


class BinaryHeap:
    def __init__(self, size: int, heap_type: HeapType):
        self.list = [None] * (size + 1)
        self.size = 0
        self.max_size = size + 1
        self.type = heap_type

    # def get_size(self):
    #     return self.size
    def print(self):
        # self._level_order_traversal()
        print(self.list)

    def peek(self):
        return self.list[1]

    def _level_order_traversal(self):
        if self.size == 0:
            return
        else:
            for i in range(1, self.size + 1):
                print(self.list[i])

    def _compare(self, left_operand, right_operand):
        if self.type == HeapType.MIN:
            return left_operand > right_operand
        if self.type == HeapType.MAX:
            return left_operand < right_operand

    def _balance_up(self, node_index: int):
        parent_index = int(node_index / 2)
        while parent_index > 0:
            if self._compare(self.list[parent_index], self.list[node_index]):
                temp = self.list[parent_index]
                self.list[parent_index] = self.list[node_index]
                self.list[node_index] = temp
                node_index = parent_index
                parent_index = int(node_index / 2)
            else:
                break

    def _balance_down(self, node_index: int):
        index = node_index
        while (index * 2) <= self.size:
            left_index = index * 2
            right_index = left_index + 1

            if right_index <= self.size and self._compare(self.list[left_index], self.list[right_index]):
                swap = right_index
            else:
                swap = left_index

            if self._compare(self.list[swap], self.list[index]):
                break
            else:
                temp = self.list[swap]
                self.list[swap] = self.list[index]
                self.list[index] = temp

                index = swap

    def delete_root(self):
        self.list[1] = self.list[self.size]
        self.list[self.size] = None
        self.size -= 1
        self._balance_down(1)

    def _get_replacement(self, index):
        left_index = index * 2
        right_index = left_index + 1
        return right_index

    def insert(self, value):
        if self.size == 0:
            self.list[1] = value
        elif self.size + 1 >= self.max_size:
            return
        else:
            self.list[self.size + 1] = value
            self._balance_up(self.size + 1)
        self.size += 1


def test_binary_heap():
    heap = BinaryHeap(8, HeapType.MIN)
    heap.insert(5)
    heap.insert(7)
    heap.insert(3)
    heap.insert(2)
    heap.insert(8)
    # heap.insert(12)
    # heap.insert(4)
    # heap.insert(9)
    # heap.insert(11)
    heap.print()
    heap.delete_root()
    heap.print()




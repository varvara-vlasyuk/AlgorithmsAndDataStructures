
class Queue:
    def __init__(self, max_length=None):
        self.list = []
        self.list_length = 0
        self.max_length = max_length

    def __str__(self) -> str:
        print_values = []
        for i in range(self.list_length - 1, -1, -1):
            print_values.append(str(self.list[i]))
        return '-'.join(print_values)

    def __iter__(self):
        for i in range(self.list_length - 1, -1, -1):
            yield self.list[i]

    def enqueue(self, value):
        if not self.max_length or self.is_full():
            self.list.insert(0, value)
            self.list_length += 1

    def dequeue(self):
        if not self.is_empty():
            elem = self.list.pop()
            self.list_length -= 1
            return elem
        return None

    def peek(self):
        return self.list[-1]

    def is_empty(self):
        if self.list_length == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.max_length > self.list_length:
            return False
        else:
            return True


class CircularQueue:
    def __init__(self, max_len):
        self.list = [None] * max_len
        self.list_len = 0
        self.max_len = max_len
        self.beg = -1
        self.end = -1

    def __str__(self):
        print_values = []
        ind = self.beg
        while True:
            print_values.append(str(self.list[ind]))
            if ind == self.end:
                break
            else:
                ind = self._next(ind)
        return '-'.join(print_values)

    def _next(self, index):
        return 0 if index > self.max_len - 1 else index + 1

    def enqueue(self, value):
        if self.is_empty():
            self.beg = self.end = 0
            self.list[0] = value
            self.list_len = 1
        elif not self.is_full():
            self.end = self._next(self.end)
            self.list[self.end] = value
            self.list_len += 1

    def dequeue(self):
        if not self.is_empty():
            elem = self.list[self.beg]
            self.beg = self._next(self.beg)
            self.list_len -= 1
            return elem
        return None

    def peek(self):
        return None if self.is_empty() else self.list[self.beg]

    def is_empty(self):
        return True if self.list_len == 0 else False

    def is_full(self):
        return False if self.max_len > self.list_len else True


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LLQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        str_list = []
        elem = self.head
        while elem:
            str_list.append(str(elem.value))
            elem = elem.next
        return '->'.join(str_list)

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.is_empty():
            elem = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return elem
        return None

    def peek(self):
        return self.head.value

    def is_empty(self):
        return self.head is None

# my_queue = LLQueue()
# print(f'Is empty {my_queue.is_empty()}')
# my_queue.enqueue(1)
# print(f'Is empty {my_queue.is_empty()}')
# # my_queue.enqueue(2)
# my_queue.enqueue(3)
# print(my_queue)
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# my_queue.enqueue(1)
#
# print(my_queue.peek())
# # print(my_queue.peek())
# print(my_queue)

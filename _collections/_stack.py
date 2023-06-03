"""
    Stack implementations based on List(read Array) and LinkedList
"""


# based on List
class StackL:
    def __init__(self, max_size=None):
        self.top = list()
        self.max_size = max_size
        self.len = 0

    def __iter__(self):
        for elem in range(len(self.top)-1, -1, -1):
            yield elem

    def __str__(self):
        print_values = list()
        for i in range(len(self.top)-1, -1, -1):
            print_values.append(str(self.top[i]))
        return '\n'.join(print_values)

    def push(self, value):
        if self.max_size is None or self.len < self.max_size:
            self.top.append(value)
            self.len += 1

    def pop(self):
        if not self.is_empty():
            return self.top.pop()

    def peek(self):
        if not self.is_empty():
            return self.top[-1]

    def is_empty(self) -> bool:
        if not self.top:
            return True
        else:
            return False

    def delete(self):
        self.top = None


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


# based on LinkedList
class StackLL:
    def __init__(self):
        self.top = None

    def __len__(self):
        elem = self.top
        count = 0
        while elem:
            count += 1
            elem = elem.next
        return count

    def __iter__(self):
        elem = self.top
        while elem:
            yield elem
            elem = elem.next

    def __str__(self):
        elem = self.top
        print_list = list()
        while elem:
            print_list.append(str(elem.value))
            elem = elem.next

        return '\n'.join(print_list)

    def push(self, value):
        new_node = Node(value)
        if self.top:
            new_node.next = self.top

        self.top = new_node

    def is_empty(self):
        if self.top:
            return False
        else:
            return True

    def pop(self):
        elem = self.top
        self.top = self.top.next
        return elem

    def peek(self):
        return self.top

    def delete(self):
        self.top = None


my_stack = StackL()
print(my_stack.is_empty())
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack)
print(f'popped {my_stack.pop()}')
print(my_stack)
print(f'peeked {my_stack.peek()}')
print(my_stack)


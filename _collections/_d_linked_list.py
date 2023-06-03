class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        elem = self.head
        while elem is not None:
            print(elem.value)
            elem = elem.next

    def add(self, value, before=None):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            elem = self.head
            while elem.next is not None:
                if elem.value == before:
                    prev_elem = elem.prev
                    prev_elem.next = new_node
                    new_node.next = elem
                    elem.prev = new_node
                    break
                elem = elem.next

            if before is None:
                elem.next = new_node
                new_node.prev = elem

    def delete(self, value):
        if self.head.value == value:
            self.head = self.head.next
        else:
            elem = self.head
            while elem is not None:
                if elem.value == value:
                    elem.prev.next = elem.next
                    break
                elem = elem.next


my_list = DoublyLinkedList()
my_list.add(1)
# my_list.add(2)
# my_list.add(3)
my_list.print()
print()
my_list.delete(1)
my_list.print()


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        elem = self.head
        while elem:
            print(elem.value)
            elem = elem.next

    # version w/ tail
    # def add(self, value, before=None):
    #     new_node = Node(value)
    #
    #     if self.head is None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         if before is None:
    #             self.tail.next = new_node
    #             self.tail = new_node
    #         elif before == self.head.value:
    #             new_node.next = self.head
    #             self.head = new_node
    #         else:
    #             elem = self.head
    #             prev_elem = None
    #             while elem.next is not None:
    #                 if elem.value == before:
    #                     prev_elem.next = new_node
    #                     new_node.next = elem
    #                     break
    #                 prev_elem = elem
    #                 elem = elem.next

    # version w/o tail
    def add(self, value, before=None):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif before == self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            elem = self.head
            prev_elem = None
            while elem.next is not None:
                if elem.value == before:
                    prev_elem.next = new_node
                    new_node.next = elem
                    break
                prev_elem = elem
                elem = elem.next

            if before is None:
                elem.next = new_node

    def delete(self, value):
        if value == self.head.value:
            self.head = self.head.next
        else:
            elem = self.head.next
            prev_elem = self.head
            while elem is not None:
                if elem.value == value:
                    prev_elem.next = elem.next
                    del elem
                    break
                prev_elem = elem
                elem = elem.next


class CircularSingleLinkedList():
    def __init__(self):
        self.head = None

    def print(self):
        elem = self.head
        while elem.next != self.head:
            print(elem.value)
            elem = elem.next

        if self.head == self.head.next:
            print(self.head.value)

    def add(self, value, before=None):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            elem = self.head.next
            prev_elem = self.head
            while elem.next != self.head:
                if elem.value == value:
                    prev_elem.next = new_node
                    new_node.next = elem
                prev_elem = elem
                elem = elem.next

            if before == self.head.value:
                elem.next = new_node
                new_node.next = self.head
                self.head = new_node
            elif before is None:
                elem.next = new_node
                new_node.next = self.head


# my_linked_list = SingleLinkedList()
#
# my_linked_list.add(1)
# my_linked_list.add(2)
# my_linked_list.add(3, 1)
# my_linked_list.print()
# print()
# my_linked_list.delete(2)
# my_linked_list.print()
my_circ_ll = CircularSingleLinkedList()
my_circ_ll.add(1)
my_circ_ll.print()
print('-')
my_circ_ll.add(2)
my_circ_ll.print()
print('--')
my_circ_ll.add(3)
my_circ_ll.print()


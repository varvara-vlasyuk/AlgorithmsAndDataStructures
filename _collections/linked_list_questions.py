class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        elem = self.head
        while elem is not None:
            yield elem
            elem = elem.next

    def __str__(self):
        values = []
        for elem in self:
            values.append(str(elem))

        return '->'.join(values)

    def __len__(self):
        count = 0
        elem = self.head
        while elem is not None:
            count += 1
            elem = elem.next

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, value):
        if self.head.value == value:
            self.head = self.head.next
        elif self.tail.value == value:
            self.tail = self.tail.prev
        else:
            elem = self.head
            while elem is not None:
                if elem.value == value:
                    elem.prev.next = elem.next
                    break
                elem = elem.next

    def deduplicate(self):
        unique_values = set()
        elem = self.head
        new_tail = None
        while elem is not None:
            if elem.value in unique_values:
                if elem.prev:
                    elem.prev.next = elem.next
                if elem.next:
                    elem.next.prev = elem.prev
            else:
                unique_values.add(elem.value)
                new_tail = elem
            elem = elem.next

        if new_tail:
            self.tail = new_tail

    def kth_to_last(self, k: int):
        arr = []
        elem = self.head
        while elem is not None:
            arr.append(elem.value)
            elem = elem.next

        return arr[-k]

    @staticmethod
    def _insert_prev(current_node, new_node):
        prev = current_node.prev
        current_node.prev = new_node
        new_node.next = current_node
        new_node.prev = prev
        if prev:
            prev.next = new_node

    @staticmethod
    def _insert_next(current_node, new_node):
        next = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
        new_node.next = next
        if next:
            next.prev = new_node

    def partition_by(self, value):
        middle_node = Node()
        new_head = middle_node
        new_tail = middle_node
        elem = self.head
        while elem:
            if elem.next is None:
                break
            new_node = Node(elem.value)
            if value < elem.value:
                self._insert_next(middle_node, new_node)
                if new_tail.value is None:
                    new_tail = new_node
            else:
                self._insert_prev(middle_node, new_node)
                if new_head.value is None:
                    new_head = new_node
            elem = elem.next

        middle_node.value = elem.value
        if new_head:
            self.head = new_head

        if new_tail:
            self.tail = new_tail

    def partition_by_v2(self, value):
        elem = self.head
        new_tail = self.head
        new_head = self.head
        while elem:
            next_elem = elem.next
            if elem.value < value:
                elem.next = new_head
                new_head.prev = elem
                elem.prev = None
                new_head = elem
            else:
                new_tail.next = elem
                elem.prev = new_tail
                elem.next = None
                new_tail = elem
            elem = next_elem

        self.head = new_head
        self.tail = new_tail

    def sum_numbers(self, llist):
        new_list = LinkedList()
        elem1 = self.head
        elem2 = llist.head
        reminder = 0
        while elem2 or elem1:
            val1 = 0 if elem1 is None else elem1.value
            val2 = 0 if elem2 is None else elem2.value

            elem_sum = val1 + val2 + reminder
            new_list.add(elem_sum % 10)
            reminder = int(elem_sum / 10)

            if elem1 is not None:
                elem1 = elem1.next

            if elem2 is not None:
                elem2 = elem2.next

        return new_list

    def sum_numbers_v2(self, llist):
        elem1 = self.head
        elem2 = llist.head
        result = LinkedList()
        reminder = 0
        while elem2 or elem1:
            el_sum = reminder
            if elem1:
                el_sum += elem1.value
                elem1 = elem1.next
            if elem2:
                el_sum += elem2.value
                elem2 = elem2.next
            result.add(el_sum % 10)
            reminder = int(el_sum / 10)
        return result

# my_list = LinkedList()
# for el in [10, 3, 2, 6, 2, 2]:
#     my_list.add(el)
#
# print(my_list)
# my_list.deduplicate()
# print(my_list)
# # print(my_list.kth_to_last(2))
# # my_list.partition_by(5)
# # print(my_list)
# my_list.partition_by_v2(5)
# print(my_list)

list1 = LinkedList()
list2 = LinkedList()
for el in [8, 3, 2, 1, 1]:
    list1.add(el)
for el in [6, 2, 2]:
    list2.add(el)

print(list1)
print(list2)

print(list1.sum_numbers_v2(list2))

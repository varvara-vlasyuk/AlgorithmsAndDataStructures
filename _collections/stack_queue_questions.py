# Three stacks based on the same list
class MultiStack:
    def __init__(self, one_stack_size):
        self.num_stacks = 3             # hardcoded because of the task requirement
        self.stack_size = one_stack_size
        self.base_list = [0] * (self.stack_size * self.num_stacks)
        self.tops = [-1] * self.num_stacks

    def __str__(self):
        final_str = ''
        for stack_ind in range(0, self.num_stacks):
            str_stack = []
            for i in range(self.tops[stack_ind], self.stack_size * stack_ind-1, -1):
                str_stack.append(str(self.base_list[i]))
            final_str += f'\nStack {stack_ind+1}:' + '->'.join(str_stack)

        return final_str

    def add(self, stack_num, value):
        if not self.is_full(stack_num):
            stack_ind = stack_num - 1
            if self.is_empty(stack_num):
                self.tops[stack_ind] = self.stack_size * stack_ind
            else:
                self.tops[stack_ind] += 1

            self.base_list[self.tops[stack_ind]] = value

    def pop(self, stack_num):
        if not self.is_empty(stack_num):
            ind = self.tops[stack_num - 1]
            if ind - 1 < (stack_num - 1) * self.stack_size:
                self.tops[stack_num - 1] = -1
            else:
                self.tops[stack_num - 1] -= 1

            return self.base_list[ind]

        return None

    def is_full(self, stack_num):
        stack_limit = self.stack_size * stack_num - 1
        return stack_limit == self.tops[stack_num - 1]

    def is_empty(self, stack_num):
        return self.tops[stack_num - 1] == -1


def multistack_test():
    multistack = MultiStack(5)
    multistack.add(1, 1)
    multistack.add(1, 1)
    multistack.add(2, 2)
    multistack.add(2, 2)
    multistack.add(3, 3)
    multistack.add(3, 3)
    print(multistack)
    multistack.pop(1)
    multistack.pop(2)
    multistack.pop(3)
    print(multistack)
    multistack.pop(1)
    multistack.pop(2)
    multistack.pop(3)
    print(multistack)
    multistack.add(1, 1)
    multistack.add(1, 1)
    multistack.add(2, 2)
    multistack.add(2, 2)
    multistack.add(3, 3)
    multistack.add(3, 3)
    print(multistack)

# create a new stack when the current one reached the threshold,
# add ability to pop\add like this is one big stack as well as pop from the concrete stack
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = []
        self.num_stacks = 0
        self.stack_size = []

    def __str__(self):
        final_str = ''
        for stack_ind in range(0, self.num_stacks):
            stack_str = []
            elem = self.top[stack_ind]
            while elem:
                stack_str.append(str(elem.value))
                elem = elem.next
            final_str += f'\nStack {stack_ind + 1}: ' + '->'.join(stack_str)

        return final_str

    def add(self, value):
        if self.is_empty() or self.is_full(self.num_stacks):
            self._new_stack(value)
        else:
            new_node = Node(value)
            new_node.next = self.top[self.num_stacks - 1]
            self.top[self.num_stacks - 1] = new_node
            self.stack_size[self.num_stacks - 1] += 1

    def pop(self):
        if not self.is_empty():
            top = self.top[self.num_stacks - 1]
            self.pop_at(self.num_stacks)
            return top.value

    def pop_at(self, stack_num):
        if not self.is_empty(stack_num):
            top = self.top[stack_num - 1]
            self.top[stack_num - 1] = top.next
            self.stack_size[stack_num - 1] -= 1
            if self.stack_size[stack_num - 1] == 0:  # and self.num_stacks > 1:
                self.top.pop(stack_num - 1)
                self.stack_size.pop(stack_num - 1)
                self.num_stacks -= 1
            return top.value
        return None

    def is_empty(self, stack_num=None):
        if stack_num:
            return stack_num > self.num_stacks or self.top[stack_num-1] is None
        else:
            return self.top == [] or self.top[0] is None

    def is_full(self, stack_num):
        return self.stack_size[stack_num-1] == self.capacity

    def _new_stack(self, value):
        self.top.append(Node(value))
        self.stack_size.append(1)
        self.num_stacks += 1


def test_set_of_stacks():
    set_of_stacks = SetOfStacks(2)
    set_of_stacks.add(1)
    set_of_stacks.add(2)
    set_of_stacks.add(1)
    set_of_stacks.add(2)
    set_of_stacks.pop()
    set_of_stacks.pop()
    set_of_stacks.pop()
    set_of_stacks.pop()
    set_of_stacks.pop()
    set_of_stacks.add(3)
    set_of_stacks.add(4)
    set_of_stacks.add(5)
    set_of_stacks.add(6)
    set_of_stacks.add(7)
    print(set_of_stacks)
    print(set_of_stacks.pop_at(2))
    print(set_of_stacks.pop_at(2))
    print(set_of_stacks.pop_at(2))
    print(set_of_stacks)
    t = [1,2]
    t.pop()


# implement a queue of animals with DequeueAny, DequeueDog, DequeueCat where the oldest shelter customer will be popped
class AnimalShelter:
    def __init__(self):
        self.end = None
        self.beg = None

    def __str__(self):
        animal = self.beg
        str_list = []
        while animal:
            str_list.append(animal.value)
            animal = animal.next
        return '->'.join(str_list)

    def enqueue(self, specie):
        new_animal = Node(specie)
        if self.is_empty():
            self.beg = new_animal
            self.end = new_animal
        else:
            self.end.next = new_animal
            self.end = new_animal

    def dequeue_any(self):
        if not self.is_empty():
            adopted = self.beg
            self.beg = self.beg.next
            if self.beg is None:
                self.end = None
            return adopted.value
        return None

    def dequeue_specie(self, specie):
        if self.beg.value == specie:
            return self.dequeue_any()
        else:
            animal = self.beg
            prev_animal = self.beg
            adopted = None
            while animal:
                if animal.value == specie:
                    prev_animal.next = animal.next
                    adopted = animal.value
                    break
                prev_animal = animal
                animal = animal.next
            return adopted

    def dequeue_cat(self):
        return self.dequeue_specie('cat')

    def dequeue_dog(self):
        return self.dequeue_specie('dog')

    def is_empty(self):
        return self.end is None


def test_animal_shelter():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    print(shelter)
    shelter.dequeue_cat()
    print(shelter)
    print(shelter.dequeue_cat())
    print(shelter.dequeue_any())
    print(shelter.dequeue_any())
    print(shelter.dequeue_any())
    print(shelter)



test_animal_shelter()

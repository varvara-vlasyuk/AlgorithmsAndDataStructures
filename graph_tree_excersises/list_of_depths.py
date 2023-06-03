"""
List of Depths
Given a binary search tree, design an algorithm
which creates a linked list of all the nodes at each depth
(ie , if you have a tree with depth D, you’ll have D linked lists)
   _5__                     [1]
  /    \
  3    8                    [3] -> [8]
 / \  / \
 2 4  7 9                   [2] -> [4] -> [7] -> [9]
/    /
1    6                      [1] -> [6]
"""


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next is None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        return "({val})".format(val=self.val) + str(self.next)

class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

def depth(tree):
    pass


# using list here for the queue because the website doesn't accept importing SimpleQueue class
def treeToLinkedList(tree, custDict={}, d=None):
    queue = [(tree, 1)]     # keeping node and its depth
    while len(queue) > 0:
        node, dep = queue.pop(0)
        if dep in custDict:
            custDict[dep].add(node.val)
        else:
            custDict[dep] = LinkedList(node.val)

        if node.left is not None:
            queue.append((node.left, dep + 1))

        if node.right is not None:
            queue.append((node.right, dep + 1))

    return custDict


def test_list_of_depths():
    my_tree = BinaryTree(1)
    my_tree.left = BinaryTree(2)
    my_tree.right = BinaryTree(3)
    my_tree.left.left = BinaryTree(4)
    my_tree.left.right = BinaryTree(5)
    my_tree.right.left = BinaryTree(6)
    my_tree.right.right = BinaryTree(7)
    for d, llst in treeToLinkedList(my_tree).items():
        node = llst
        str_list = ""
        while node is not None:
            str_list += str(node.val)
            node = node.next
        print(str_list)

"""
In-order Successor in BST - LeetCode 285
Write an algorithm to find the next node (i.e in-order successor) of given node in a binary search tree.
You may assume that each node has a link to its parent.
"""


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)


def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
        return node

# brut-force approach, moving according to in-order traversal order
def in_order_successor_search(root: Node, n):
    stack = []
    node = root
    parent_found = False
    while node or stack:
        while node is not None:
            stack.append(node)
            node = node.left

        node = stack.pop()
        print(node.data)
        if parent_found:
            return node.data
        if node.data == n:
            parent_found = True
        node = node.right
    return "nothing"


# optimized approach
def tree_min_node(root: Node):
    min_node = root
    while min_node.left is not None:
        min_node = min_node.left
    return min_node


def inOrderSuccessor(root: Node, n):
    node = root
    # search for node n
    while node is not None:
        if node.left is not None and node.data > n:
            node = node.left
        elif node.right is not None and node.data < n:
            node = node.right
        else:
            break

    if node.data == n:
        if node.right is not None:
            return tree_min_node(node.right)
        parent = node.parent
        while parent is not None:
            if node != parent.right:    # found the next node
                break
            node = parent
            parent = node.parent
        return parent

    return None


# my_tree = Node(5)
# insert(my_tree, 3)
# insert(my_tree, 8)
# insert(my_tree, 1)
# insert(my_tree, 4)
# insert(my_tree, 0)
# insert(my_tree, 2)
# insert(my_tree, 6)
# insert(my_tree, 10)
# insert(my_tree, 7)
# insert(my_tree, 9)
# insert(my_tree, 11)


my_tree = Node(8)
insert(my_tree, 3)
insert(my_tree, 7)
insert(my_tree, 4)
insert(my_tree, 5)
insert(my_tree, 6)

print(inOrderSuccessor(my_tree, 7))

"""
First Common Ancestor - LeetCode 236
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.value)


def if_tree_contains(root: Node, node):
    if root is not None:
        stack = [root]
        while stack:
            current = stack.pop()
            if current == node:
                return True
            if current.left is not None:
                stack.append(current.left)
            if current.right is not None:
                stack.append(current.right)
    return False


def findFirstCommonAncestor(n1, n2, root):
    parent = root
    while parent is not None:
        n1_in_left = if_tree_contains(parent.left, n1)
        n2_in_left = if_tree_contains(parent.left, n2)
        n1_in_right = if_tree_contains(parent.right, n1)
        n2_in_right = if_tree_contains(parent.right, n2)
        if n1_in_left and n2_in_left:
            parent = parent.left
        elif n1_in_right and n2_in_right:
            parent = parent.right
        elif (n1_in_left and n2_in_right) or (n2_in_left and n1_in_right):
            return parent
        else:
            parent = None

    return None


node1 = Node(11, Node(55), Node(77, Node(44)))
node2 = Node(22, Node(99))

# self.assertEqual(first_common_ancestor(node1, node2), None)
node3 = Node(33, node1, Node(88, Node(123, None, node2)))
node4 = Node(44, node3, Node(66))
# self.assertEqual(first_common_ancestor(node1, node2), node3)
print(findFirstCommonAncestor(node4, node2, node3))

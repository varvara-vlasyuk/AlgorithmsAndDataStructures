"""
Check Balanced - LeetCode 110
Implement a function to check if a binary tree is balanced.
For the purposes of this question, a balanced tree is defined to be a tree
such that the heights of the two subtrees of any node never differ by more than one.
"""

# Balanced Tree

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# def get_depth(node, depth):
#     if node is None:
#         return 0
#     left_depth = get_depth(node.left, depth)
#     right_depth = get_depth(node.right, depth)
#     return max(left_depth, right_depth) + 1
#
#
# def isBalanced(root):
#     left_depth = get_depth(root.left, 0)
#     right_depth = get_depth(root.right, 0)
#     if abs(left_depth - right_depth) > 1:
#         return False
#     else:
#         return True

def isBalanced(root):
    if root is None:
        return 0
    left_depth = isBalanced(root.left)
    right_depth = isBalanced(root.right)
    if abs(left_depth - right_depth) > 1:
        return -1
    return max(left_depth, right_depth) + 1


def test_balanced():
    my_tree = Node(1)
    my_tree.left = Node(2)
    my_tree.right = Node(3)
    my_tree.left.left = Node(4)
    my_tree.left.right = Node(5)
    my_tree.right.left = Node(6)
    my_tree.right.right = Node(7)
    print(isBalanced(my_tree))

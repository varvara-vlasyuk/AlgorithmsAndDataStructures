"""
Validate BST - LeetCode 98
Implement a function to check if a binary tree is a Binary Search Tree.
"""


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def isValidBST(root:TreeNode):
    queue = [root]
    while len(queue) > 0:
        node = queue.pop()
        if node.left is not None:
            if node.left.val < node.val:
                queue.append(node.left)
            else:
                return False

        if node.right is not None:
            if node.right.val > node.val:
                queue.append(node.right)
            else:
                return False

    return True


def test_validate_bst():
    my_tree = TreeNode(5)
    left_node = TreeNode(3)
    right_node = TreeNode(8)
    left_node.left = TreeNode(9)
    left_node.right = TreeNode(4)
    right_node.left = TreeNode(6)
    right_node.right = TreeNode(9)
    my_tree.left = left_node
    my_tree.right = right_node
    print(isValidBST(my_tree))

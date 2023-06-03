"""
AVL tree (Adelson-Velsky and Landis tree) is a self-balancing Binary Search Tree (BST)
where the difference of heights of left and right subtrees of any node is less than or equal to one.
This property of AVL trees makes them balanced, ensuring that operations
like insertion, deletion, and search can be done in logarithmic time.
      30
     /  \
   20   40
  /    /  \
10   35   50
"""


import queue


class AVLTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.value)


class AVLTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        prt_str = []
        level = 3
        tr_queue = queue.Queue()
        tr_queue.put(self.root)
        while not tr_queue.empty():
            node = tr_queue.get()
            if node is None:
                prt_str.append('--')
                continue
            else:
                prt_str.append(f'\n{node.value}-h{node.height}')

            if node.left is not None:
                prt_str.append(f'-l{node.left.value}')
                tr_queue.put(node.left)
            if node.right is not None:
                prt_str.append(f'-r{node.right.value}')
                tr_queue.put(node.right)

        return ''.join(prt_str)

    @staticmethod
    def _get_height(node) -> int:
        return 0 if node is None else node.height

    def _rotate_left(self, node: AVLTreeNode) -> AVLTreeNode:
        root = node.right
        node.right = root.left
        root.left = node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        return root

    def _rotate_right(self, node: AVLTreeNode) -> AVLTreeNode:
        root = node.left
        node.left = root.right
        root.right = node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        return root

    def _get_balance(self, node):
        return 0 if node is None else self._get_height(node.left) - self._get_height(node.right)

    def _rebalance(self, root):
        balance = balance = self._get_balance(root)
        # left left condition
        if balance > 1 and self._get_balance(root.left) >= 0:
            root = self._rotate_right(root)
        # left right condition
        if balance > 1 and self._get_balance(root.left) < 0:
            root.left = self._rotate_left(root.left)
            root = self._rotate_right(root)
        # right right condition
        if balance < -1 and self._get_balance(root.right) <= 0:
            root = self._rotate_left(root)
        # right left condition
        if balance < -1 and self._get_balance(root.right) > 0:
            root.right = self._rotate_right(root.right)
            root = self._rotate_left(root)

        return root

    def _insert(self, root, value):
        if root is None:
            root = AVLTreeNode(value)
        elif value > root.value:
            root.right = self._insert(root.right, value)
        else:
            root.left = self._insert(root.left, value)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        return self._rebalance(root)

    def insert_node(self, value):
        self.root = self._insert(self.root, value)

    def _search_min(self, node: AVLTreeNode) -> AVLTreeNode | None:
        if node is None or node.left is None:
            return node
        return self._search_min(node.left)

    def _delete(self, root: AVLTreeNode, value) -> AVLTreeNode | None:
        if root is None:
            return root
        elif value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)
        else:      # one child case
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:  # two children case, need a replacement
                replacement = self._search_min(root.right)
                root.value = replacement.value
                root.right = self._delete(root.right, replacement.value)
                root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        return self._rebalance(root)

    def delete_node(self, value):
        self._delete(self.root, value)


def test_avl_tree():
    tree = AVLTree()
    tree.insert_node(70)
    tree.insert_node(50)
    tree.insert_node(90)
    tree.insert_node(30)
    tree.insert_node(60)
    tree.insert_node(80)
    tree.insert_node(100)
    tree.insert_node(20)
    tree.insert_node(40)
    tree.insert_node(65)
    tree.insert_node(110)
    tree.insert_node(15)
    # tree.insert_node(40)
    tree.delete_node(40)
    tree.delete_node(15)
    tree.delete_node(65)
    tree.delete_node(60)
    tree.delete_node(80)
    tree.insert_node(105)
    tree.delete_node(90)
    print(tree)

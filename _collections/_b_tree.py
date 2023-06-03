"""
binary tree based on LinkedList
"""

import queue


class BiTreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


# class BiTree:
#     def __init__(self):
#         self.root = None
def preorder_traversal(root_node):  # root node -> left subtree -> right subtree
    if not root_node:
        return
    print(root_node.value)
    preorder_traversal(root_node.left)
    preorder_traversal(root_node.right)


def inorder_traversal(root_node):  # left subtree(sub-subtree goes first) -> root -> right subtree
    if not root_node:
        return
    inorder_traversal(root_node.left)
    print(root_node.value)
    inorder_traversal(root_node.right)


def postorder_traversal(root_node):  # left subtree -> right subtree -> root
    if not root_node:
        return
    postorder_traversal(root_node.left)
    postorder_traversal(root_node.right)
    print(root_node.value)


def levelorder_traversal(root_node):
    if not root_node:
        return
    print_queue = queue.Queue()
    print_queue.put(root_node)
    while not print_queue.empty():
        node = print_queue.get()
        print(node.value)
        if node.left is not None:
            print_queue.put(node.left)
        if node.right is not None:
            print_queue.put(node.right)


def tree_search(root,
                elem):  # level traversal was chosen because it is based on Queue(quicker) while others are based on Stack(because of recursion)
    if not root:
        return
    if root.value == elem:
        return 'Success'
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        if node.value == elem:
            return 'Success'
        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)
    return 'Failure'


def insert_node(root, value):
    new_node = BiTreeNode(value)
    if not root:
        root = new_node
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        if node.left is None:
            node.left = new_node
            break
        else:
            q.put(node.left)

        if node.right is None:
            node.right = new_node
            break
        else:
            q.put(node.right)


def delete_node(root, value):
    if not root:
        return
    buf_queue = queue.Queue()
    buf_queue.put((root, None))
    target_node = None
    node = None
    parent = None
    while not buf_queue.empty():
        node, parent = buf_queue.get()
        if node.value == value:
            target_node = node
        if node.left is not None:
            buf_queue.put((node.left, node))
        if node.right is not None:
            buf_queue.put((node.right, node))

    if target_node:
        target_node.value = node.value
        if parent.left.value == node.value:
            parent.left = None
        else:
            parent.right = None


def test_tree():
    tree = BiTreeNode('Drinks')
    # hot = BiTreeNode('Hot')
    # cold = BiTreeNode('Cold')
    # tea = BiTreeNode('Tea')
    # coffee = BiTreeNode('Coffee')
    # fanta = BiTreeNode('Fanta')
    # hot.left = tea
    # hot.right = coffee
    # cold.left = fanta
    # tree.left = hot
    # tree.right = cold
    insert_node(tree, 'Hot')
    insert_node(tree, 'Cold')
    insert_node(tree, 'Tea')
    insert_node(tree, 'Coffee')
    insert_node(tree, 'Fanta')

    # preorder_traversal(tree)
    # inorder_traversal(tree)
    levelorder_traversal(tree)
    # print(tree_search(tree, 'C'))
    delete_node(tree, 'Hot')
    print()
    levelorder_traversal(tree)


class BTreeList:
    def __init__(self, size):
        self.list = size * [None]
        self.last_filled = 0
        self.max_size = size

    def __str__(self):
        if self.list[1] is None:
            return
        final_str = 'Tree:\n'
        tree_level = 1
        for i in range(1, self.last_filled + 1):
            final_str += str(self.list[i]) + '  '
            if i == pow(2, tree_level) - 1:
                final_str += '\n'
                tree_level += 1
        return final_str

    @staticmethod
    def _get_left_index(ind):
        return ind * 2

    @staticmethod
    def _get_right_index(ind):
        return ind * 2 + 1

    def _search_available(self):
        if self.list[1] is None:
            return 1
        else:
            buf_queue = queue.Queue()
            buf_queue.put(1)
            while not buf_queue.empty():
                ind = buf_queue.get()
                if ind >= self.max_size:
                    return None
                left_ind = self._get_left_index(ind)
                right_ind = self._get_right_index(ind)
                if left_ind < self.max_size and self.list[left_ind] is None:
                    return left_ind
                else:
                    buf_queue.put(left_ind)

                if right_ind < self.max_size and self.list[right_ind] is None:
                    return right_ind
                else:
                    buf_queue.put(right_ind)

    def search_node(self, value):
        for i in range(1, self.last_filled):
            if self.list[i] == value:
                print('Success')
                return i

        print('Failure')
        return None

    def insert_node(self, value):
        if self.last_filled + 1 == self.max_size:
            print('Tree is full')
        else:
            self.last_filled += 1
            self.list[self.last_filled] = value

    def delete_node(self, value):
        ind = self.search_node(value)
        self.list[ind] = self.list[self.last_filled]
        self.list[self.last_filled] = None
        self.last_filled -= 1

    def preorder_tr(self, index):
        if index >= self.max_size:
            return
        print(self.list[index])
        self.preorder_tr(self._get_left_index(index))
        self.preorder_tr(self._get_right_index(index))

    def inorder_tr(self, index):
        if index >= self.max_size:
            return
        self.inorder_tr(self._get_left_index(index))
        print(self.list[index])
        self.inorder_tr(self._get_right_index(index))

    def postorder_tr(self, index):
        if index >= self.max_size:
            return
        self.postorder_tr(self._get_left_index(index))
        self.postorder_tr(self._get_right_index(index))
        print(self.list[index])

def test_btree_list():
    tree = BTreeList(8)
    tree.insert_node(1)
    tree.insert_node(2)
    tree.insert_node(3)
    tree.insert_node(4)
    tree.insert_node(5)
    tree.insert_node(6)
    tree.insert_node(7)
    tree.delete_node(4)
    tree.insert_node(4)
    # tree.insert_node(4)
    print(tree)
    # tree.postorder_tr(1)


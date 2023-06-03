"""
Binary Search Tree (BST) is a tree data structure in which each node has at most two children,
referred to as the left child and the right child. For each node, all elements in the left subtree
are less than the node, and all elements in the right subtree are greater than the node.
        50
    30      70
20    40   60   80
"""
import queue

from _b_tree import BiTreeNode


class BST:
    def __init__(self):
        self.root = None

    def _tree_to_str_list(self, str_list: list, node: BiTreeNode = None):
        if not node and str_list == []:
            node = self.root
        if not node:
            return

        str_list.append(str(node.value))
        self._tree_to_str_list(str_list, node.left)
        self._tree_to_str_list(str_list, node.right)

    def print_levels(self):
        node = self.root
        qu = queue.Queue()
        qu.put(node)
        count = 1
        level = 1
        prt_str = ''
        while not qu.empty():
            node = qu.get()
            if node:
                prt_str += ' '*(20-level*3) + f'{str(node.value)}'   # ({None if node.left is None else node.left.value},{None if node.right is None else node.right.value})'
                qu.put(node.left)
                qu.put(node.right)
            else:
                prt_str += ' '*(15-level*3) + 'N' #+ ' '*(25-level*4)
                # prt_str += 'N' + ' '*(25-level*4)

            count += 1
            if pow(2, level) == count:
                level += 1
                prt_str += '\n'
        return prt_str

    def __str__(self):
        str_list = []
        self._tree_to_str_list(str_list, self.root)
        return '\n'.join(str_list)

    def insert_node(self, value) -> BiTreeNode | None:
        new_node = BiTreeNode(value)
        if not self.root:
            self.root = new_node
            return

        tnode = self.root
        while tnode:
            if value > tnode.value:
                if tnode.right:
                    tnode = tnode.right
                else:
                    tnode.right = new_node
                    break
            else:
                if tnode.left:
                    tnode = tnode.left
                else:
                    tnode.left = new_node
                    break

    def delete_node(self, value):
        target = self._search(self.root, value)
        self._delete_root(target)

    def _delete_root(self, root: BiTreeNode):
        # case 1 -- leaf w/ no children
        if root.left is None and root.right is None:
            parent = self._search_parent(self.root, root)
            if parent.left == root:
                parent.left = None
            if parent.right == root:
                parent.right = None
        elif root.left is None or root.right is None:
            if root.left is not None:
                root.value = root.left.value
                root.left = None
            elif root.right is not None:
                root.value = root.right.value
                root.right = None
        else:
            replacement = self._search_min(root.right, root.right)
            root.value = replacement.value
            self._delete_root(replacement)

    def _search_parent(self, root: BiTreeNode, node: BiTreeNode) -> BiTreeNode | None:
        if not root:
            return None

        if root.left == node or root.right == node:
            return root

        parent = self._search_parent(root.left, node)
        if parent is not None:
            return parent
        parent = self._search_parent(root.right, node)

        return parent

    def _search(self, root: BiTreeNode, value) -> BiTreeNode | None:
        if not root:
            return None

        if root.value == value:
            return root
        l = root.left
        l_res = self._search(root.left, value)
        r_res = self._search(root.right, value)

        if l_res:
            return l_res
        elif r_res:
            return r_res
        else:
            return None

    def _search_min(self, root: BiTreeNode, min_node: BiTreeNode) -> BiTreeNode | None:
        if not root:
            return min_node

        min_node = self._search_min(root.left, min_node)
        min_node = self._search_min(root.right, min_node)

        if root.value < min_node.value:
            min_node = root

        return min_node

    def search_node(self, value, root=None) -> BiTreeNode | None:
        if not root:
            root = self.root

        result = self._search(root, value)
        return None if result is None else result.value


def test_bst():
    tree = BST()
    tree.insert_node(10)
    tree.insert_node(12)
    tree.insert_node(2)
    tree.insert_node(8)
    tree.insert_node(3)
    tree.insert_node(1)
    tree.insert_node(13)
    tree.insert_node(13)
    tree.insert_node(13)
    tree.insert_node(13)
    tree.insert_node(13)
    node = tree._search(tree.root, 3)
    # print(tree)
    # print(f'value = {node}')
    # num = 2
    # print(f'deleted {num} replaced w/ {tree.delete_node(num)}')
    print(tree.print_levels())
    tree.delete_node(2)
    print(tree.print_levels())


test_bst()

"""
Minimal Tree
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.

Example

sortedArray = [1,2,3,4,5,6,7,8,9]
minimalTree(sortedArray)

#Output

   _5__
  /    \
  3    8
 / \  / \
 2 4  7 9
/    /
1    6
"""
from queue import SimpleQueue


class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# sortedArray = [1,2,3,4,5,6,7,8,9]
# 5 - root; ltree - 1,2,3,4; rtree - 6,7,8,9
# 2 - root; ltree - 1; rtree - 3,4
# 7 - root; ltree - 6; rtree - 8,9
def minimalTree(sortedArray):
    tree_root = BSTNode()
    queue = SimpleQueue()
    queue.put((0, len(sortedArray) - 1, tree_root))
    while not queue.empty():
        beg, end, root = queue.get()
        mid = beg + int((end - beg) / 2)
        root.data = sortedArray[mid]
        # left
        lbeg = beg
        lend = mid - 1
        if lbeg < lend:
            root.left = BSTNode()
            queue.put((lbeg, lend, root.left))
        elif lbeg == lend:
            root.left = BSTNode(data=sortedArray[lbeg])
        # right
        rbeg = mid + 1
        rend = end
        if rbeg < rend:
            root.right = BSTNode()
            queue.put((rbeg, rend, root.right))
        elif rbeg == rend:
            root.right = BSTNode(data=sortedArray[rbeg])

    return tree_root


def print_tree(root: BSTNode):
    queue = SimpleQueue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        # print(f'{node.data}: {node.left.data} - {node.right.data}')
        if node.left is not None:
            queue.put(node.left)
            print(f'{node.data}:l {node.left.data}')
        if node.right is not None:
            queue.put(node.right)
            print(f'{node.data}:r {node.right.data}')


def test_min_tree():
    sortedArray = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
    tree = minimalTree(sortedArray)
    print_tree(tree)
    print(sortedArray[:5])


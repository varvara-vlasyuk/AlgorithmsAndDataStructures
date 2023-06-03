"""
Disjoined set is a data structure that represents a number of separate sets with two operations:
e.g. we have a disjoined set containing two sets A(1, 2, 3) and B(4, 5)
Find - checks if two given elements are in the same set
    find(2, 4) = False
    find(1, 3) = True
Union - merges two given sets
    union(A,B) = (1, 2, 3, 4, 5)
Each set from the disjoined set has the root. The root is a main element that takes part in the operations above.
Rank shows the original deep of the branch, it can only increase(and can't decrease).
If we merge two sets in one the result set takes the higher rank OR the rank of the root set increases(if both ranks are equal)
"""


class DisjoinedSet:
    def __init__(self, vertices: list):
        self.vertices = vertices
        self.parent = dict.fromkeys(self.vertices, -1)
        self.rank = dict.fromkeys(self.parent, 0)

    def _find_root(self, vert):
        root = vert
        while True:
            if self.parent[root] != -1:
                root = self.parent[root]
            else:
                break
        self.parent[vert] = root if self.parent[vert] != -1 else -1
        return root

    def union(self, vert1, vert2):
        root1 = self._find_root(vert1)
        root2 = self._find_root(vert2)

        if root2 == root1:
            return False

        if self.rank[vert1] > self.rank[vert2]:
            self.parent[vert2] = root1
        elif self.rank[vert1] < self.rank[vert2]:
            self.parent[vert1] = root2
        else:
            self.parent[vert2] = root1
            self.rank[vert2] += 1

        return True


def test_djs():
    vert = ["a", "b", "c", "d"]
    my_djset = DisjoinedSet(vert)
    my_djset.union("a", "b")
    my_djset.union("a", "c")
    my_djset.union("c", "d")
    print(my_djset.parent)

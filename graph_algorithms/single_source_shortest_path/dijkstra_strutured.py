"""
here we will use two data structures for node and edge as well as a class for the Dijkstra calculation
"""
import heapq
from typing import List

# TODO : implement Dijkstra class that can cache the paths
# the idea is that Dijkstra class will run calculate method only if the graph topology has changed
# otherwise the calculated results would be preserved as a map Vertex : Distances to all the other vertices


class Edge:
    def __init__(self):
        self.src: Node
        self.dst: Node
        self.weight = 0


class Node:
    def __init__(self, name):
        self.node = name
        self.min_distance = float("inf")
        self.visited = False
        self.predecessor: Node
        self.neighbours: List[Edge] = []    # list of edges

    def __lt__(self, other_node: 'Node') -> bool:
        return self.min_distance < other_node.min_distance

    def add_neighbours(self, neighbours: List[Edge]):
        self.neighbours = neighbours

    def add_neighbour(self, neighbour: Edge):
        self.neighbours.append(neighbour)


class Dijkstra:
    def __init__(self, graph: List[Node]):
        self.graph = graph.copy()
        self.heap = []
        self.calc_map = {}              # node_name: list of distances
        # heapq.heappushpop()

    def calculate(self):
        pass



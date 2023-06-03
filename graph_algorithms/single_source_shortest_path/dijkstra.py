"""
Directed weighted graph:
dictionary of dictionaries, e.g:
{
    "A": {
            "B": 4,
            "C": 8
    },
    "B": {
            "D": 11
            "E": 2
    },
    "D": {}
    "E": {}
}
each node will have the following attributes:
min_distance - the distance from start to the given node
predecessor - the node where we came from to the given node with the min distance
neighbours - all the nodes where we can move to from the given node

we will also use visited set and queue
"""
from typing import Tuple

from graph_algorithms.graph import DirectedWeightedGraph
from queue import SimpleQueue


def dijkstra(graph: DirectedWeightedGraph, start, finish) -> Tuple[float, list]:
    visited = set()
    min_distance = dict.fromkeys(graph.graph.keys(), float("inf"))
    predecessor = {}
    queue = SimpleQueue()
    queue.put(start)
    predecessor[start] = None
    min_distance[start] = 0
    while not queue.empty():
        vert = queue.get()
        if vert not in visited:
            neighbours = graph.get_neighbours(vert)
            for v, w in neighbours.items():
                if min_distance[v] > min_distance[vert] + w:
                    queue.put(v)
                    min_distance[v] = min_distance[vert] + w
                    predecessor[v] = vert
                    # this step is needed in case we recalculated the node min distance,
                    # which means we need to recalculate its neighbours once again
                    visited.discard(v)
        visited.add(vert)
        if len(visited) == len(min_distance):
            break

    cur = finish
    path = []
    it = 0
    while it <= len(predecessor) * 2:
        path.append(cur)
        if cur == start:
            break
        else:
            cur = predecessor[cur]
            it += 1

    return min_distance[finish], path


my_graph = DirectedWeightedGraph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")
my_graph.add_vertex("F")
my_graph.add_vertex("G")
my_graph.add_vertex("H")
my_graph.add_neighbours("A", {"B": 6, "D": 9, "C": 2})
my_graph.add_neighbours("B", {"E": 16, "F": 13, "D": 5})
my_graph.add_neighbours("C", {"D": 6, "H": 5, "G": 21})
my_graph.add_neighbours("D", {"F": 8, "H": 7})
my_graph.add_neighbours("F", {"E": 4, "G": 12})
my_graph.add_neighbours("E", {"G": 10})
my_graph.add_neighbours("H", {"F": 2, "G": 14})
print(dijkstra(my_graph, "A", "F"))

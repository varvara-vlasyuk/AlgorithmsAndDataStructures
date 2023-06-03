"""
Prim's algorithm
Finds minimum spanning tree (MST)
"""
from pprint import pprint
from queue import SimpleQueue

from graph_algorithms.graph import WeightedGraph


def prim(graph: WeightedGraph):
    start = graph.get_first_vertex()
    visited = set(start)
    mst = [start]
    while len(visited) < len(graph):
        vertex = mst[-1]
        min_weight = float("inf")
        next_vertex = None
        for vert, weight in graph.get_neighbours(vertex).items():
            if vert not in visited and min_weight > weight:
                min_weight = weight
                next_vertex = vert
        mst.append(next_vertex)
        visited.add(next_vertex)
    print(mst)


def test_prim():
    my_graph = WeightedGraph()
    my_graph.add_edge("A", "B", 10)
    my_graph.add_edge("A", "C", 20)
    my_graph.add_edge("B", "C", 1)
    my_graph.add_edge("B", "D", 5)
    my_graph.add_edge("C", "D", 15)
    my_graph.add_edge("C", "E", 6)
    my_graph.add_edge("D", "E", 8)
    pprint(my_graph.graph)
    prim(my_graph)

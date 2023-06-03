"""
Kruskal's algorithm
Finds minimum spanning tree (MST)
"""
from typing import Tuple, Any

from graph_algorithms.graph import WeightedGraph
from graph_algorithms.disjoint_set import DisjoinedSet


def kruskal(graph: WeightedGraph) -> Tuple[list, float]:
    vertices = graph.get_vertices()
    djs = DisjoinedSet(vertices)
    mst = []
    length = 0
    edges = graph.get_edges()
    edges = sorted(edges, key=lambda e: e[2])
    for v1, v2, w in edges:
        if djs.union(v1, v2):
            mst.append((v1, v2, w))
            length += w

    return mst, length


def test_kruskal():
    my_graph = WeightedGraph()
    my_graph.add_edge("A", "B", 5)
    my_graph.add_edge("A", "C", 13)
    # my_graph.add_edge("B", "A", 5)
    my_graph.add_edge("B", "C", 10)
    my_graph.add_edge("B", "D", 8)
    # my_graph.add_edge("C", "A", 13)
    # my_graph.add_edge("C", "B", 10)
    # my_graph.add_edge("C", "D", 6)
    # my_graph.add_edge("D", "B", 8)
    my_graph.add_edge("D", "C", 6)
    # my_graph.add_edge("A", "E", 15)
    my_graph.add_edge("E", "A", 15)
    # my_graph.add_edge("C", "E", 20)
    my_graph.add_edge("E", "C", 20)
    for edge in my_graph.get_edges():
        # print(f'{edge[0]}, {edge[1]}, {edge[2]}')
        print(edge)
    mst_list, mst_length = kruskal(my_graph)
    print(mst_list)
    print(mst_length)

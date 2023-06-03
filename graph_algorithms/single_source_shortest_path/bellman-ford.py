from graph_algorithms.graph import DirectedWeightedGraph


def bellman_ford(graph: DirectedWeightedGraph, start):
    min_distance = dict.fromkeys(graph.graph.keys(), float("inf"))
    min_distance[start] = 0
    for _ in range(len(graph.graph.keys()) - 1):
        for v1, v2, w in graph.get_all_edges():
            if min_distance[v2] > min_distance[v1] + w:
                min_distance[v2] = min_distance[v1] + w

    # negative cycle condition
    for v1, v2, w in graph.get_all_edges():
        if min_distance[v2] > min_distance[v1] + w:
            print("negative cycle")
            return

    print(min_distance)


my_graph = DirectedWeightedGraph()
# my_graph.add_edge("A", "C", 6)
# my_graph.add_edge("A", "D", 6)
# my_graph.add_edge("B", "A", 3)
# my_graph.add_edge("C", "D", 1)
# my_graph.add_edge("D", "C", 2)
# my_graph.add_edge("D", "B", 1)
# my_graph.add_edge("E", "B", 4)
# my_graph.add_edge("E", "D", 2)
my_graph.add_edge("A", "B", -1)
my_graph.add_edge("A", "C", -1)
my_graph.add_edge("B", "D", -1)
my_graph.add_edge("C", "D", -1)
bellman_ford(my_graph, "A")

"""
BST stands for breadth first search
"""
from graph_algorithms.graph import DirectedGraph
from queue import SimpleQueue


# we add to the queue all the paths and extend each.
# e.g. 2nd iteration queue contains ["A","B"], ["A","C"]
# path is an array, not a vertex
def bfs(graph: DirectedGraph, start, end):
    queue = SimpleQueue()
    queue.put([start])
    while not queue.empty():
        path = queue.get()
        vert = path[-1]
        if vert == end:
            return path
        for v in graph.adj_dict.get(vert, []):
            draft_path = path.copy()
            draft_path.append(v)
            queue.put(draft_path)


my_dict = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["E", "F"],
    "E": [],
    "F": [],
}
my_graph = DirectedGraph(my_dict)
print(bfs(my_graph, "A", "E"))

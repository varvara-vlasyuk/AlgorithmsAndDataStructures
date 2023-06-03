from graph import Graph
from queue import SimpleQueue


# Breadth First Search
def bfs(graph: Graph, start):
    visited = set()
    queue = SimpleQueue()
    queue.put(start)
    while not queue.empty():
        vert = queue.get()
        if vert not in visited:
            print(vert)
            visited.add(vert)
            for v in graph.adj_dict[vert]:
                if v not in visited:
                    queue.put(v)


# Depth First Search
def dfs(graph: Graph, start):
    visited = set()
    stack = [start]
    while stack:
        vert = stack.pop()
        if vert not in visited:
            print(vert)
            visited.add(vert)
            for v in graph.adj_dict[vert]:
                if v not in visited:
                    stack.append(v)


def test_traversal():
    my_dict = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "E"],
        "D": ["B", "E", "F"],
        "E": ["D", "F"],
        "F": ["D", "E"],
    }
    my_graph = Graph(my_dict)
    bfs(my_graph, "A")
    dfs(my_graph, "A")


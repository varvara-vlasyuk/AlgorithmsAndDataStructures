from collections import defaultdict


class TopologicalGraph:
    def __init__(self, num_vertex: int):
        self.gdict = defaultdict(list)
        self.num_vertex = num_vertex

    def __str__(self):
        str_repr = ''
        for vert, edges in self.gdict.items():
            str_repr += f'{str(vert)} : {edges}\n'
        return str_repr

    def _add_vertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []

    def add_edge(self, vertex, edge):
        self._add_vertex(vertex)
        self._add_vertex(edge)
        self.gdict[vertex].append(edge)

    def ts_util(self, vertex, visited, stack):
        visited.add(vertex)
        for vert in self.gdict[vertex]:
            if vert not in visited:
                self.ts_util(vert, visited, stack)

        stack.append(vertex)

    def topological_sort(self):
        visited = set()
        stack = []
        for vertex in self.gdict.keys():
            if vertex not in visited:
                self.ts_util(vertex, visited, stack)

        print(stack)


def test_topological_graph():
    my_graph = TopologicalGraph(8)
    my_graph.add_edge("A", "C")
    my_graph.add_edge("C", "E")
    my_graph.add_edge("E", "H")
    my_graph.add_edge("E", "F")
    my_graph.add_edge("F", "G")
    my_graph.add_edge("B", "D")
    my_graph.add_edge("B", "C")
    my_graph.add_edge("D", "F")
    print(my_graph)
    my_graph.topological_sort()



my_dict = defaultdict(int)
my_dict["a"] = 1
print(my_dict["b"])

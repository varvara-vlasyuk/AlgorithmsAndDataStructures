# adjacency list as a dictionary
from typing import Any, List, Tuple


class Graph:
    def __init__(self, gdict: dict = None):
        if gdict is None:
            self.adj_dict: dict = {}
        else:
            self.adj_dict = gdict

    def __str__(self):
        str_repr = ''
        for vert, edges in self.adj_dict.items():
            str_repr += f'{str(vert)} : {edges}\n'
        return str_repr

    def _vertex_exists(self, vertex):
        return True if vertex in self.adj_dict.keys() else False

    def _add_vertex(self, vertex):
        if not self._vertex_exists(vertex):
            self.adj_dict[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self._add_vertex(vertex1)
        self._add_vertex(vertex2)
        self.adj_dict[vertex1].append(vertex2)
        self.adj_dict[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if self._vertex_exists(vertex1) and self._vertex_exists(vertex2):
            self.adj_dict[vertex1].remove(vertex2)
            self.adj_dict[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        edges = self.adj_dict.pop(vertex)
        for edge in edges:
            self.adj_dict[edge].remove(vertex)


class DirectedGraph(Graph):
    def __init__(self, gdict: dict = None):
        super().__init__(gdict)

    def add_edge(self, vertex1, vertex2):
        self._add_vertex(vertex1)
        self.adj_dict[vertex1].append(vertex2)


class WeightedGraph:
    def __init__(self):
        self.graph: dict[Any, dict[Any, float]] = {}
        self.vertices = []

    def __len__(self):
        return len(self.graph)

    def add_vertex(self, vert):
        if vert not in self.graph.keys():
            self.graph[vert] = {}
            self.vertices.append(vert)

    def add_edge(self, vert_from, vert_to, weight: float):
        self.add_vertex(vert_from)
        self.add_vertex(vert_to)
        self.graph[vert_from][vert_to] = weight
        self.graph[vert_to][vert_from] = weight

    def get_vertices(self) -> List:
        return list(self.graph.keys())

    def get_neighbours(self, vertex) -> dict[Any, float]:
        return self.graph[vertex]

    def get_min_edge(self) -> Tuple[Tuple[Any, Any], float]:
        vertices = self.get_vertices()
        min_weight = float("inf")
        min_edge = ()
        for v1 in vertices:
            for v2 in vertices:
                if self.graph[v1][v2] < min_weight:
                    min_weight = self.graph[v1][v2]
                    min_edge = (v1, v2)

        return min_edge, min_weight

    # for Kruskal's
    def get_edges(self) -> List[Tuple]:
        vertices = self.get_vertices()
        edges = []
        # taking edges under the main diagonal to get rid of duplicates
        i = 0
        for v1 in vertices:
            j = 0
            for v2 in vertices:
                if j > i and v2 in self.graph[v1].keys():
                    edge = (v1, v2, self.graph[v1][v2])
                    edges.append(edge)
                j += 1
            i += 1
        return edges

    # for Prim's
    def get_first_vertex(self):
        return self.vertices[0]


class DirectedWeightedGraph(WeightedGraph):
    def __init__(self):
        super().__init__()

    def add_edge(self, vert_from, vert_to, weight: float):
        self.add_vertex(vert_from)
        self.add_vertex(vert_to)
        self.graph[vert_from][vert_to] = weight

    def add_neighbours(self, vert, neighbours: dict[Any, float]):
        self.graph[vert] = neighbours

    # for Bellman-Ford
    def get_all_edges(self) -> List[Tuple[Any, Any, float]]:
        result_list: List[Tuple[Any, Any, float]] = []
        for vertex1 in self.graph.keys():
            for vertex2, weight in self.get_neighbours(vertex1).items():
                result_list.append((vertex1, vertex2, weight))

        return result_list

    # for Floyd-Warshall
    def build_matrix(self) -> Tuple[dict[Any, int], List[List[float]]]:
        matrix: list[list[float]] = [[float("inf") for j in range(len(self.graph))] for i in range(len(self.graph))]
        vert_index: dict[Any, int] = dict.fromkeys(self.graph.keys())
        ind = 0
        for vert in self.graph.keys():
            vert_index[vert] = ind
            ind += 1

        for vert in self.graph.keys():
            src_ind = vert_index[vert]
            matrix[src_ind][src_ind] = 0
            for v, w in self.get_neighbours(vert).items():
                dst_ind = vert_index[v]
                matrix[src_ind][dst_ind] = w

        return vert_index, matrix


def test_graph():
    my_dict = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["A"]
    }
    my_graph = Graph(my_dict)
    my_graph.add_edge("A", "D")
    my_graph.remove_vertex("A")
    print(my_graph)



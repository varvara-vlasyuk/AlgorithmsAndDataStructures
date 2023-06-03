"""
the solution is based on the adj. matrix realisation of a graph,
where cell value
            = weight if the edge exists,
            = infinity if edge doesn't exist and
            = 0 in the main diagonal
there are 3 levels of iterations:
1. the vertex in the middle of the path, e.g. we can reach C from A through B, then B will be middle vertex
2. start vertex
3. end vertex

The idea is to visit each cell of the matrix with each middle vertex
and calculate the path from i to j through middle vertex
"""
from graph_algorithms.graph import DirectedWeightedGraph

INF = 9999


# Printing the solution
def printSolution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if (distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


def floydWarshall(nV, G):
    distance = G
    count = 0
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                count += 1
    print(count)
    printSolution(nV, distance)


def floyd_warshall(graph: DirectedWeightedGraph):
    vert_map, graph_matrix = graph.build_matrix()
    print(vert_map)
    print(graph_matrix)
    count = 0
    for k in range(len(graph_matrix)):              # middle vertex
        for i in range(len(graph_matrix)):          # start of the path
            if i == k:
                continue
            for j in range(len(graph_matrix)):      # end of the path
                if j == k:
                    continue
                graph_matrix[i][j] = min(graph_matrix[i][j], graph_matrix[k][j] + graph_matrix[i][k])
                count += 1
    print(count)
    print(graph_matrix)


#     A   B  C   D
G = [[0, 8, INF, -1],  # A
     [INF, 0, 1, INF],  # B
     [4, INF, 0, INF],  # C
     [INF, 2, 9, 0]  # D
     ]
print(G)
print("given impl")
floydWarshall(4, G)


my_graph = DirectedWeightedGraph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_neighbours("A", {"B": 8, "D": 1})
my_graph.add_neighbours("D", {"B": 2, "C": 9})
my_graph.add_neighbours("B", {"C": 1})
my_graph.add_neighbours("C", {"A": 4})
print("my impl")
floyd_warshall(my_graph)

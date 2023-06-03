"""
Route Between Nodes
Given a directed graph and two nodes (S and E).
Based on the given Graph class implementation design an algorithm to find out whether there is a route from S to E.

Examples

customDict = { "a" : ["c","d", "b"],
            "b" : ["j"],
            "c" : ["g"],
            "d" : [],
            "e" : ["f", "a"],
            "f" : ["i"],
            "g" : ["d", "h"],
            "h" : [],
            "i" : [],
            "j" : []
               }

g = Graph(customDict)
g.checkRoute("a", "j") #True
"""
from queue import SimpleQueue

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def checkRoute(self, startNode, endNode):       # BFS
        visited = set()
        queue = SimpleQueue()
        queue.put(startNode)
        while not queue.empty():
            vertex = queue.get()
            for vert in self.gdict[vertex]:
                if vert not in visited:
                    if vert == endNode:
                        return True
                    queue.put(vert)
                    visited.add(vert)
        return False


def test():
    customDict = { "a" : ["c","d", "b"],
                "b" : ["j"],
                "c" : ["g"],
                "d" : [],
                "e" : ["f", "a"],
                "f" : ["i"],
                "g" : ["d", "h"],
                "h" : [],
                "i" : [],
                "j" : []
                   }

    g = Graph(customDict)
    print(g.checkRoute("a", "e"))

"""
Graph
Graphs are networks consisting of nodes connected by edges or arcs.
In directed graphs, the connections between nodes have a direction, and are called arcs; in undirected graphs,
the connections have no direction and are called edges. We mainly discuss directed graphs.
Algorithms in graphs include finding a path between two nodes, finding the shortest path between two nodes,
determining cycles in the graph (a cycle is a non-empty path from a node to itself),
finding a path that reaches all nodes (the famous "traveling salesman problem"), and so on.
Sometimes the nodes or arcs of a graph have weights or costs associated with them,
and we are interested in finding the cheapest path.  ---https://www.python.org/doc/essays/graphs/
"""
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    def __repr__(self):
        return 'Graph(%s, %s)' % (dict(self.graph), self.V)

    # function to add an edge(u->v) to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)


g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print(g)

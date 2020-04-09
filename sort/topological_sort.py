"""
Topological sorting for Directed Acyclic Graph (DAG)
time complexity: O(n)

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge
uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

refers:
https://www.geeksforgeeks.org/python-program-for-topological-sorting/
https://www.geeksforgeeks.org/topological-sorting/
"""
from graph import Graph, g


# A recursive function used by topological_sort
def topological_sort_util(graph, v, visited, stack):
    # Mark the current node as visited.
    visited[v] = True

    # Recur for all the vertices adjacent to this vertex
    for i in graph.graph[v]:
        if not visited[i]:
            topological_sort_util(graph, i, visited, stack)

            # Push current vertex to stack which stores result
    stack.insert(0, v)

    # The function to do Topological Sort. It uses recursive


def topological_sort(graph):
    """
    graph: instance of Graph in graph.py
    """
    # Mark all the vertices as not visited
    visited = [False] * graph.V
    stack = []

    # Call the recursive helper function to store Topological
    # Sort starting from all vertices one by one
    for i in range(graph.V):
        if not visited[i]:
            topological_sort_util(graph, i, visited, stack)

    # Print contents of stack
    print("STACK: ", stack)


topological_sort(g)

print('************************2***************************')

def topological_sort_2(graph):
    is_visit = dict((node, False) for node in graph)
    li = []

    def dfs(graph, start_node):

        for end_node in graph[start_node]:
            if not is_visit[end_node]:
                is_visit[end_node] = True
                dfs(graph, end_node)
        li.append(start_node)

    for start_node in graph:
        if not is_visit[start_node]:
            is_visit[start_node] = True
            dfs(graph, start_node)

    li.reverse()
    return li


graph_2 = {
        'v1': ['v5'],
        'v2': ['v1'],
        'v3': ['v1', 'v5'],
        'v4': ['v2', 'v5'],
        'v5': [],
    }
li = topological_sort_2(graph_2)
print('li', li)

import importlib
G = importlib.import_module('1_graph')
AdjListGraph = getattr(G, 'AdjListGraph')
create_graph_one = getattr(G, 'create_graph_one')
create_graph_two = getattr(G, 'create_graph_two')
create_graph_three = getattr(G, 'create_graph_three')

from collections import deque as Queue


def adj_list_dfs_recursive(graph, source, marked, color):
    for v in graph.adjacent(source):
        if not marked[v]:
            marked[v] = True
            color[v] = 1 - color[source]
            if not adj_list_dfs_recursive(graph, v, marked, color):
                return False
        elif color[source] == color[v]:
            return False

    return True


def adj_list_bfs_iterative(graph, source, marked, color):
    q = Queue()
    q.append(source)

    while (q):
        v = q.popleft()
        for w in graph.adjacent(v):
            if not marked[w]:
                marked[w] = True
                color[w] = 1 - color[v]
                q.append(w)
            elif color[v] == color[w]:
                return False

    return True


def dfs_main():

    graph = AdjListGraph(7)
    graph = create_graph_three(graph)

    color = [-1] * graph.num_of_vertices()
    marked = [False] * graph.num_of_vertices()

    source_vertex = 0
    color[source_vertex] = 1
    marked[source_vertex] = True

    return adj_list_dfs_recursive(graph, source_vertex, marked, color)


def bfs_main():
    graph = AdjListGraph(7)
    graph = create_graph_three(graph)

    color = [-1] * graph.num_of_vertices()
    marked = [False] * graph.num_of_vertices()

    source_vertex = 0
    color[source_vertex] = 1
    marked[source_vertex] = True

    return adj_list_bfs_iterative(graph, source_vertex, marked, color)


if __name__ == '__main__':
    print(dfs_main())
    print(bfs_main())

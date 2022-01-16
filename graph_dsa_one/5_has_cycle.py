import importlib
G = importlib.import_module('1_graph')
AdjListGraph = getattr(G, 'AdjListGraph')
create_graph_one = getattr(G, 'create_graph_one')
create_graph_four = getattr(G, 'create_graph_four')

from collections import deque as Queue


def adj_list_dfs_recursive(graph, source, marked, parent_vertex):
    marked[source] = True

    for v in graph.adjacent(source):
        if not marked[v]:
            if adj_list_dfs_recursive(graph, v, marked, source):
                return True
        elif v != parent_vertex:
            return True

    return False


def adj_list_bfs_iterative(graph, source, marked, parent_vertex):
    q = Queue()
    q.append((source, parent_vertex))
    marked[source] = True

    while(q):
        s, parent = q.popleft()
        for v in graph.adjacent(s):
            if not marked[v]:
                marked[v] = True
                q.append((v, s))
            elif v != parent:
                return True

    return False



def dfs_main():
    graph = AdjListGraph(13)
    graph = create_graph_one(graph)

    ''' graph = AdjListGraph(4)
    graph = create_graph_four(graph) '''

    marked = [False] * graph.num_of_vertices()
    parent_vertex = -1

    for s in range(graph.num_of_vertices()):
        if not marked[s]:
            if adj_list_dfs_recursive(graph, s, marked, parent_vertex):
                return True

    return False


def bfs_main():
    ''' graph = AdjListGraph(13)
    graph = create_graph_one(graph) '''

    graph = AdjListGraph(4)
    graph = create_graph_four(graph)

    marked = [False] * graph.num_of_vertices()
    parent_vertex = -1

    for s in range(graph.num_of_vertices()):
        if not marked[s]:
            if adj_list_bfs_iterative(graph, s, marked, parent_vertex):
                return True

    return False


if __name__ == '__main__':
    print(dfs_main())
    print(bfs_main())

import importlib
G = importlib.import_module('1_graph')
AdjListGraph = getattr(G, 'AdjListGraph')
create_graph_one = getattr(G, 'create_graph_one')
create_graph_five = getattr(G, 'create_graph_five')

from collections import deque as Queue


def adj_list_bfs_iterative(graph, marked, source):
    q = Queue()
    q.append(source)
    marked[source] = True

    while(q):
        s = q.popleft()
        for v in graph.adjacent(s):
            if not marked[v]:
                marked[v] = True
                q.append(v)


def adj_list_dfs_recursive(graph, marked, source):
    marked[source] = True
    for v in graph.adjacent(source):
        if not marked[v]:
            adj_list_dfs_recursive(graph, marked, v)


def is_connected(graph):
    marked = [False] * graph.num_of_vertices()

    for s in range(graph.num_of_vertices()):
        if not marked[s]:
            adj_list_bfs_iterative(graph, marked, s)
            break

    for s in range(graph.num_of_vertices()):
        if not marked[s] and graph.degree(s):
            return False

    return True


def count_odd_vertices(graph):
    count = 0
    for v in range(graph.num_of_vertices()):
        if graph.degree(v) % 2 != 0:
            count += 1

    return count


def main():
    graph = AdjListGraph(7)
    graph = create_graph_five(graph) 

    ''' graph = AdjListGraph(13)
    graph = create_graph_one(graph) '''

    connected = is_connected(graph)
    odd_count = count_odd_vertices(graph)

    # Graph is Eulierian (uses each edge exactly once) if:
    # (a) All vertices excpect 'zero degree' vertices are connected.
    # (b) No. of vertices with 'odd degree' are zero or exactly two.
    if connected and (odd_count == 0 or odd_count == 2):
        if odd_count == 0:
            print('Graph has Euler Cycle')
        else:
            print('Graph has Euler Path')
    else:
        print('Graph is not Eulierian')


if __name__ == '__main__':
    main()

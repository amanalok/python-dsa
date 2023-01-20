import importlib
G = importlib.import_module('1_graph')
AdjListGraph = getattr(G, 'AdjListGraph')
create_graph_one = getattr(G, 'create_graph_one')

from collections import deque as Queue


def adj_list_dfs_recursive(graph, source, marked, id, count):
    marked[source] = True
    id[source] = count
    for v in graph.adjacent(source):
        if not marked[v]:
            adj_list_dfs_recursive(graph, v, marked, id, count)


def adj_list_bfs_iterative(graph, source, marked, id, count):
    q = Queue()
    q.append(source)

    marked[source] = True
    id[source] = count

    while (q):
        v = q.popleft()
        for w in graph.adjacent(v):
            if not marked[w]:
                q.append(w)
                marked[w] = True
                id[w] = count


def dfs_main():
    adj_list_graph_one = AdjListGraph(13)
    adj_list_graph_one = create_graph_one(adj_list_graph_one)

    marked = [None] * adj_list_graph_one.num_of_vertices()
    id = [None] * adj_list_graph_one.num_of_vertices()
    count = 0

    for v in range(adj_list_graph_one.num_of_vertices()):
        if not marked[v]:
            adj_list_dfs_recursive(adj_list_graph_one, v, marked, id, count)
            count += 1

    print('No. of connected components: {}'.format(count))
    print(id)
    print(marked)


def bfs_main():
    adj_list_graph_one = AdjListGraph(13)
    adj_list_graph_one = create_graph_one(adj_list_graph_one)

    marked = [None] * adj_list_graph_one.num_of_vertices()
    id = [None] * adj_list_graph_one.num_of_vertices()
    count = 0

    for v in range(adj_list_graph_one.num_of_vertices()):
        if not marked[v]:
            adj_list_bfs_iterative(adj_list_graph_one, v, marked, id, count)
            count += 1

    print('No. of connected components: {}'.format(count))
    print(id)
    print(marked)


if __name__ == '__main__':
    bfs_main()

import importlib
G = importlib.import_module('1_graph')
AdjListGraph = getattr(G, 'AdjListGraph')
create_graph_one = getattr(G, 'create_graph_one')

from collections import deque as Queue


def adj_list_dfs_recursive(graph, source, marked, edge_to):
    marked[source] = True
    for v in graph.adjacent(source):
        if not marked[v]:
            edge_to[v] = source
            adj_list_dfs_recursive(graph, v, marked, edge_to)

    return marked, edge_to

def adj_list_dfs_iterative(graph, source, marked, edge_to):
    stack = []
    stack.append(source)

    while(stack):
        v = stack.pop()

        if not marked[v]:
            marked[v] = True

        for w in graph.adjacent(v):
            if not marked[w]:
                edge_to[w] = v
                stack.append(w)

    return marked, edge_to


def adj_list_bfs_iteraive(graph, source, marked, edge_to, dist_to):
    q = Queue()
    q.append(source)
    marked[source] = True

    while(q):
        v = q.popleft()
        for w in graph.adjacent(v):
            if not marked[w]:
                q.append(w)
                marked[w] = True
                edge_to[w] = v
                dist_to[w] = dist_to[v] + 1


def adj_list_bfs_recursive(graph, queue, marked, edge_to, dist_to):
    if not(queue):
        return

    v = queue.popleft()
    marked[v] = True

    for w in graph.adjacent(v):
        if not marked[w]:
            queue.append(w)
            marked[w] = True
            edge_to[w] = v
            dist_to[w] = dist_to[v] + 1

    adj_list_bfs_recursive(graph, queue, marked, edge_to, dist_to)



def path_to(s, v, edge_to):

    if edge_to[v] is None:
        return None

    path = []
    start = v
    while (True):
        w = edge_to[start]
        if w == s:
            break

        path.append(w)
        start = w

    path.append(s)
    return path


def dfs_main():
    adj_list_graph_one = AdjListGraph(13)
    adj_list_graph_one = create_graph_one(adj_list_graph_one)

    marked = [False] * adj_list_graph_one.num_of_vertices()
    edge_to = [None] * adj_list_graph_one.num_of_vertices()
    # marked, edge_to = adj_list_dfs_recursive(adj_list_graph_one, 0, marked, edge_to)
    marked, edge_to = adj_list_dfs_iterative(adj_list_graph_one, 0, marked, edge_to)

    print(marked)
    print(edge_to)

    path = path_to(0, 6, edge_to)
    print(path)


def bfs_main():
    adj_list_graph_one = AdjListGraph(13)
    adj_list_graph_one = create_graph_one(adj_list_graph_one)

    marked = [False] * adj_list_graph_one.num_of_vertices()
    edge_to = [None] * adj_list_graph_one.num_of_vertices()
    dist_to = [0] * adj_list_graph_one.num_of_vertices()

    # adj_list_bfs_iteraive(adj_list_graph_one, 0, marked, edge_to, dist_to)

    queue = Queue()
    queue.append(0)
    adj_list_bfs_recursive(adj_list_graph_one, queue, marked, edge_to, dist_to)

    print(marked)
    print(edge_to)

    path = path_to(0, 3, edge_to)
    print(path)



if __name__ == '__main__':
    bfs_main()

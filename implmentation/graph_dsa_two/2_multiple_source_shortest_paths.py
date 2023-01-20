import importlib
DG = importlib.import_module('1_digraph')
AdjListDigraph = getattr(DG, 'AdjListDigraph')
create_digraph_one = getattr(DG, 'create_digraph_one')

from collections import deque as Queue


def bfs(digraph, source_set, marked, edge_to):
    q = Queue()
    for s in source_set:
        q.append(s)

    while(q):
        v = q.popleft()
        marked[v] = True
        for w in digraph.adjacent(v):
            if not marked[w]:
                q.append(w)
                marked[w] = True
                edge_to[w] = v


def shortest_path(edge_to, destination, source_set):
    s_path = []
    s_path.append(destination)

    index = destination
    while(True):
        v = edge_to[index]
        s_path.append(v)

        if v in source_set:
            break

        if v is None:
            return []

        index = v

    return s_path


def print_path(path):
    if not path:
        print('No path available for the destination vertex from any source vertices')
        return

    print(path.pop(), end='')
    while(path):
        v = path.pop()
        print('-{}'.format(v), end='')


def main():
    source_set = set([2, 0, 10])
    destinations = set([4, 5, 12, 1, 7])

    digraph = AdjListDigraph(13)
    digraph = create_digraph_one(digraph)

    marked = [False] * digraph.num_of_vertices()
    edge_to = [None] * digraph.num_of_vertices()
    bfs(digraph, source_set, marked, edge_to)

    print(edge_to)

    for d in destinations:
        print('For vertex {}, shortest path is :'.format(d))
        s_path = shortest_path(edge_to, d, source_set)
        print_path(s_path)
        print('\n')


if __name__ == '__main__':
    main()

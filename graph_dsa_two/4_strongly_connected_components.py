import importlib
DG = importlib.import_module('1_digraph')
AdjListDigraph = getattr(DG, 'AdjListDigraph')
create_digraph_one = getattr(DG, 'create_digraph_one')


def reverse_graph(digraph):
    reversed_digraph = AdjListDigraph(digraph.num_of_vertices())

    for v in range(digraph.num_of_vertices()):
        for w in digraph.adjacent(v):
            reversed_digraph.add_edge(w, v)

    return reversed_digraph


def dfs_post_order(digraph, source, marked, post_order):
    marked[source] = True
    for v in digraph.adjacent(source):
        if not marked[v]:
            dfs_post_order(digraph, v, marked, post_order)

    post_order.append(source)


def dfs_strong_components(digraph, source, marked, id, count):
    marked[source] = True
    id[source] = count

    for v in digraph.adjacent(source):
        if not marked[v]:
            dfs_strong_components(digraph, v, marked, id, count)


def main():
    digraph = AdjListDigraph(13)
    digraph = create_digraph_one(digraph)

    reversed_digraph = reverse_graph(digraph)
    post_order = []
    marked = [False] * reversed_digraph.num_of_vertices()

    for s in range(reversed_digraph.num_of_vertices()):
        if not marked[s]:
            dfs_post_order(reversed_digraph, s, marked, post_order)

    marked = [False] * digraph.num_of_vertices()
    id = [None] * digraph.num_of_vertices()
    count = 0

    while(post_order):
        s = post_order.pop()
        if not marked[s]:
            dfs_strong_components(digraph, s, marked, id, count)
            count += 1

    print(count)
    print(id)


if __name__ == '__main__':
    main()

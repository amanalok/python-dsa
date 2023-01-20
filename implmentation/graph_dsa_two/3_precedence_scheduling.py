import importlib
DG = importlib.import_module('1_digraph')
AdjListDigraph = getattr(DG, 'AdjListDigraph')
create_digraph_two = getattr(DG, 'create_digraph_two')


def reverse_post_order(post_order):
    while(post_order):
        yield post_order.pop()


def dfs(digraph, source, marked, post_order):
    marked[source] = True
    for v in digraph.adjacent(source):
        if not marked[v]:
            dfs(digraph, v, marked, post_order)

    post_order.append(source)


def topological_sort(digraph):
    post_order = []
    marked = [False] * digraph.num_of_vertices()
    for s in range(digraph.num_of_vertices()):
        if not marked[s]:
            dfs(digraph, s, marked, post_order)

    return post_order


def main():
    digraph = AdjListDigraph(7)
    digraph = create_digraph_two(digraph)

    post_order = topological_sort(digraph)

    for vertex in reverse_post_order(post_order):
        print(vertex, end=' ')

    print('\n')


if __name__ == '__main__':
    main()

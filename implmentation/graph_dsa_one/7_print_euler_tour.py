import importlib
G = importlib.import_module('1_graph')
AdjListGraph = getattr(G, 'AdjListGraph')
create_graph_five = getattr(G, 'create_graph_five')
create_graph_six = getattr(G, 'create_graph_six')


def adj_list_dfs_recursive_count(graph, s, marked):
    count = 1
    marked[s] = True
    for v in graph.adjacent(s):
        if not marked[v]:
            count += adj_list_dfs_recursive_count(graph, v, marked)

    return count


def is_valid_edge(graph, s, v):

    # If v is the only adjacent vertex to s
    if graph.degree(s) == 1:
        return True
    # If multiple adjacent vertices, do the following
    else:
        # Count the number of vertices reachable from s
        marked = [False] * graph.num_of_vertices()
        count1 = adj_list_dfs_recursive_count(graph, s, marked)

        # Remove the edge (s, v) and count the vertices reachable from s
        graph.remove_edge(s, v)
        marked = [False] * graph.num_of_vertices()
        count2 = adj_list_dfs_recursive_count(graph, s, marked)

        graph.add_edge(s, v)

        # If count1 > count2, edge (s, v) is a bridge
        return False if count1 > count2 else True


def print_euler_util(graph, source):
    for v in graph.adjacent(source):
        if graph.num_of_edges() == 0:
            break
        if is_valid_edge(graph, source, v):
            print('({}-{})'.format(source, v))
            graph.remove_edge(source, v)
            print_euler_util(graph, v)


def main():
    graph = AdjListGraph(7)
    graph = create_graph_five(graph)

    source_vertex = 0
    for v in range(graph.num_of_vertices()):
        if graph.degree(v) % 2 != 0:
            source_vertex = v
            break

    print_euler_util(graph, source_vertex)


if __name__ == '__main__':
    main()

import importlib
WG = importlib.import_module('1_weighted_graph')
AdjListWeightedGraph = getattr(WG, 'AdjListWeightedGraph')
create_weighted_graph_one = getattr(WG, 'create_weighted_graph_one')

import heapq
from collections import deque as Queue


def find(parent, i):
    if parent[i] == i:
        return i

    return find(parent, parent[i])


def apply_union(id, size, x, y):
    '''
    Function to perform union of the 2 sets x and y.
    Performs union by size.
    '''

    if size[x] < size[y]:
        id[x] = y
        size[y] += size[x]
    else:
        id[y] = x
        size[x] += size[y]


def kruskal_algorithm(weighted_graph, id, size):
    mst = Queue()

    edge_set = weighted_graph.get_edges()
    heapq.heapify(edge_set)

    while(edge_set and (len(mst) < weighted_graph.num_of_vertices() - 1)):
        # Get the edge with the smallest weight
        edge = heapq.heappop(edge_set)

        v = edge.either_vertex()
        w = edge.other_vertex(v)

        # Get the set for each of the vertices
        x = find(id, v)
        y = find(id, w)

        # If edge (v, u) belong to different sets, add it to MST and merge the
        # sets containing v and u
        if x != y:
            mst.append(edge)
            apply_union(id, size, x, y)

    return mst


def main():
    weighted_graph = AdjListWeightedGraph(8)
    weighted_graph = create_weighted_graph_one(weighted_graph)

    id = []
    size = []

    # Create V subsets with single elements
    for vertex in range(weighted_graph.num_of_vertices()):
        id.append(vertex)
        size.append(1)

    mst = kruskal_algorithm(weighted_graph, id, size)

    while(mst):
        edge = mst.popleft()
        print('{}-{}, {}'.format(edge.v, edge.w, edge.weight))


if __name__ == '__main__':
    main()

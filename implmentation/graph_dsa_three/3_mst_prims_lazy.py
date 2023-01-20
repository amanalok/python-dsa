import importlib
WG = importlib.import_module('1_weighted_graph')
AdjListWeightedGraph = getattr(WG, 'AdjListWeightedGraph')
create_weighted_graph_one = getattr(WG, 'create_weighted_graph_one')

from collections import deque as Queue
import heapq


def visit(weighted_graph, source, marked, pq):
    marked[source] = True
    for edge in weighted_graph.adjacent(source):
        v = edge.other_vertex(source)
        if not marked[v]:
            heapq.heappush(pq, edge)


def lazy_mst_prims(weighted_graph):
    mst = Queue()
    pq = []
    marked = [False] * weighted_graph.num_of_vertices()
    s = 0
    visit(weighted_graph, s, marked, pq)

    while(pq and (len(mst) < weighted_graph.num_of_vertices() - 1)):
        edge = heapq.heappop(pq)
        v = edge.either_vertex()
        w = edge.other_vertex(v)

        if marked[v] and marked[w]:
            continue

        mst.append(edge)

        if not marked[v]:
            visit(weighted_graph, v, marked, pq)

        if not marked[w]:
            visit(weighted_graph, w, marked, pq)

    return mst


def main():
    weighted_graph = AdjListWeightedGraph(8)
    weighted_graph = create_weighted_graph_one(weighted_graph)

    mst = lazy_mst_prims(weighted_graph)

    while(mst):
        edge = mst.popleft()
        print('{}-{}, {}'.format(edge.v, edge.w, edge.weight))


if __name__ == '__main__':
    main()

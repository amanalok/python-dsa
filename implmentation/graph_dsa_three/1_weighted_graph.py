class AdjNode:
    def __init__(self, edge):
        self.edge = edge
        self.next = None


class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def either_vertex(self):
        return self.v

    def other_vertex(self, vertex):
        if self.v == vertex:
            return self.w

        return self.v

    def compare_to(self, edge):
        if self.weight < edge.weight:
            return -1
        elif self.weight > edge.weight:
            return 1
        else:
            return 0

    def __lt__(self, edge):
        return self.weight < edge.weight


class AdjListWeightedGraph:
    def __init__(self, num_vertices):
        self.storage = [None] * num_vertices
        self.num_vertices = num_vertices

    def add_edge(self, edge):
        v = edge.either_vertex()
        w = edge.other_vertex(v)

        node1 = AdjNode(edge)
        node1.next = self.storage[v]
        self.storage[v] = node1

        node2 = AdjNode(edge)
        node2.next = self.storage[w]
        self.storage[w] = node2

    def _remove_edge_util(self, v, edge):
        w = edge.other_vertex(v)

        node = self.storage[v]
        if node is None:
            raise Exception('Vertex {} does not have any adjacent vertices'.format(v))

        if node.edge.v == w or node.edge.w == w:
            node = node.next
            self.storage[v] = node
            return

        previous_node = node
        while(node is None):
            if node.edge.v == w or node.edge.w == w:
                previous_node.next = node.next
                return

            previous_node = node
            node = node.next

        raise Exception('Edge ({}, {}) not present'.format(v, w))


    def remove_edge(self, edge):
        v = edge.either_vertex()
        w = edge.other_vertex(v)

        self._remove_edge_util(v, edge)
        self._remove_edge_util(w, edge)

    def adjacent(self, v):
        adjacent_edges = []

        node = self.storage[v]
        while(node is not None):
            adjacent_edges.append(node.edge)
            node = node.next

        return adjacent_edges

    def num_of_vertices(self):
        return self.num_vertices

    def num_of_edges(self):
        num_edges = 0
        for v in range(self.num_of_vertices()):
            for _ in self.adjacent(v):
                num_edges += 1

        return num_edges / 2

    def degree(self, v):
        count = 0
        for _ in self.adjacent(v):
            count += 1

        return count

    def max_degree(self):
        max = 0
        for v in range(self.num_of_vertices()):
            d = self.degree(v)
            if d > max:
                max = d

        return max

    def average_degree(self):
        return 2 * self.num_of_edges() / self.num_of_vertices()

    def num_of_self_loops(self):
        count = 0
        for v in range(self.num_of_vertices()):
            adjacent_vertices = self.adjacent(v)
            if v in adjacent_vertices:
                count += 1

        return count

    def get_edges(self):
        edge_list = []
        for v in range(self.num_of_vertices()):
            node = self.storage[v]
            while(node is not None):
                edge_list.append(node.edge)
                node = node.next

        edge_set = set(edge_list)
        return list(edge_set)


def create_weighted_graph_one(weighted_graph):
    for u, v, weight in [(0, 7, 0.16), (2, 3, 0.17), (1, 7, 0.19), (0, 2, 0.26),
                        (5, 7, 0.28), (1, 3, 0.29), (1, 5, 0.32), (2, 7, 0.34),
                        (4, 5, 0.35), (1, 2, 0.36), (4, 7, 0.37), (0, 4, 0.38),
                        (6, 2, 0.40), (3, 6, 0.52), (6, 0, 0.58), (6, 4, 0.93)]:
        edge = Edge(u, v, weight)
        weighted_graph.add_edge(edge)

    return weighted_graph


if __name__ == '__main__':
    weighted_graph_one = AdjListWeightedGraph(8)
    weighted_graph_one = create_weighted_graph_one(weighted_graph_one)

    for v in [6, 4, 2]:
        print('Following are the vertices adjacent to {}'.format(v))
        print(weighted_graph_one.adjacent(v))

    print('Number of vertices in the weighted graph: {}'.format(weighted_graph_one.num_of_vertices()))
    print('Number of edges in the weighted graph: {}'.format(weighted_graph_one.num_of_edges()))
    print('Max Degree: {}'.format(weighted_graph_one.max_degree()))
    print('Average Degree: {}'.format(weighted_graph_one.average_degree()))
    print('No. of self loops: {}'.format(weighted_graph_one.num_of_self_loops()))
    print('Following are the edges in the weighted graph:')
    for edge in weighted_graph_one.get_edges():
        print('{}-{}, {}'.format(edge.v, edge.w, edge.weight))

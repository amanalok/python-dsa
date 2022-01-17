class AdjNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class AdjListDigraph:

    def __init__(self, num_vertices):
        self.storage = [None] * num_vertices
        self.num_vertices = num_vertices

    def add_edge(self, v, w):
        node = AdjNode(w)
        node.next = self.storage[v]
        self.storage[v] = node

    def remove_edge(self, v, w):
        if self.storage[v] is None:
            raise Exception('No adjacent vertices present for {}'.format(v))

        node = self.storage[v]
        if node.value == w:
            self.storage[v] = node.next
            return

        previous_node = node
        while(node is not None):
            if node.value == w:
                previous_node.next = node.next
                return

            previous_node = node
            node = node.next

        raise Exception('No adjacent vertex {} present for {}'.format(w, v))

    def adjacent(self, v):
        adjacent_vertices = []
        node = self.storage[v]

        while(node is not None):
            adjacent_vertices.append(node.value)
            node = node.next

        return adjacent_vertices

    def num_of_vertices(self):
        return self.num_vertices

    def num_of_edges(self):
        num_edges = 0
        for v in range(self.num_vertices):
            for _ in self.adjacent(v):
                num_edges += 1

        return num_edges

    def degree(self, v):
        count = 0
        for _ in self.adjacent(v):
            count += 1

        return count

    def max_out_degree(self):
        max = 0
        for v in range(self.num_vertices):
            d = self.degree(v)
            if d > max:
                max = d

        return max

    def average_out_degree(self):
        return self.num_of_edges() / self.num_of_vertices()

    def num_of_self_loops(self):
        count = 0
        for v in range(self.num_vertices):
            adjacent_vertices = self.adjacent(v)
            if v in adjacent_vertices:
                count += 1

        return count


def create_digraph_one(digraph):
    for v, w in [(0, 1), (0, 5), (2, 0), (2, 3), (3, 2), (3, 5), (4, 2), (4, 3),
                (5, 4), (6, 0), (6, 4), (6, 8), (6, 9), (7, 6), (7, 9), (8, 6),
                (9, 10), (9, 11), (10, 12), (11, 4), (11, 12), (12, 9)]:
        digraph.add_edge(v, w)

    return digraph


def create_digraph_two(digraph):
    for v, w in [(0, 1), (0, 2), (0, 5), (1, 4), (3, 2), (3, 4),
                (3, 5), (3, 6), (5, 2), (6, 0), (6, 4)]:
        digraph.add_edge(v, w)

    return digraph


if __name__ == '__main__':
    digraph_one = AdjListDigraph(13)
    digraph_one = create_digraph_one(digraph_one)

    for v in [9, 4, 12]:
        print('Following are the vertices adjacent to {}'.format(v))
        print(digraph_one.adjacent(v))

    print('Number of vertices in the digraph: {}'.format(digraph_one.num_of_vertices()))
    print('Number of edges in the digraph: {}'.format(digraph_one.num_of_edges()))
    print('Max Degree: {}'.format(digraph_one.max_out_degree()))
    print('Average Degree: {}'.format(digraph_one.average_out_degree()))
    print('No. of self loops: {}'.format(digraph_one.num_of_self_loops()))

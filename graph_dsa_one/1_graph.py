class AdjNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class AdjListGraph:

    def __init__(self, num_vertices):
        self.storage = [None] * num_vertices
        self.num_vertices = num_vertices

    def add_edge(self, v, w):
        new_adj_node = AdjNode(w)
        new_adj_node.next = self.storage[v]
        self.storage[v] = new_adj_node

        new_adj_node = AdjNode(v)
        new_adj_node.next = self.storage[w]
        self.storage[w] = new_adj_node

    def adjacent(self, v):
        adjacent_vertices = []
        node = self.storage[v]
        while (node is not None):
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

        return num_edges / 2

    def degree(self, v):
        count = 0
        for _ in self.adjacent(v):
            count += 1

        return count

    def max_degree(self):
        max = 0
        for v in range(self.num_vertices):
            d = self.degree(v)
            if d > max:
                max = d

        return max

    def average_degree(self):
        return 2 * self.num_of_edges() / self.num_of_vertices()

    def num_of_self_loops(self):
        count = 0
        for v in range(self.num_vertices):
            for w in self.adjacent(v):
                if v == w:
                    count += 1

        return count

    def _remove_edge_util(self, v, w):
        node = self.storage[v]
        if node is None:
            return

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


    def remove_edge(self, v, w):
        self._remove_edge_util(v, w)
        self._remove_edge_util(w, v)



class AdjMatrixGraph:

    def __init__(self, num_vertices):
        self.storage = []
        for i in range(num_vertices):
            self.storage.append([0 for j in range(num_vertices)])

        self.num_vertices = num_vertices

    def add_edge(self, v, w):
        self.storage[v][w] = 1
        self.storage[w][v] = 1

    def adjacent(self, v):
        adjacent_vertices = []
        for index in range(self.num_vertices):
            if self.storage[v][index] == 1:
                adjacent_vertices.append(index)

        return adjacent_vertices

    def num_of_vertices(self):
        return self.num_vertices

    def num_of_edges(self):
        num_edges = 0
        for v in range(self.num_vertices):
            for w in range(self.num_vertices):
                if self.storage[v][w]:
                    num_edges += 1

        return num_edges / 2

    def degree(self, v):
        count = 0
        for index in range(self.num_vertices):
            if self.storage[v][index] == 1:
                count += 1

        return count

    def max_degree(self):
        max = 0
        for v in range(self.num_vertices):
            d = self.degree(v)
            if d > max:
                max = d

        return max

    def average_degree(self):
        return 2 * self.num_of_edges() / self.num_of_vertices()

    def num_of_self_loops(self):
        count = 0
        for v in range(self.num_vertices):
            if self.storage[v][v] == 1:
                count += 1

        return count


def create_graph_one(graph):
    '''
    This method creates an undirected graph with 3 connected components.
    '''
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 5)
    graph.add_edge(0, 6)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(7, 8)
    graph.add_edge(9, 10)
    graph.add_edge(9, 11)
    graph.add_edge(9, 12)
    graph.add_edge(11, 12)

    return graph


def create_graph_two(graph):
    for v, w in [(0, 1), (0, 2), (0, 5), (1, 2),
                (2, 3), (2, 4), (3, 4), (3, 5)]:
        graph.add_edge(v, w)

    return graph


def create_graph_three(graph):
    '''
    This method creates a Bi-partite graph.
    '''
    for v, w in [(0, 1), (0, 2), (0, 5), (0, 6), (1, 3),
                (2, 3), (2, 4), (4, 5), (4, 6)]:
        graph.add_edge(v, w)

    return graph


def create_graph_four(graph):
    for v, w in [(0, 1), (0, 2), (1, 3)]:
        graph.add_edge(v, w)

    return graph


def create_graph_five(graph):
    '''
    This method creates a graph with a Euler Cycle
    '''
    for v, w in [(0, 1), (0, 2), (0, 5), (0, 6), (1, 2),
                (2, 3), (2, 4), (3, 4), (4, 5), (4, 6)]:
        graph.add_edge(v, w)

    return graph


def create_graph_six(graph):
    '''
    This method creates a graph with Euler Path
    '''
    for v, w in [(0, 1), (0, 2), (1, 2), (2, 3)]:
        graph.add_edge(v, w)

    return graph


if __name__ == '__main__':
    print('*** Adjacency List Graph One ***')

    adj_list_graph_one = AdjListGraph(13)
    adj_list_graph_one = create_graph_one(adj_list_graph_one)

    for v in [3, 9, 1]:
        print(adj_list_graph_one.adjacent(v))
        print(adj_list_graph_one.degree(v))

    print(adj_list_graph_one.num_of_vertices())
    print(adj_list_graph_one.num_of_edges())
    print(adj_list_graph_one.average_degree())
    print(adj_list_graph_one.max_degree())

    print('\n*** Adjacency Matrix Graph One ***')

    adj_mat_graph_one = AdjMatrixGraph(13)
    adj_mat_graph_one = create_graph_one(adj_mat_graph_one)

    for v in [3, 9, 1]:
        print(adj_mat_graph_one.adjacent(v))
        print(adj_mat_graph_one.degree(v))

    print(adj_mat_graph_one.num_of_vertices())
    print(adj_mat_graph_one.num_of_edges())
    print(adj_mat_graph_one.average_degree())
    print(adj_mat_graph_one.max_degree())

    print('*** Adjacency List Graph Two ***')

    adj_list_graph_two = AdjListGraph(6)
    adj_list_graph_two = create_graph_two(adj_list_graph_two)

    for v in [3, 5, 1]:
        print(adj_list_graph_two.adjacent(v))
        print(adj_list_graph_two.degree(v))

    print(adj_list_graph_two.num_of_vertices())
    print(adj_list_graph_two.num_of_edges())
    print(adj_list_graph_two.average_degree())
    print(adj_list_graph_two.max_degree())

    print('\n*** Adjacency Matrix Graph Two ***')

    adj_mat_graph_two = AdjMatrixGraph(6)
    adj_mat_graph_two = create_graph_two(adj_mat_graph_two)

    for v in [3, 5, 1]:
        print(adj_mat_graph_two.adjacent(v))
        print(adj_mat_graph_two.degree(v))

    print(adj_mat_graph_two.num_of_vertices())
    print(adj_mat_graph_two.num_of_edges())
    print(adj_mat_graph_two.average_degree())
    print(adj_mat_graph_two.max_degree())

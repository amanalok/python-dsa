class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        current_node = self.tail.next

        nodes = []
        while(current_node):
            nodes.append(current_node.data)
            current_node = current_node.next
            if current_node == self.tail.next:
                break

        return '->'.join(nodes)

    def _add_to_empty(self, data):
        if self.tail is not None:
            raise Exception('Circular linked list is not empty !!!')

        new_node = Node(data)
        self.tail = new_node
        self.tail.next = self.tail
        return

    def add_front(self, data):

        if self.tail is None:
            return self._add_to_empty(data)

        new_node = Node(data)
        new_node.next = self.tail.next
        self.tail.next = new_node
        return

    def add_end(self, data):

        if self.tail is None:
            return self._add_to_empty(data)

        new_node = Node(data)
        new_node.next = self.tail.next
        self.tail.next = new_node
        self.tail = new_node
        return

    def add_after(self, target_node_data, new_node_data):

        if self.tail is None:
            raise Exception('Circular linked list is empty !!!')

        current_node = self.tail.next
        while (current_node):
            if current_node.data == target_node_data:
                if current_node == self.tail:
                    return self.add_end(new_node_data)

                new_node = Node(new_node_data)
                new_node.next = current_node.next
                current_node.next = new_node
                return

            current_node = current_node.next
            if current_node == self.tail.next:
                break

        raise Exception(
            'Node with data {} not found in circular linked list'.format(target_node_data))

    def add_before(self, target_node_data, new_node_data):

        if self.tail is None:
            raise Exception('Circular linked list is empty !!!')

        current_node = self.tail.next
        if current_node.data == target_node_data:
            return self.add_front(new_node_data)

        previous_node = current_node
        while(current_node):
            current_node = current_node.next
            if current_node == self.tail.next:
                break

            if current_node.data == target_node_data:
                new_node = Node(new_node_data)
                new_node.next = current_node
                previous_node.next = new_node
                return

            previous_node = previous_node.next

        raise Exception(
            'Node with data {} not found in circular linked list'.format(target_node_data))

    def delete_node(self, target_node_data):

        if self.tail is None:
            raise Exception('Circular linked list is empty !!!')

        current_node = self.tail.next
        if current_node.data == target_node_data:
            self.tail.next = current_node.next
            current_node = None
            return

        previous_node = current_node
        while (current_node):
            current_node = current_node.next
            if current_node == self.tail.next:
                break

            if current_node.data == target_node_data:
                previous_node.next = current_node.next
                if current_node == self.tail:
                    self.tail = previous_node
                current_node = None
                return

            previous_node = previous_node.next

        raise Exception(
            'Node with data {} not found in circular linked list'.format(target_node_data))



def circular_linked_list():
    cll = CircularLinkedList()
    cll.add_end('3')
    cll.add_front('5')
    cll.add_end('8')
    cll.add_front('2')
    cll.add_end('6')
    print(cll)

    cll.add_after('2', '11')
    cll.add_after('6', '9')
    cll.add_after('5', '7')
    print(cll)

    cll.add_before('2', '40')
    cll.add_before('9', '73')
    cll.add_before('7', '16')
    print(cll)

    cll.delete_node('16')
    print(cll)
    cll.delete_node('9')
    print(cll)
    cll.delete_node('40')
    print(cll)
    cll.delete_node('373')


if __name__ == '__main__':
    circular_linked_list()

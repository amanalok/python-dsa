class Node:

    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):
        current_node = self.head

        nodes = []
        while (current_node is not None):
            nodes.append(current_node.data)
            current_node = current_node.next

        forward_pass =  '->'.join(nodes + ['None'])
        backward_pass = '<-'.join(['None'] + nodes)

        return '{}\n{}\n'.format(forward_pass, backward_pass)

    def add_front(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while (current_node is not None):
            if current_node.next is None:
                current_node.next = new_node
                new_node.prev = current_node
                return

            current_node = current_node.next

    def add_after(self, target_node_data, new_node_data):
        if self.head is None:
            raise Exception('Doubly linked list is empty !!!')

        current_node = self.head
        while (current_node is not None):
            if current_node.data == target_node_data:
                new_node = Node(new_node_data)

                if current_node.next is None:
                    current_node.next = new_node
                    new_node.prev = current_node
                    return


                new_node.next = current_node.next
                current_node.next.prev = new_node
                current_node.next = new_node
                new_node.prev = current_node
                return

            current_node = current_node.next

        raise Exception('Target Node not found in doubly linked list')

    def add_before(self, target_node_data, new_node_data):
        if self.head is None:
            raise Exception('Doubly linked list is empty !!!')

        if self.head.data == target_node_data:
            self.add_front(new_node_data)
            return

        current_node = self.head.next
        while (current_node is not None):
            if current_node.data == target_node_data:
                new_node = Node(new_node_data)
                new_node.next = current_node
                current_node.prev.next = new_node
                new_node.prev = current_node.prev
                current_node.prev = new_node
                return
            current_node = current_node.next

        raise Exception('Target Node not found in doubly linked list')

    def delete_node(self, target_node_data):
        if self.head is None:
            raise Exception('Doubly linked list is empty !!!')

        if self.head.data == target_node_data:
            temp = self.head
            self.head = self.head.next
            temp = None
            return

        current_node = self.head.next
        while (current_node is not None):
            if current_node.data == target_node_data:
                if current_node.next is None:
                    temp = current_node
                    current_node.prev.next = None
                    temp = None
                    return

                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                current_node = None
                return
            current_node = current_node.next

        raise Exception('Target Node not found in doubly linked list')


def doubly_linked_list():
    dbl_llist = DoublyLinkedList()

    dbl_llist.add_end('5')
    dbl_llist.add_front('1')
    dbl_llist.add_front('6')
    dbl_llist.add_end('9')
    print(dbl_llist)

    dbl_llist.add_after('5', '11')
    dbl_llist.add_after('1', '15')
    print(dbl_llist)

    dbl_llist.add_before('9', '13')
    dbl_llist.add_before('15', '45')
    print(dbl_llist)

    dbl_llist.delete_node('1')
    print(dbl_llist)

    dbl_llist.delete_node('9')
    print(dbl_llist)


if __name__ == '__main__':
    doubly_linked_list()

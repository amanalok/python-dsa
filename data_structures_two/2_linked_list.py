class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def __repr__(self):
        current = self.front
        nodes = []
        while (current is not None):
            nodes.append(current.data)
            current = current.next

        nodes.append('None')
        return '->'.join(nodes)

    def __iter__(self):
        current = self.front
        while (current is not None):
            yield current
            current = current.next

    def add_front(self, data):
        node = Node(data)
        node.next = self.front

        if (self.front is None and self.rear is None):
            self.front = node
            self.rear = node
        else:
            self.front = node

    def add_rear(self, data):
        node = Node(data)

        if (self.front is None and self.rear is None):
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def add_after(self, target_node_data, new_node_data):
        if self.front is None:
            raise('Linked List is empty !!!')

        for node in self:
            if node.data == target_node_data:
                if node.next is None:
                    return self.add_rear(new_node_data)
                else:
                    new_node = Node(new_node_data)
                    new_node.next = node.next
                    node.next = new_node
                    return

        raise Exception('Node with data {} not found in linked list'
                        .format(target_node_data))

    def add_before(self, target_node_data, new_node_data):
        if self.front == None:
            raise Exception('Linked List is empty')

        if self.front.data == target_node_data:
            return self.add_front(new_node_data)

        previous_node = self.front
        for node in self:
            if node.data == target_node_data:
                new_node = Node(new_node_data)
                new_node.next = node
                previous_node.next = new_node
                return
            previous_node = node

        raise Exception('Node with data {} not found in linked list'
                        .format(target_node_data))

    def remove_node(self, target_node_data):
        if self.front is None:
            raise Exception('Linked List is empty')

        if self.front.data == target_node_data:
            self.front = self.front.next
            return

        previous_node = self.front
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception('Node with data {} not found in linked list'
                        .format(target_node_data))

    def reverse(self):
        if self.front is None:
            raise Exception('Linked list is empty')

        # self.rear = self.front
        prev_node = None
        current_node = self.front
        while (current_node is not None):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.front = prev_node

    def sort(self):
        if self.front is None:
            raise Exception('Linked list is empty')

        for node in self:
            next_node = node.next
            while next_node is not None:
                if node.data > next_node.data:
                    node.data, next_node.data = next_node.data, node.data

                next_node = next_node.next



def singly_single_list():
    llist = LinkedList()
    foo = 0
    for item in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']:
        if foo % 2 == 0:
            llist.add_front(item)
        else:
            llist.add_rear(item)

        foo += 1
        print(llist)

    llist.add_after('j', 'o')
    llist.add_after('a', 'k')
    llist.add_after('f', 'f')
    llist.add_after('i', 'n')
    llist.add_rear('m')
    print(llist)

    llist.add_before('i', 'z')
    llist.add_before('z', 'y')
    llist.add_before('n', 'p')
    llist.add_before('m', 'q')
    # llist.add_before('x', 'u')
    print(llist)

    llist.remove_node('y')
    llist.remove_node('m')
    llist.remove_node('a')
    print(llist)

    print('*** Reversing linked list ***')
    llist.reverse()
    print(llist)

    llist.sort()
    print('*** Sorted linked list ***')
    print(llist)



if __name__ == '__main__':
    singly_single_list()

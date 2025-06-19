class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None
    
    def insert_at_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
            return True
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

        return True

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return True
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

        return True

    def insert_at_k(self, k_index, data):
        if k_index == 0:
            self.insert_at_head(data)
            return True

        if self.is_empty():
            return False
        
        current = self.head
        for _ in range(k_index):
            if current is None:
                return False
            current = current.next

        if current.next is None:
            self.insert_at_tail(data)
            return True
        
        new_node = Node(data)
        new_node.next = current.next
        current.next.prev = new_node
        new_node.prev = current
        current.next = new_node

        return True
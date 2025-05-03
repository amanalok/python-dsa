class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_k(self, k_index, data):
        if k_index == 0:
            self.insert_at_head(data)
            return
        
        if self.is_empty():
            return
        
        current = self.head
        for _ in range(k_index - 1):
            if current.next is None:
                return
            current = current.next
        
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def insert_at_tail(self, data):
        if self.is_empty():
            self.insert_at_head(data)
            return

        current = self.head
        while current.next:
            current = current.next
        
        new_node = Node(data)
        current.next = new_node

    def delete_at_head(self):
        if self.is_empty():
            return
        
        temp_node = self.head
        self.head = self.head.next

        del temp_node

    def delete_by_value(self, value):
        if self.is_empty():
            return
        
        current = self.head
        previous = self.head
        while current:
            if current.data == value:
                break
            if current != previous:
                previous = previous.next
            
            current = current.next

        if not current:
            return
        
        if current == previous:
            self.delete_at_head()
        else:
            previous.next = current.next
            del current

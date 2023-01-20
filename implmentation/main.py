import importlib
l = importlib.import_module('data_structures_two.2_linked_list')
LinkedList = getattr(l, 'LinkedList')

import heapq as hq

class CircularQueue:
    def __init__(self, capacity) -> None:
        self.data_store = [None] * capacity
        self.front = -1
        self.rear = -1
        self.capacity = capacity

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def size(self):
        if self.is_empty():
            return 0
        elif self.front <= self.rear:
            return (self.rear - self.front) + 1
        else:
            return (self.capacity - self.front) + (self.rear + 1)

    def enqueue(self, item):
        if self.is_full():
            raise Exception('CQ is full')

        if self.is_empty():
            self.front = 0
            self.rear = 0
        elif self.rear + 1 == self.capacity:
            self.rear = 0
        else:
            self.rear += 1

        self.data_store[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise Exception('CQ is empty')

        item = self.data_store[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.front + 1 == self.capacity:
            self.front = 0
        else:
            self.front += 1

        return item

    def display(self):
        if self.is_empty():
            raise Exception('CQ is empty')

        if self.front <= self.rear:
            print(self.data_store[self.front:self.rear+1])
        else:
            front_data = self.data_store[self.front:self.capacity]
            rear_data = self.data_store[0:self.rear+1]
            front_data.extend(rear_data)
            print(front_data)


# Driver Code
if __name__ == '__main__':

    ob = CircularQueue(5)
    ob.enqueue(14)
    ob.enqueue(22)
    ob.enqueue(13)
    ob.enqueue(-6)
    ob.display()
    print ("\nDeleted value = ", ob.dequeue())
    print ("\nDeleted value = ", ob.dequeue())
    ob.display()
    ob.enqueue(9)
    ob.enqueue(20)
    ob.enqueue(5)
    ob.display()
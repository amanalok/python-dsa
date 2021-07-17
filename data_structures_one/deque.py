class DequeWithList:
    def __init__(self):
        self.storage = []
        self.len = 0

    def is_empty(self):
        return self.len == 0

    def enqueue_front(self, data):
        self.storage.insert(0, data)
        self.len += 1

    def enqueue_rear(self, data):
        self.storage.append(data)
        self.len += 1

    def dequeue_front(self):
        return self.storage.pop(0)
        self.len -= 1

    def dequeue_rear(self):
        return self.storage.pop()
        self.len -= 1

    def size():
        return self.len



class Deque:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1

    def is_full(self):
        full_cond_1 = (self.front == 0 and self.rear+1 == self.capacity)
        full_cond_2 = (self.front == self.rear + 1)
        return (full_cond_1 or full_cond_2)

    def is_empty(self):
        return self.front == -1

    def add_front(self, data):
        if self.is_full():
            raise Exception('Deque is already full !!!')

        if self.front == -1:
            self.front = 0
            self.rear = 0
        elif self.front == 0:
            self.front = self.capacity - 1
        else:
            self.front -= 1

        self.storage[self.front] = data

    def delete_front(self):
        if self.is_empty():
            raise Exception('Deque is empty !!!')

        data = self.storage[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.front == self.capacity - 1:
            self.front = 0
        else:
            self.front += 1

    def add_rear(self, data):
        if self.is_full():
            raise Exception('Deque is full !!!')

        if self.front == -1:
            self.front = 0
            self.rear = 0
        elif self.rear == self.capacity - 1:
            self.rear = 0
        else:
            self.rear += 1

        self.storage[self.rear] = data

    def delete_rear(self):
        if self.is_empty():
            raise Exception('Deque is empty !!!')

        data = self.storage[self.rear]

        if self.rear == self.front:
            self.front = -1
            self.rear = -1
        elif self.rear == 0:
            self.rear = self.capacity - 1
        else:
            self.rear -= 1

    def display(self):
        if self.is_empty():
            raise Exception('Deque is empty')
        print('Following are the elements of Deque: ', end='')
        if self.front == self.rear:
            print(self.storage[:self.front+1])
        else:
            front = self.storage[self.front:self.capacity]
            rear = self.storage[0:self.rear+1]
            front.extend(rear)
            print(front)

    def size(self):
        if self.front == -1:
            return 0
        elif self.front == self.rear:
            return 1
        else:
            front_size = self.capacity - self.front
            rear_size = self.rear + 1
            return front_size + rear_size



def deque_main():
    dq = Deque(10)
    print(dq.size())
    for item in ['a', 'b', 'c', 'd', 'e']:
        dq.add_front(item)
        dq.display()
        print('Front: {}, Rear: {}, Size: {}'.format(dq.front, dq.rear, dq.size()))

    for item in ['f', 'g', 'h', 'i', 'j']:
        dq.add_rear(item)
        dq.display()
        print('Front: {}, Rear: {}, Size: {}'.format(dq.front, dq.rear, dq.size()))


if __name__ == '__main__':
    deque_main()

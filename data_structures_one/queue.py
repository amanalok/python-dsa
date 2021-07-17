class QueueWithList:

    def __init__(self):
        self.queue = []
        self.len = -1

    def enqueue(self, item):
        self.queue.append(item)
        self.len += 1

    def dequeue(self):
        if self.len == -1:
            return None

        self.len -= 1
        return self.queue.pop(0)

    def is_empty(self):
        return self.len == -1

    def peek(self):
        if self.len == -1:
            print('Queue is empty!!!', end=' ')
            return

        return self.queue[0]

    def size(self):
        return self.len + 1

    def display(self):
        print(self.queue)



class Queue:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.front == 0) and (self.rear+1 == self.capacity)

    def enqueue(self, data):
        if self.is_full():
            raise Exception('Queue is already full')

        if self.is_empty():
            self.front = 0
            self.rear = 0
            self.storage[self.rear] = data
        else:
            self.rear += 1
            self.storage[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')

        data = self.storage[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

        return data

    def size(self):
        if self.is_empty():
            return 0
        elif self.front == self.rear:
            return 1
        else:
            return 1 + self.rear - self.front

    def display(self):
        if self.is_empty():
            raise Exception('Queue is empty. No elements to display!!!')

        print('Following are the elements in the queue: ', end=' ')
        print(self.storage[self.front:self.rear+1])



def queue_main():
    q = Queue(10)

    print('Size of queue: {}'.format(q.size()))

    for data in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']:
    # for data in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']:
        q.enqueue(data)
        q.display()
        print('Size: {}'.format(q.size()))

    print('Sequence of dequeued items are: ', end = '')
    # for i in range(0, 11):
    while (not q.is_empty()):
        data = q.dequeue()
        print(data, end=' ')



if __name__ == '__main__':
    queue_main()

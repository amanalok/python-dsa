class Queue:

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

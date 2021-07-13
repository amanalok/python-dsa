class SizedCircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1

    def enqueue(self, item):

        if (self.tail+1) % self.size == self.head:
            print('The circular queue is full')
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item
        else:
            self.tail = (self.tail+1) % self.size
            self.queue[self.tail] = item

    def dequeue(self):

        if self.head == -1:
            print('The circular queue is empty')
        elif self.head == self.tail:
             temp = self.queue[self.head]
             self.head = -1
             self.tail = -1
             return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head+1) % self.size
            return temp

    def display(self):

        if self.head == -1:
            print('The circular queue is empty')
        elif self.tail >= self.head:
            print('\nElements in the circular queue are:', end=' ')
            for i in range(self.head, self.tail+1):
                print(self.queue[i], end=' ')
        else:
            print('\nElements in the circular queue are :', end=' ')
            for i in range(self.head, self.size):
                print(self.queue[i], end=' ')
            for i in range(0, self.tail+1):
                print(self.queue[i], end=' ')


# Driver Code
if __name__ == '__main__':

    ob = SizedCircularQueue(5)
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

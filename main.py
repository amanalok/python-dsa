from data_structures_one.stack import Stack
from data_structures_one.queue import Queue

def stack_implement():
    stack = Stack()
    print('Top Element: {}'.format(stack.peek()))
    print('Length of stack: {}'.format(stack.size()))

    for i in range(1, 5):
        stack.push(i)

    stack.display()

    print('Top Element: {}'.format(stack.peek()))
    print('Length of stack: {}'.format(stack.stack_length()))

    for i in range(1, 3):
        print('Popped Element: {}'.format(stack.pop()))

    print('Length of stack: {}'.format(stack.stack_length()))
    print('Top Element: {}'.format(stack.peek()))

    len_s = stack.stack_length()
    print('Length of stack: {}'.format(len_s))

def queue_implement():
    queue = Queue()
    print('First Element: {}'.format(queue.peek()))
    print('Length of queue: {}'.format(queue.size()))

    for i in range(1, 6):
        queue.enqueue(i)

    print('First Element: {}'.format(queue.peek()))
    queue.display()

    for i in range(3):
        print('Dequeued {}'.format(queue.dequeue()))

    print('First Element: {}'.format(queue.peek()))
    print('Length of queue: {}'.format(queue.size()))


if __name__ == '__main__':
    queue_implement()

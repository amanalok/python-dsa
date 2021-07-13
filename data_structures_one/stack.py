class StackWithList:

    def __init__(self):
        self.stack = []
        self.len = -1

    def push(self, item):
        self.stack.append(item)
        self.len += 1

    def pop(self):
        if self.len == -1:
            return None

        self.len -= 1
        return self.stack.pop()

    def is_empty(self):
        return self.len == -1

    def peek(self):
        if self.is_empty():
            print('Stack is empty!!!', end=' ')
            return

        return self.stack[self.len]

    def size(self):
        return self.len + 1

    def display(self):
        print(self.stack)



class Stack:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def push(self, data):
        if self.is_full():
            raise('Stack is already full')

        self.storage[self.size] = data
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise('Stack is empty')

        data = self.storage[self.size-1]
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise('Stack is empty')

        return self.storage[self.size-1]

    def size(self):
        return self.size

    def display(self):
        print('Following are the elements in the Stack: ', end='')
        print(self.storage[:self.size])



def stack_main():
    st = Stack(10)
    st.push('a')
    st.push('b')
    st.push('c')

    st.display()

    print('Top element: {}'.format(st.peek()))

    print('Popped element sequence: ', end='')
    while(not st.is_empty()):
        print(st.pop(), end= ' ')


if __name__ == '__main__':
    stack_main()

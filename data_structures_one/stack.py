class Stack:

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

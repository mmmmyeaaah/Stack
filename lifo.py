class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def pop(self):
        if self.stack == []:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)   
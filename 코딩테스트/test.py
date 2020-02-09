import queue

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):

        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
    def is_empty(self):
        if len(self.stack) == 0:
            return 1
        return 0

q = queue.Queue()
q.put("aa")
q.put("bb")

s = Stack()
s.push("tet")
print(s.pop())

a = q.get()
print(a)


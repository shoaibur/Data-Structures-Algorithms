class Stack(object):
    def __init__(self):
        self.stack = []
      
    def push(self, value):
        self.stack.append(value)
      
    def pop(self):
        self.stack.pop()
# Create a stack
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.stack) # [1, 2, 3]
s.pop()
print(s.tack) # [1, 2]

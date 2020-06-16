class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, value): # O(1)
        self.stack.append(value)
        
    def pop(self): # O(1)
        return self.stack.pop()
    
# Test
s = Stack()
nums = [1,2,3,4]
for num in nums:
    s.push(num)
print('stack:', s.stack)
print('pop:', s.pop())
print('stack:', s.stack)

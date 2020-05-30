def min_stack(stack):
    minn = stack.pop()
    while stack:
        minn = min(minn, stack.pop())
    return minn
    
# Test script
nums = [1,2,3,4,3,1]
stack = Stack()
for num in nums:
    stack.push(num)
    
# Stack class
class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop()
 

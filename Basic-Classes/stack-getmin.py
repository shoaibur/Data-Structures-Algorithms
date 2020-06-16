class GetMinStack:
    def __init__(self):
        self.stack = []
        self.min = float('inf')
        
    def push(self, value):
        if len(self.stack) == 0:
            self.stack.append(value)
            self.min = value
        elif value >= self.min:
            self.stack.append(value)
        else:
            self.stack.append(2*value-self.min)
            self.min = value
    
    def pop(self):
        if len(self.stack) == 0:
            self.min = float('inf')
        else:
            p = self.stack.pop()
            if p < self.min:
                self.min = 2*self.min - p
            return p
        
    def getmin(self):
        return self.min

# Tests
s = GetMinStack()
nums = [8,9,6,3,7]
print('original:', nums)
for num in nums:
    s.push(num)
for i in range(5):
    s.pop()
    print( f'pop & getmin: {s.getmin()}')

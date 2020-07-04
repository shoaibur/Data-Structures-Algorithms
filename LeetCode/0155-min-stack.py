class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack:
            self.minstack.append(x)
        else:
            self.minstack.append( min(self.minstack[-1], x) )

    def pop(self) -> None:
        self.minstack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minstack: return []
        return self.minstack[-1]

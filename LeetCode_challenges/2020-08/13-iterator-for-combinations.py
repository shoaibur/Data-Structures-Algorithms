class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        # self.combinations = itertools.combinations(characters, combinationLength)
        # self.combinations = [''.join(t) for t in self.combinations]
        # self.pointer = -1
        
        self.combinations = []
        self.pointer = -1
        
        q = collections.deque()
        q.append(('', 0))
        while q:
            temp, curr = q.popleft()
            if len(temp) == combinationLength:
                self.combinations.append(temp)
                
            for i in range(curr, len(characters)):
                q.append((temp+characters[i], i+1))
        

    def next(self) -> str:
        if self.hasNext():
            self.pointer += 1
            return self.combinations[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer + 1 < len(self.combinations)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

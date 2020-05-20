class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
#         
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        '''Append a value at the end of the list'''
        if self.head is None:
            self.head = Node(value)
            return
        tail = head
        while tail.next:
            tail = tail.next
        tail.next = Node(value)
        return
      
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        tail = self.head
        self.head = Node(value)
        self.head.next = tail
        return

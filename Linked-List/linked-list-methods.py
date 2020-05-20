class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
#         
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Append: append 'value' at the end of the list
    # time: O(n); space: O(1)
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = Node(value)
        return
    
    # Prepend
    
    # Search
    
    # Remove
    
    # Pop
    
    # Insert
    
    # Size
    
    # To python list

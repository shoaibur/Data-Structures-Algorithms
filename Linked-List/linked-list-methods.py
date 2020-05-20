class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
#         
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Append: append 'value' at the end of the list
    # time: O(n), space: O(1)
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = Node(value)
        return
    
    # Prepend: prepend 'value' at the begining of the list
    # time: O(1), space: O(1)
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        tail = self.head
        self.head = Node(value)
        self.head.next = tail
        return
    
    # Search: search for a 'value' and return the node
    def search(self, value):
        if self.head is None:
            return None
        tail = self.head
        while tail:
            if tail.next.value == value:
                return tail
        return None
    
    # Remove
    
    # Pop
    
    # Insert
    
    # Size
    
    # To python list

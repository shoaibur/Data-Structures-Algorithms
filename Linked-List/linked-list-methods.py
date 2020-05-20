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
    # time: O(n), space: O(1)
    def search(self, value):
        if self.head is None:
            return None
        tail = self.head
        while tail:
            if tail.next.value == value:
                return tail
            tail = tail.next
        return None
    
    # Remove: remove first occurence of a 'value'
    # time: O(n), space: O(1)
    def remove(self, value):
        if self.head is None:
            return
        tail = self.head
        while tail:
            if tail.next.value == value:
                tail.next = tail.next.next
                return
            tail = tail.next
        return
    
    # Pop: return the value of the first node and remove the node from the list
    # time: O(1), space: O(1)
    def pop(self):
        if self.head is None:
            return None
        tail = self.head
        self.head = tail.next
        return tail.value
    
    # Insert
    
    # Size
    
    # To python list

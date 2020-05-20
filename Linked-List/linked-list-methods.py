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
            return
        tail = self.head
        while tail:
            if tail.next.value == value:
                return tail
            tail = tail.next
        return
    
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
            return
        tail = self.head
        self.head = tail.next
        return tail.value
    
    # Insert: insert a 'value' at a given 'position'
    # time: O(n), space: O(1)
    def insert(self, value, position):
        if self.head is None:
            self.head = Node(value)
            return
        if position == 0:
            self.prepend(value)
            return
        index = 0
        tail = self.head
        while tail and index <= position:
            if index == position:
                new_node = Node(value)
                new_node.next = tail.next
                tail.next = new_node
                return
        self.append(value)
        return
    
    # Size: return the length of the list
    # time: O(n), space: O(1)
    def size(self):
        if self.head is None:
            return 0
        length = 1
        tail = self.head
        while tail.next:
            length += 1
            tail = tail.next
        return length
    
    # To python list: convert linked list to a python list
    # time: O(n), space: O(n)
    def to_python_list(self):
        if self.head is None:
            return []
        plist = []
        tail = self.head
        while tail.next:
            plist.append(tail.value)
            tail = tail.next
        plist.append(tail.value)
        return plist

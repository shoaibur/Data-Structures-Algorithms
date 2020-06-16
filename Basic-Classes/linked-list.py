class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value): # O(n)
        if self.head is None:
            self.head = Node(value)
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = Node(value)
    
    def prepend(self, value): # O(1)
        if self.head is None:
            self.head = Node(value)
            return
        tail = self.head
        self.head = Node(value)
        self.head.next = tail
        
    def insert(self, insert_value, after_value): # O(n)
        if self.head is None:
            self.head = Node(insert_value)
        tail = self.head
        while tail:
            if tail.value == after_value:
                temp = tail.next
                tail.next = Node(insert_value)
                tail.next.next = temp
                break
            tail = tail.next
    
    def delete(self, value): # O(n)
        if self.head is None:
            return
        tail = self.head
        while tail.next:
            if tail.next.value == value:
                tail.next = tail.next.next
                return
            tail = tail.next
        raise ValueError('Invalid node value!')
        
    def tolist(self): # O(n)
        if self.head is None: return []
        out = []
        tail = self.head
        while tail:
            out.append(tail.value)
            tail = tail.next
        return out
    
    def reverse(self): # O(n)
        prev = None
        while self.head:
            temp = self.head
            self.head = self.head.next
            temp.next = prev
            prev = temp
        self.head = prev
        
    def traverse(self): # O(n)
        out = []
        if self.head is None:
            return out
        tail = self.head
        while tail:
            out.append(tail.value)
            tail = tail.next
        return out
    
# 
nums = [1,2,3,4]
ll = LinkedList()
for num in nums:
    ll.append(num)
print('orignal:', ll.traverse())

ll.delete(2)
print('delete:', ll.traverse())

ll.prepend(2)
print('prepend:', ll.traverse())

ll.insert(5,3)
print('insert:', ll.traverse())

ll.reverse()
print('reverse:', ll.traverse())

print('to list:', ll.tolist())

# Outputs:
# orignal: [1, 2, 3, 4]
# delete: [1, 3, 4]
# prepend: [2, 1, 3, 4]
# insert: [2, 1, 3, 5, 4]
# reverse: [4, 5, 3, 1, 2]
# to list: [4, 5, 3, 1, 2]

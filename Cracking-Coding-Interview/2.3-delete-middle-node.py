# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first 
# and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
# EXAMPLE
# Input: the node c from the linked list a - >b- >c - >d - >e- >f
# Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def delete(self, value):
        if self.head is None:
            return
        tail = self.head
        while tail.next:
            if tail.next.value == value:
                tail.next = tail.next.next
                return
            tail = tail.next
        raise ValueError('Invalid node value!')
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = Node(value)
        
    def traverse(self):
        out = []
        if self.head is None:
            return out
        tail = self.head
        while tail:
            out.append(tail.value)
            tail = tail.next
        return out
# 
chars = ['a', 'b', 'c', 'd', 'e', 'f']
ll = LinkedList()
for char in chars:
    ll.append(char)
print('orignal:', ll.traverse())

ll.delete('c')
print('after deleting:', ll.traverse())

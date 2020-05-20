# Create a  node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
# Create a simple linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Traverse through the linked list
current_node = head
while current_node is not None:
    print(current_node.value)
    current_node = current_node.next

# Create a node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
#         
def create_linked_list_from_array(arr):
    head = None
    tail = None
    
    for value in arr:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next
    return head

# Example
arr = [1,2,3,4,5]
head = create_linked_list_from_array(arr)

# Print ll
current_node = head
while current_node is not None:
    print(current_node.value)
    current_node = current_node.next

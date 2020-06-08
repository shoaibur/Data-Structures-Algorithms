# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def append(head, value):
    if head is None: return Node(value)
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = Node(value)
    return head

def prepen(head, value):
    if head is None: return Node(value)
    tail = head
    head = Node(value)
    head.next = tail
    return head

def ll2array(head):
    if head is None: return None
    out = []
    tail = head
    while tail:
        out.append(tail.value)
        tail = tail.next
    return out

def array2ll(nums):
    if not nums: return Node(None)
    head = Node(nums[0])
    for num in nums[1:]:
        head = append(head, num)
    return head

def kth_to_last(head, k):
    counter = 0
    tail = head
    while counter < k:
        tail = tail.next
        counter += 1
    return tail

# Tests
nums = [2,1,3,2,4]
head = array2ll(nums)
new_head = kth_to_last(head, 2)
ll2array(new_head)

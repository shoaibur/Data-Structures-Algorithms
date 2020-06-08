# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

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

def remove_dups(head):
    nums = ll2array(head)
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
    return array2ll(list(d.keys()))

# Tests
nums = [2,1,3,2,4]
head = array2ll(nums)
new_head = remove_dups(head)
ll2array(new_head)

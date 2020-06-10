# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by 
# splicing together the nodes of the first two lists.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = Node(value)
    
def nums2LL(nums):
    head = LinkedList()
    for num in nums:
        head.append(num)
    return head
    
def LL2nums(self):
    out = []
    tail = self.head
    while tail:
        out.append(tail.value)
        tail = tail.next
    return out

def merge_two_sorted_lists(nums1, nums2):
    nums = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1
    nums += nums1[i:]
    nums += nums2[j:]
    return nums


def merge_two_sorted_LL(head1, head2):
    nums1 = LL2nums(head1)
    nums2 = LL2nums(head2)
    nums = merge_two_sorted_lists(nums1, nums2)
    return nums2LL(nums)

nums1 = [1,2,4]
nums2 = [1,3,4]
head1 = nums2LL(nums1)
head2 = nums2LL(nums2)
head = merge_two_sorted_LL(head1, head2)
LL2nums(head)

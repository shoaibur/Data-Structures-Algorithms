# Add two numbers:
# Problem 1: One number is 1
# Problem 2: Two numbers are integers/binary; add them without using arithmatic operators
# Problem 3: Two numbers are strings
# Problem 4: Two numbers are python lists
# Problem 5: Two numbers are linked lists


# Problem 2: Two numbers are integers/binary; add them without using arithmatic operators
# summ = xor(x, y) = x^y
# carry = and(x, y) then left shift = (x & y) << 1
def add(x, y):
    if y == 0: return x
    summ = x ^ y
    carry = (x & y) << 1
    return add(summ, carry)

# Problem 3: Two numbers are strings
def add_numbers_string(s1, s2):
    if len(s1) == 0: return s2
    if len(s2) == 0: return s1
    return str( int(s1) + int(s2) )
    
# Problem 4: Two numbers are python lists
# Solution 1 -- Add element-by-element
def add(nums1, nums2):
    n1, n2 = len(nums1), len(nums2)
    if n1 > n2:
        nums2 = [0]*(n1-n2) + nums2
    if n2 > n1:
        nums1 = [0]*(n2-n1) + nums1
    carry = 0
    for i in range(len(nums1)):
        summ = nums1[i] + nums2[i] + carry
        summ, carry = summ % 10, summ // 10
        nums1[i] = summ
    if carry > 0:
        nums1 = [carry] + nums1
    return nums1
# Solution 2 -- convert lists into integers and add them
def add(nums1, nums2):
    nums1 = nums1[::-1]
    nums2 = nums2[::-1]
    int1 = nums1[0]
    int2 = nums2[0]
    for i, num in enumerate(nums1[1:]):
        int1 += num * 10**(i+1)
    for i, num in enumerate(nums2[1:]):
        int2 += num * 10**(i+1)
    return int1 + int2

# Problem 5: Two numbers are linked lists
# Solution 1 -- convert lls into integers, sum them and back the sum to the ll
def add(nums1, nums2):
    # ll to int
    int1 = ll2int(nums1)
    int2 = ll2int(nums2)
    # sum
    summ = int1 + int2
    # Back to ll
    head = int2ll(summ)
    return head

def ll2int(head):
    if head is None: return 0
    tail = head
    nums = []
    while tail:
        nums.append(tail.value)
        tail = tail.next
    nums = int( ''.join([str(num) for num in nums]) )
    return nums

def int2ll(nums):
    nums = [int(num) for num in str(nums)]
    head = Node(nums[0])
    for num in nums[1:]:
        append(head, num)
    return head

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

# Solution 2 -- reverse lls, sum them element-by-element and prepend the sums to a new ll
def add(head1, head2):
    # Equalize length
    n1 = length(head1)
    n2 = length(head2)
    if n1 > n2:
        for i in range(n1-n2):
            head2 = prepend(head2, 0)
    if n2 > n1:
        for i in range(n2-n1):
            head1 = prepend(head1, 0)
    # Reverse ll
    head1 = reverse(head1)
    head2 = reverse(head2)
    
    # Sum and store into new ll
    new_head = Node(None)
    carry = 0
    tail1 = head1
    tail2 = head2
    while tail1:
        summ = tail1.value + tail2.value + carry
        summ, carry = summ % 10, summ // 10
        new_head = prepend(new_head, summ)
    if carry > 0:
        new_head = prepend(new_head, carry)
    return new_head

def reverse(head):
    new_head = Node(None)
    tail = head
    while tail:
        value = tail.value
        new_head = prepend(new_head, value)
    return new_head
def prepend(head, value):
    if head is None: return Node(value)
    tail = head
    head = Node(value)
    head.next = tail
    return head
def length(head):
    tail = head
    count = 0
    while tail:
        count += 1
        tail = tail.next
    return count

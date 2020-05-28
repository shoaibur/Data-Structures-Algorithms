def even_after_odd(nums):
    even = []
    odd = []
    for num in nums:
        if num % 2: odd.append(num)
        else: even.append(num)
    return odd + even
  
def even_after_odd(head):
    even = None
    odd = None
    tail = head
    while tail:
        if tail.value % 2:
            odd = append(odd, tail.value)
        else:
            even = append(even, tail.value)
        tail = tail.next
    tail = odd
    while tail.next:
        tail = tail.next
    tail.next = even
    return odd
  
    

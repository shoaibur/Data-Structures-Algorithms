def reverse_linked_list(head):
    prev = None
    tail = head
    while tail:
        temp = tail.next
        tail.next = prev
        prev = tail
        tail = temp
    return prev
    

def copyRandomList(head)
    if not head: return head
    # create duplicates
    tail = head
    while tail:
        temp = tail.next
        tail.next = Node(tail.val)
        tail.next.next = temp
        tail = temp
    # copying random pointers to duplicates
    tail = head
    while tail:
        if tail.random:
            tail.next.random = tail.random.next 
        else:
            tail.next.random = None
        tail = tail.next.next
    # Separate two linked lists
    org = head
    copy   = head.next
    clone = head.next
    while(org):
        org = org.next.next
        copy.next = copy.next.next if copy.next else None
        copy = copy.next
    return clone

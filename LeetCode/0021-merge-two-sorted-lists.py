def mergeTwoLists(l1, l2)
    if l1 is None: return l2
    if l2 is None: return l1
    
    t1 = l1
    t2 = l2
    l3 = ListNode(0)
    t3 = l3
    while t1 and t2:
        if t1.val <= t2.val:
            t3.next = ListNode(t1.val)
            t1 = t1.next
        else:
            t3.next = ListNode(t2.val)
            t2 = t2.next
        t3 = t3.next
    while t1:
        t3.next = ListNode(t1.val)
        t3 = t3.next
        t1 = t1.next
    while t2:
        t3.next = ListNode(t2.val)
        t3 = t3.next
        t2 = t2.next
    return l3.next

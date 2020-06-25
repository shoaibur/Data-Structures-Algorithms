def add_two_numbers(l1, l2):
    result = ListNode(0)
    result_tail = result

    t1, t2, carry = l1, l2, 0
    while t1 or t2 or carry:
        v1 = (t1.val if t1 else 0)
        v2 = (t2.val if t2 else 0)
        carry, s = divmod(v1 + v2 + carry, 10)

        result_tail.next = ListNode(s)
        result_tail = result_tail.next

        t1 = (t1.next if t1 else None)
        t2 = (t2.next if t2 else None)

    return result.next

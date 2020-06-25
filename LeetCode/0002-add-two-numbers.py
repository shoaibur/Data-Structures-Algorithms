    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        out = ListNode(0)
        out_tail = out
        
        t1, t2, carry = l1, l2, 0
        while t1 or t2 or carry:
            v1 = (t1.val if t1 else 0)
            v2 = (t2.val if t2 else 0)
            carry, s = divmod(v1 + v2 + carry, 10)
            
            out_tail.next = ListNode(s)
            out_tail = out_tail.next
            
            t1 = (t1.next if t1 else None)
            t2 = (t2.next if t2 else None)
            
        return out.next

def getIntersectionNode(headA, headB):
    if headA == None or headB == None: return None
    pA, pB = headA, headB
    while pA != pB:
        pA = headB if pA == None else pA.next
        pB = headA if pB == None else pB.next
    return pA

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        newlists = []
        for list_ in lists:
            tail = list_
            a = []
            while tail:
                a.append(tail.val)
                tail = tail.next
            if len(a) > 0:
                newlists.append(a)
        lists = newlists
                
        results = []
        heap = []
        
        for k in range(len(lists)):
            heap.append( (lists[k][0], k, 0) )
        heapq.heapify(heap)
        
        while len(heap) > 0:
            val, k, indx = heapq.heappop(heap)
            results.append(val)
            if len(lists[k]) > indx+1:
                heapq.heappush( heap, (lists[k][indx+1], k, indx+1) )
        
        head = ListNode(0)
        tail = head
        for num in results:
            tail.next = ListNode(num)
            tail = tail.next
        return head.next

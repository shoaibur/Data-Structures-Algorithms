def level_order(root):
    if root is None: return root
    # import queue
    res = []
    q = [] # queue.Queue()
    q.append(root)
    while len(q) > 0: # q.qsize() > 0
        n = len(q) # q.qsize()
        a = []
        while n != 0:
            # deq
            p = q.pop(0) # q.get()

            # visit
            a.append(p.val)

            #print(p.left.val, p.right.val)

            # enq left child
            if p.left is not None:
                q.append(p.left) # q.put(p.left)
            # enq right child
            if p.right is not None:
                q.append(p.right) # q.put(p.right)
            n -= 1
        res.append(a)
    return res

import collections
def levelOrderBottom(root)
    
    if root is None: return []
    
    q = collections.deque()
    q.append(root)
    out = []
    
    while len(q) > 0:
        size = len(q)
        count = 0
        temp = []
        while count < size:
            pop = q.popleft()
            temp.append(pop.val)
            count += 1
            
            if pop.left:
                q.append(pop.left)
            if pop.right:
                q.append(pop.right)
        
        out.append(temp)
    return out[::-1]

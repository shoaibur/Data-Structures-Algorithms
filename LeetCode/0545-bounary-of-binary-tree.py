from collections import deque
def boundary_tree(root):
    if root is None: return []
    if root.left is None and root.right is None:
        return [[root.val]]
    q = deque()
    q.append(root)
    levels = []
    while len(q) > 0:
        temp = []
        size = len(q)
        count = 0
        while count < size:
            p = q.popleft()
            temp.append(p.val)
            
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
                
            count += 1
        levels.append(temp)
        
    boundary = levels[0]
    for item in levels[1:-1]:
        boundary.append(item[0])
    boundary += levels[-1]
    for item in levels[-2:0:-1]:
        boundary.append(item[-1])
    return boundary

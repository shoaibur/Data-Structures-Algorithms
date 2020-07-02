import collections
def zigzagLevelOrder(root)
    if root is None: return root
    out = []
    q = collections.deque()
    q.append(root)
    while len(q) > 0:
        size = len(q)
        count = 0
        temp = []
        while count < size:
            popped = q.popleft()
            temp.append(popped.val)
            count += 1
            if popped.left:
                q.append(popped.left)
            if popped.right:
                q.append(popped.right)
        out.append(temp)
    out = [item[::-1] if i%2 else item for i, item in enumerate(out)]
    return out

def isValidBST(root)
    if root is None: return True
    out = []
    def inorder(root):
        if root.left:
            inorder(root.left)
        out.append(root.val)
        if root.right:
            inorder(root.right)
        return out
    
    out = inorder(root)
    for i in range(len(out)-1):
        if out[i] >= out[i+1]:
            return False
    return True
